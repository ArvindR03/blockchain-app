import hashlib
import ecdsa

class Transaction:
    def __init__(self, sender_public_key, sender, receiver, amount):
        self.sender = sender
        self.sender_public_key = sender_public_key
        self.receiver = receiver
        self.amount = amount
        self.transactionID = self.calculate_transactionID()
        self.signature = None

    def calculate_transactionID(self):
        data = f"{self.sender}{self.receiver}{self.amount}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def check_valid_transaction(self, sender_balance):
        return True # to complete
    
    def sign_transaction(self, sender_private_key):
        private_key = ecdsa.SigningKey.from_string(bytes.fromhex(sender_private_key), curve=ecdsa.SECP256k1)
        transaction_data = f"{self.sender_public_key}{self.receiver}{self.amount}".encode()

        signature = private_key.sign_deterministic(transaction_data, hashfunc=hashlib.sha256, sigencode=ecdsa.util.sigencode_string)
        self.signature = signature.hex()

t = Transaction('hey', 0, 1, 100)
t.sign_transaction('private-key'.encode().hex())
print(t.signature)