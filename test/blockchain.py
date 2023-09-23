import hashlib
import time

class Block:
    def __init__(self, index, prev_hash, timestamp, transactions):
        self.index = index
        self.prev_hash = prev_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.hash) + self.prev_hash + str(self.timestamp) + str(self.transactions)
        return hashlib.sha256(data.encode()).hexdigest()
    

def create_genesis_block():
    return Block(0, "0", int(time.time), [])

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
    
class Blockchain:

    def __init__(self):
        self.chain = [create_genesis_block()]

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block_transactions):
        prev_block = self.get_last_block()
        new_block_index = prev_block.index + 1
        new_block_timestamp = int(time.time())
        new_block = Block(new_block_index, prev_block.hash, new_block_timestamp, new_block_transactions)

    def check_valid_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.prev_hash != prev_block.hash:
                return False
            
        return True
    
    

