from web3 import Web3, HTTPProvider
import json
import requests
# import pywifi
# from pywifi import *
# from pywifi import const
import cv2
import base64
# from utils import utils
import time
import numpy as np
target_times = 100
factor = 1000000000

web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
# contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])
configForlocal = {"address" : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
with open("ABI.json") as f:
    configForlocal["abi"] = json.load(f)


#set provider
web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
# web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

#get the contract
contract_instance = web3.eth.contract(address=configForlocal["address"], abi=configForlocal['abi'])

#the private key for accounts

# accounts = {
#     'proxy': {
#         'address': '0xD7397b3894DF7168E7a103508659FC6eC5580F6b',
#         'pass': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'
#     },
#     'edge1': {
#         'address': '0x383B9f270bC983fB7A848B744b8A23eB5eF99699',
#         'pass': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1'
#     },
#     'user': {
#         'address': '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149',
#         'pass': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c'
#     },
#     'edge3': {
#         'address': '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761', 
#         'pass': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
#     }
# }

# private_key = {
#     '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
#     '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
#     '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
#     '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
#     '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
# }

# user = accounts['user']['address']
# proxy = accounts['proxy']['address']
# edge1 = accounts['edge1']['address']
# edge3 = accounts['edge3']['address']

user = web3.eth.accounts[0]
proxy = web3.eth.accounts[1]
edge1 = web3.eth.accounts[2]
edge2 = web3.eth.accounts[3]
edge3 = web3.eth.accounts[4]

edge = edge1
private_key = {
    user: 'd97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4',
    proxy:'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309',
    edge1:'30341350fd95867002c89d32eb2f7c1b843e8d95310bf3c5b14e5c1ccd6db44b',
    edge2:'e487dc9904ae94719b86d98edb970f82fbfb6c07098f3370c014b53749519ff2',
    edge3:'fce674c91f36e1c52988aa8db06a64fcb7b85f99a42b8171216fae71bd8d40e3'
}
edge_address = {
    '1' : edge,
    'TP-LINK_4423': edge
}

password_map = {
    '1' : '20690539',
    'TP-LINK_4423':'jiangxing123'
}

# num_of_tasks = target_times
# print('-----------------------------------------------------')
# #check each account's balance
# print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
# print("The balance for user before transaction:", web3.eth.getBalance(user))
# print("The balance for contract before transaction:", web3.eth.getBalance(configForlocal['address']))
# print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
# total_gas = 0

begin = time.time()
#each edge register first:
# r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})
# total_gas += json.loads(r.text)['gas']

#user build PC itself
tx = contract_instance.functions.openChannel(edge1).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
transaction_hash = web3.toHex(a)
gas = web3.eth.waitForTransactionReceipt(transaction_hash).gasUsed

total_time = time.time() - begin
print(total_time)
