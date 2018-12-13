#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random

#get contract's address and abi
config = { "address"  : "0xc9C239CDc4d986d8458ebbBe1409ac5d269E3145"}
with open("/Users/a931759898/Desktop/Desktop/BlockChain/Edge+BlockChain/Proxy2/login/ABI.JSON", 'r') as f:
    config["abi"] = json.load(f)

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


#how many times of simulation
simulation_times = 1000
choice_list = list(range(1, 11))
count = 1
private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4'}
def sign_transaction(user_address, taker_address, deposit_money):
    information = web3.soliditySha3(['address', 'address', 'uint256'], [proxy, edge, 0])
    signed_message = web3.eth.account.signHash(information, private_key=private_key[user_address])
    return signed_message

def to_32byte_hex(val):
   return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

# signed_message = sign_transaction(proxy, edge, 5)

information = web3.soliditySha3(['address', 'address', 'uint256'], [proxy, edge, 0])

signed_message = web3.eth.account.signHash(information, private_key=private_key[proxy])
print(contract_instance.functions.getChannelCollateral(proxy, edge).call())
print(contract_instance.functions.verifySignature(proxy, edge, 0, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).call({'from':edge}))
print(contract_instance.functions.getChannelCollateral(proxy, edge).call())
print(web3.eth.account.recoverHash(information, signature = signed_message.signature) == proxy)

# print(to_32byte_hex(signed_message.s))
# print(proxy)
# print(edge)
# print(information.hex())

