import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    #changing my starting nonce to get different variance from the rest of the group
    #this should be called a nonce... not a fan of calling it proof as it isn't the proof, the proof is the alignment boolean condition
    #in the valid_proof statement
    proof = 100000000000
    #  TODO: Your code here

    #getting the hash of the work attempt
    last_proof_byte = f'{last_proof}'.encode()
    #converting the previous proof to SHA256
    last_proof_hash = hashlib.sha256(proof_byte).hexdigest()
    #check if the proof is valid, if it is not, incriment the proof by 1 and try again!
    while valid_proof(last_proof_hash, proof) is False:
        proof += 1


    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!

    #takes the nonce value and converts it to SHA256
    byte_guess = f'{proof}'.encode()
    hashed_guess = hashlib.sha256(block_guess).hexdigest()

    #for the multi-ourobrous proof of work algorithim
    #the last 6 digits of the hash need to equal the first 6 digits of the new hash
    #this boolean check goes into the while statement above to see if a valid bock was found.
    return last_hash[-6:] == hashed_guess[:6]


    pass


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
