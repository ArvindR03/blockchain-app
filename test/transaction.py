import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.transactionID = self.calculate_transactionID()

    def calculate_transactionID(self):
        data = f"{self.sender}{self.receiver}{self.transactionID}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def check_valid_transaction(self, sender_balance):
        return True # to complete