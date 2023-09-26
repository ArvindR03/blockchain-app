import datetime
import hashlib
import json
import transaction

class BlockChain:

    def __init__(self):
        self.chain = []
        self.genesis_block()

    
    # this is the hash operation that is used to check for proof of work
    @staticmethod
    def hash_op(new_proof, prev_proof):
        return hashlib.sha256(
                    str(new_proof ** 2 - prev_proof **2).encode()
                ).hexdigest()
        # should result in the first 4 digits of the hash being '0000'




    # this is used to hash an entire block
    @staticmethod
    def hash_block(block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    



    # this is used to check if a chain is valid
    @staticmethod
    def is_chain_valid(chain):
        prev = chain[0]

        for i in range(len(chain)):
            block = chain[i]
            if block["previous_hash"] != BlockChain.hash_block([prev]):
                return False
            
            prev_proof = prev["proof"]  
            curr_proof = block["proof"]

            hash_op = BlockChain.hash_op(prev_proof, curr_proof)
            if hash_op[:4] != '0000':
                return False
            
            prev = block
                
        return True
    

    # TODO: make this harder to break
    # this is the proof of work function for miners to be able to manipulate the chain
    @staticmethod
    def proof_of_work(prev_proof):
        new_proof = 1
        check_proof = False

        while not check_proof:
            hash_op = BlockChain.hash_op(new_proof, prev_proof)
            if hash_op[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        
        return new_proof
    


    # TODO: find a way of returning information to the user that the block was not added
    # ----- maybe return an error message somehow rather than the block?
    # TODO: an efficient way of checking that the type of transactions is List
    # this is used to add a block to the chain
    def create_and_add_block(self, proof, prev_hash, transactions: list = []):
        block = {
            'index': len(self.chain),
            'transactions': [],
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': prev_hash
        }

        for t in transactions:
            if type(t) == transaction.Transaction:
                block['transactions'].append(t.to_dict())
            elif type(t) == dict:
                block['transactions'].append(t)

        new_chain = self.chain
        new_chain.append(block)

        if BlockChain.is_chain_valid(new_chain):
            self.chain.append(block)
            return block
        else:
            pass
    


    
    # this is used to create and add the genesis block to the chain
    def genesis_block(self):
        return self.create_and_add_block(proof=1, prev_hash='0')
    


    
    # this is a getter function to get the most recent block from the chain
    def get_previous_block(self):
        return self.chain[-1]
    
    
# example use of the backend:
    
b = BlockChain()

t1 = transaction.Transaction('arvind', 'idkk', '2')

def client_add_block(b):

    prev_block = b.get_previous_block()
    prev_proof = prev_block['proof']

    curr_proof = BlockChain.proof_of_work(prev_proof)
    prev_hash = BlockChain.hash_block(prev_block)

    new_block = b.create_and_add_block(curr_proof, prev_hash, transactions=[t1])

for i in range(10):
    client_add_block(b)

for i in b.chain:
    print(i)
    print("----------------------")