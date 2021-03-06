#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
import numpy as np
# from utils import sign_transaction, to_32byte_hex

def sign_transaction(user_address, taker_address, deposit_money):
    """
    to sign a cheque
    input: signer's address, receiver's address, amount
    output: the hash of the message and the signed message
    """
    message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
    signed_message = web3.eth.account.signHash(message_hash, private_key=private_key[user_address])
    return (message_hash,signed_message)


def to_32byte_hex(val):
    """
    for data type conversion
    To invoke the solidity's function correctly
    """
    return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))


def get_random_number():
    """
    input: None
    output: return a random integer in 1 - 9
    """
    return random.randint(1, 10)





#get contract's address and abi
config = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
with open("/Users/a931759898/Desktop/test/1.json") as f:
    config["abi"] = json.load(f)



#set provider
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))


#the proxy for trainsiting the money
proxy = web3.eth.accounts[0]


#the sender
user = web3.eth.accounts[1]


#the receiver
edge = web3.eth.accounts[2]

#get the contract
contract_instance = web3.eth.contract(address=config["address"], abi=config['abi'])

#the private key for accounts
private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', user: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}


#store all the edges availzble
edges = [
    web3.eth.accounts[2],
    web3.eth.accounts[3],
    web3.eth.accounts[4],
    web3.eth.accounts[5],
    web3.eth.accounts[6],
    web3.eth.accounts[7],
    web3.eth.accounts[8],
    web3.eth.accounts[9],
]


#assume user is moving, and the available edges are not fixed
num_of_available_edges = random.randint(1, 8)

#get all available edges
available_edges = np.random.choice(edges, replace=False, size=num_of_available_edges)
print(available_edges.tolist())


print('-----------------------------------------------------')
#check each account's balance
print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
print("The balance for user before transaction:", web3.eth.getBalance(user))
print("The balance for edge before transaction:", web3.eth.getBalance(edge))



#user build PC itself
contract_instance.functions.openChannel(proxy).transact({'from':user, 'value':10, 'gas':600000})
print('-----------------------------------------------------')


# check the balance in payment channel
print('The balance for each channel')
print("before transaction:")
print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())



#user sign transaction, cost 5 coin
valueTransferred = 5
hashmes, signed_message = sign_transaction(user, proxy, valueTransferred)


#submit the cheque to proxy
data = {'senderAddress':user, 
'recipientAddress':proxy, 'valueTransferred':valueTransferred, 'v' : signed_message.v, 'r' : to_32byte_hex(signed_message.r), 's' : to_32byte_hex(signed_message.s),
'availableEdges':available_edges.tolist()}
# headers = {'Content-Type': 'application/json'}
r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)

print()
print("after transaction:")
print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
print('-----------------------------------------------------')
print("The balance for proxy after transaction:", web3.eth.getBalance(proxy))
print("The balance for user after transaction:", web3.eth.getBalance(user))
print("The balance for edge after transaction:", web3.eth.getBalance(edge))



