from hashlib import sha256

def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    pass

if __name__ == '__main__':
    transactions = '''
    Dhaval -> Bhavin -> 20,
    Mando -> Cara -> 45
    '''
    new_hash = mine(transactions)
    print(SHA256('ABC'))
