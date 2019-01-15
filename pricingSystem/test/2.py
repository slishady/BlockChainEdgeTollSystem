#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
#get contract's address and abi
config = { "address"  : "0xBBC631C80f102633cb7ecd20cc02FA2A8Fb456c7"}
# with open("/Users/a931759898/Desktop/Desktop/BlockChain/Edge+BlockChain/Proxy2/login/ABI.JSON", 'r') as f:
#     config["abi"] = json.load(f)

# with open("/Users/a931759898/Desktop/test/1.json") as f:
#     config["abi"] = json.load(f)

with open("ABI.json") as f:
    config["abi"] = json.load(f)


#set provider
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))


#the proxy for trainsiting the money
proxy = web3.eth.accounts[1]


#the sender
user = web3.eth.accounts[0]


#the receiver
edge1 = web3.eth.accounts[2]

edge2 = web3.eth.accounts[3]
edge3 = web3.eth.accounts[4]

edge = edge1
#get the contract
contract_instance = web3.eth.contract(address=config["address"], abi=config['abi'])


private_key = {
    user: '93eeceaf872686b748acda18ba68acd4c13d2b786203edee237bee8017a79105',
    proxy:'57730ecf94645a7cbeb381164e8577e1122f6e909f2b46dd839480b8916a4fc2',
    edge1:'7cad2ea1120dae749e68dfd62af603f423ebc9221fd4ac157b33873528b275d2',
    edge2:'6cd79303468fe58a83b1c40963331a14b318b6d0497df22e668d319078174921',
    edge3:'19e5a2a2716310a94704b976755c640bf8a4ec0253c400c080f3bc1849af6d36'
}

#how many times of simulation
# simulation_times = 1000
# choice_list = list(range(1, 11))
# count = 1
# private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4'}
def sign_transaction(user_address, taker_address, deposit_money):
    information = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
    signed_message = web3.eth.account.signHash(information, private_key=private_key[user_address])
    return signed_message

def to_32byte_hex(val):
   return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

# signed_message = sign_transaction(proxy, edge, 5)

# information = web3.soliditySha3(['address', 'address', 'uint256'], [proxy, edge, 0])

# signed_message = web3.eth.account.signHash(information, private_key=private_key[proxy])
signed_message = sign_transaction(user, proxy, 1)
print(contract_instance.functions.getChannelCollateral(user, proxy).call())
print(contract_instance.functions.getChannelCollateral(proxy, edge).call())

print(contract_instance.functions.verifySignature(user, proxy, 1, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).call())
a = contract_instance.functions.closeChannel(user, proxy, 1, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).transact({'from':proxy})
# print(contract_instance.functions.getChannelCollateral(proxy, edge).call())
# print(contract_instance.functions.verifySignature(proxy, edge, 0, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).call({'from':edge}))
# print(contract_instance.functions.getChannelCollateral(proxy, edge).call())
# print(web3.eth.account.recoverHash(information, signature = signed_message.signature) == proxy)
print(len(web3.eth.accounts))

# print(to_32byte_hex(signed_message.s))
# print(proxy)
# print(edge)
# print(information.hex())

