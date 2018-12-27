from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
import numpy as np

def sign_transaction(user_address, taker_address, deposit_money):
    """
    to sign a cheque
    input: signer's address, receiver's address, amount
    output: the hash of the message and the signed message
    """
    message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
    signed_message = web3.eth.account.signHash(message_hash, private_key=accounts['edge3']['pass'])
    return (message_hash,signed_message)

def to_32byte_hex(val):
    """
    for data type conversion
    To invoke the solidity's function correctly
    """
    return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215"))
accounts = {
    'proxy': {
        'address': '0xD7397b3894DF7168E7a103508659FC6eC5580F6b',
        'pass': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'
    },
    'edge1': {
        'address': '0x383B9f270bC983fB7A848B744b8A23eB5eF99699',
        'pass': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1'
    },
    'user': {
        'address': '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149',
        'pass': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c'
    },
    'edge3': {
        'address': '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761', 
        'pass': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
    }
}
# web3.personal.unlockAccount(accounts['user']['address'], accounts['user']['pass'])
# web3.personal.unlockAccount(accounts['proxy']['address'], accounts['proxy']['pass'])
# web3.personal.unlockAccount(accounts['edge1']['address'], accounts['edge1']['pass'])
# web3.personal.unlockAccount(accounts['edge2']['address'], accounts['edge2']['pass'])
# web3.personal.unlockAccount(accounts['edge3']['address'], accounts['edge3']['pass'])
# print(web3.personal.listAccounts)
# print(web3.eth.getBalance(accounts['user']['address']))
# print(web3.eth.accounts)
configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
with open("ABI.json") as f:
    configForRinkeby["abi"] = json.load(f)

user = accounts['user']['address']
proxy = accounts['proxy']['address']
edge3 = accounts['edge3']['address']
edge1 = accounts['edge1']['address']

#get the contract
contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])


# print(contract_instance.functions.getChannelCollateral(edge3, proxy).call())
# print(web3.eth.getBalance(configForRinkeby['address']))
print(contract_instance.functions.getChannelCollateral(proxy, edge3).call())
print(contract_instance.functions.getChannelCollateral(user, proxy).call())
print(contract_instance.functions.getChannelCollateral(proxy, edge1).call())

# # print(web3.eth.getBalance(accounts['proxy']['address']))
# tx = contract_instance.functions.openChannel(proxy).buildTransaction({'value':web3.toWei(2, 'ether'), 'nonce': web3.eth.getTransactionCount(edge3), 'gas':600000})
# # # # nonce = web3.eth.getTransactionCount(proxy)  
# signed_txn = web3.eth.account.signTransaction(tx, private_key=accounts['edge3']['pass'])
# web3.eth.sendRawTransaction(signed_txn.rawTransaction)
# print(contract_instance.functions.getChannelCollateral(edge3, proxy).call())
# print(web3.eth.getBalance(configForRinkeby['address']))
# # print(web3.eth.getBalance(accounts['proxy']['address']))
# print(contract_instance.functions.getChannelCollateral(proxy, user).call())
# print(web3.eth.getBalance(configForRinkeby['address']))
# # print(len('24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'))
# _, signed_message = sign_transaction(edge3, proxy, 1)
# # print(web3.eth.getBalance(accounts['user']['address']))
# # # print(web3.eth.gasPrice)
# factor = web3.toWei(1, 'ether')
# tx = contract_instance.functions.closeChannel(edge3, proxy, 1, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).buildTransaction({'nonce': web3.eth.getTransactionCount(proxy), 'gas':700000})
# print(contract_instance.functions.getChannelCollateral(edge3, proxy).call())
# print(contract_instance.functions.verifySignature(edge3, proxy, 1, signed_message.v, to_32byte_hex(signed_message.r), to_32byte_hex(signed_message.s)).call())
# signed_txn = web3.eth.account.signTransaction(tx, private_key=accounts['proxy']['pass'])
# # print(60000*web3.eth.gasPrice)
# print(web3.eth.sendRawTransaction(signed_txn.rawTransaction))
# print(contract_instance.functions.getChannelCollateral(edge3, proxy).call())
# # print(web3.eth.getBalance(configForRinkeby['address']))
# print(contract_instance.functions.getChannelCollateral(proxy, user).call())




