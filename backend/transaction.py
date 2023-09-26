import datetime
import hashlib
import json


class Transaction:

    def __init__(self, sender, recipient, amount, timestamp = datetime.datetime.now()) -> None:
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = str(timestamp)
        self.transactionID = self.generate_transactionID()

    
    def generate_transactionID(self):
        return Transaction.get_transactionID({
            'timestamp': self.timestamp,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        })
    
    @staticmethod
    def get_transactionID(transaction: dict):
        data = json.dumps(transaction, sort_keys=True).encode()
        return hashlib.sha256(data).hexdigest()

    def __str__(self) -> str:
        return f"Transaction ID: {self.transactionID}, Sender: {self.sender}, Recipient: {self.recipient}, Amount: {self.amount}, Timestamp: {self.timestamp}"
    
    def to_dict(self) -> dict:
        return {
            'transaction_id': self.transactionID,
            'timestamp': self.timestamp,
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }
    
    @staticmethod
    def is_valid_transaction(transaction: dict):
        for key in ['transaction_id', 'timestamp', 'sender', 'recipient', 'amount']:
            if key not in transaction:
                return False
        if transaction['transaction_id'] != Transaction.get_transactionID(transaction):
            return False
        return True
        