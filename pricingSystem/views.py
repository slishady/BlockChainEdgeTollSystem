# #libraries
# #django, web3
# from django.shortcuts import render
# from django.http import HttpResponse
# from pricingSystem import models
# from web3 import Web3, HTTPProvider
# from web3.contract import ConciseContract
# import json
# import requests
# # from django.core import serializers
# # from module_name import sign_transaction, to_32byte_hex
# import random

# #set up connecntion 
# #for test
# web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
# # web3 = Web3((HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")))

# #the contract address and abi
# config = { "address"  : "0x2Fad070013134B1486a50FDe06c9ecF5BC84BD9d"}
# # with open("test/ABI.json") as f:
# #     config["abi"] = json.load(f)


# a = [
#     {
#     "constant": True,
#     "inputs": [
#       {
#         "name": "",
#         "type": "address"
#       },
#       {
#         "name": "",
#         "type": "address"
#       }
#     ],
#     "name": "channels",
#     "outputs": [
#       {
#         "name": "sender",
#         "type": "address"
#       },
#       {
#         "name": "recipient",
#         "type": "address"
#       },
#       {
#         "name": "collateral",
#         "type": "uint256"
#       }
#     ],
#     "payable": False,
#     "stateMutability": "view",
#     "type": "function"
#   },
#   {
#     "constant": False,
#     "inputs": [
#       {
#         "name": "recipient",
#         "type": "address"
#       }
#     ],
#     "name": "openChannel",
#     "outputs": [],
#     "payable": True,
#     "stateMutability": "payable",
#     "type": "function"
#   },
#   {
#     "constant": False,
#     "inputs": [
#       {
#         "name": "sender",
#         "type": "address"
#       },
#       {
#         "name": "recipient",
#         "type": "address"
#       },
#       {
#         "name": "valueTransferred",
#         "type": "uint256"
#       },
#       {
#         "name": "v",
#         "type": "uint8"
#       },
#       {
#         "name": "r",
#         "type": "bytes32"
#       },
#       {
#         "name": "s",
#         "type": "bytes32"
#       }
#     ],
#     "name": "closeChannel",
#     "outputs": [],
#     "payable": False,
#     "stateMutability": "nonpayable",
#     "type": "function"
#   },
#   {
#     "constant": True,
#     "inputs": [
#       {
#         "name": "sender",
#         "type": "address"
#       },
#       {
#         "name": "recipient",
#         "type": "address"
#       },
#       {
#         "name": "valueTransferred",
#         "type": "uint256"
#       },
#       {
#         "name": "v",
#         "type": "uint8"
#       },
#       {
#         "name": "r",
#         "type": "bytes32"
#       },
#       {
#         "name": "s",
#         "type": "bytes32"
#       }
#     ],
#     "name": "verifySignature",
#     "outputs": [
#       {
#         "name": "",
#         "type": "bool"
#       }
#     ],
#     "payable": False,
#     "stateMutability": "pure",
#     "type": "function"
#   },
#   {
#     "constant": True,
#     "inputs": [
#       {
#         "name": "sender",
#         "type": "address"
#       },
#       {
#         "name": "recipient",
#         "type": "address"
#       }
#     ],
#     "name": "getChannelCollateral",
#     "outputs": [
#       {
#         "name": "",
#         "type": "uint256"
#       }
#     ],
#     "payable": False,
#     "stateMutability": "view",
#     "type": "function"
#   }
# ]
# config['abi'] = a
# #get the contract_instance
# # with open("ABI.json", 'r') as f:
# #     config["abi"] = json.load(f)
# contract_instance = web3.eth.contract(address='0xEb38F414F50750f4A32Dd34ea2405f5CE707D695', abi=config['abi'])



# #local ETH accounts
# proxy = web3.eth.accounts[0]
# user = web3.eth.accounts[1]
# edges = [
#     web3.eth.accounts[2],
#     web3.eth.accounts[3],
#     web3.eth.accounts[4],
#     web3.eth.accounts[5],
#     web3.eth.accounts[6],
#     web3.eth.accounts[7],
#     web3.eth.accounts[8],
#     web3.eth.accounts[9],
# ]

# # the accounts in rinkeby
# accounts = {
#     'user': {s
#         'address': '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1',
#         'pass': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01'
#     },
#     'proxy': {
#         'address': '0xD7397b3894DF7168E7a103508659FC6eC5580F6b',
#         'pass': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'
#     },
#     'edge1': {
#         'address': '0x383B9f270bC983fB7A848B744b8A23eB5eF99699',
#         'pass': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1'
#     },
#     'edge2': {
#         'address': '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149',
#         'pass': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c'
#     },
#     'edge3': {
#         'address': '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761', 
#         'pass': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
#     }

# }

# m = {
#     accounts['user']['address']: 'user',
#     accounts['proxy']['address']: 'proxy',
#     accounts['edge1']['address']: 'edge1',
#     accounts['edge2']['address']: 'edge2',
#     accounts['edge3']['address']: 'edge3',
# }

# # user = accounts['user']['address']
# # proxy = accounts['proxy']['address']
# # edges = [accounts['edge1']['address'], accounts['edge2']['address'], accounts['edge3']['address']]


# rinkeby_private_key = {
#     '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
#     '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
#     '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
#     '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
#     '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
# }

# #the private_key for accounts
# local_private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', user: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}




# depositToken = 10 #the money deposit every time
# user_list = []
# def index(request):
#     """
#     receive the address of edge and open payment channel
#     input: the address of the edge
#     output: open a payment channel for that edge
#     """
#     if request.method == 'POST':
#         #get edge's address
#         address = request.POST.get('address')

#         #store in database
#         models.EdgeInfo.objects.create(address=address, balance=depositToken)

#         #build PC for edge
#         contract_instance.functions.openChannel(address).transact({'from':proxy, 'value':deposit_money*10})
    

#     user_list = models.EdgeInfo.objects.all()

#     #refresh the pages
#     return render(request, 'index.html', {'data': user_list})

# def sendCheck(request):
#     """
#     Receiveing the cheque signed by user and then verify the cheque
#     if the cheque is legal, send the cheque to edge
#     input: the cheque signed by user
#     output: send edge a isometric cheque 
#     """
#     if request.method == 'POST':
#         #get the cheque's information
#         senderAddress = request.POST.get('senderAddress')
#         recipientAddress = request.POST.get('recipientAddress')
#         valueTransferred = int(request.POST.get('valueTransferred'))
#         v = int(request.POST.get('v'))
#         r = request.POST.get('r')
#         s = request.POST.get('s')
#         edge = request.POST.get('usedEdge')
#         # available_edges = request.POST.getlist('availableEdges')
#         # print(available_edges)
#         # edge = random.choice(available_edges)
#         # print(edge)
#         # if contract_instance.functions.getChannelCollateral(proxy, edge).call() == 0:
#         #     requests.post("http://127.0.0.1:8000/regist/", data={'address': edge})
#         #check whether the cheque is valid
#         if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():


#             # close the channel between proxy and edge, used for rinkeby
#             # tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.eth.getTransactionCount(recipientAddress), 'gas':600000})
#             # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[recipientAddress])
#             # web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#             # #signed a new cheque
#             # _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, rinkeby_private_key)


#             contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
#             print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
#             _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, local_private_key)


#             #send to edge
#             r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':recipientAddress, 
#                 'recipientAddress':edge, 'valueTransferred':valueTransferred, 'v':signed_message.v, 'r':to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s)})
#             print(r.status_code)
#             # return HttpResponse("valid transaction!")
#         else:
#             return HttpResponse("Invalid transaction!")

#     return render(request, 'sendCheck.html')

# # def msgcheck(requests):
# #     """
# #     receive the signature from users, if it is from users, then send a cheque to edge
# #     """
# #     if request.method == 'POST':
# #         senderAddress = request.POST.get('address')
# #         signed_message = request.POST.get('signed_message')
# #         v = int(request.POST.get('v'))
# #         r = request.POST.get('r')
# #         s = request.POST.get('s')
# #         if web3.eth.account.recoverHash(information, signature = signed_message.signature) == senderAddress:
# #             #close the channel between proxy and edge
# #             tx = contract_instance.functions.openChannel(proxy).buildTransaction({'value':web3.toWei(2, 'ether'), 'nonce': web3.eth.getTransactionCount(edge3)})
# #             # # # nonce = web3.eth.getTransactionCount(proxy)  
# #             signed_txn = web3.eth.account.signTransaction(tx, private_key=accounts['edge3']['pass'])
# #             web3.eth.sendRawTransaction(signed_txn.rawTransaction)
# #             # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
# #             print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
# #             #signed a new cheque
# #             _, signed_message = sign_transaction(proxy, edge, valueTransferred)

# #             #send to edge
# #             r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':proxy, 
# #                 'recipientAddress':edge, 'valueTransferred':valueTransferred, 'v':signed_message.v, 'r':to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s)})
# #             print(r.status_code)

# def selectEdge(requests):
#     if requests.method == 'POST':
#         edgesWiFi = requests.POST.getlist('edgesWiFi')

#         edge = edgesWiFi[0]
#         #refresh the page
#         data = {
#             'edge': edge
#         }
#         data = json.dumps(data,ensure_ascii=False)
#     return HttpResponse(data, content_type="application/json")
        
#         #choose a edge from edgesWiFi




# def receiveCheck(request):
#     """
#     for edge to receive the cheque and close the PC to get eth
#     input : cheque signed by proxy
#     output : close PC and get eth
#     """
#     if request.method == 'POST':
#         senderAddress = request.POST.get('senderAddress')
#         recipientAddress = request.POST.get('recipientAddress')
#         valueTransferred = int(request.POST.get('valueTransferred'))
#         v = int(request.POST.get('v'))
#         r = request.POST.get('r')
#         s = request.POST.get('s')
#         if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():


#             #close PC to get money for rinkeby
#             # tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.eth.getTransactionCount(recipientAddress), 'gas':600000})
#             # signed_txn = web3.eth.account.signTransaction(tx, private_key=rinkeby_private_key[recipientAddress])
#             # web3.eth.sendRawTransaction(signed_txn.rawTransaction)


#             contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
#             print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)

#         else:
#             return HttpResponse("Invalid transaction!")
#     return render(request, 'edge.html')
        
    


# def sign_transaction(user_address, taker_address, deposit_money, _privatekey):
#     """
#     to sign a cheque
#     input: signer's address, receiver's address, amount
#     output: the hash of the message and the signed message
#     """
#     message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
#     signed_message = web3.eth.account.signHash(message_hash, private_key=_privatekey[user_address])
#     return (message_hash,signed_message)


# def to_32byte_hex(val):
#     """
#     for data type conversion
#     To invoke the solidity's function correctly
#     """
#     return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))


# def get_random_number():
#     """
#     input: None
#     output: return a random integer in 1 - 9
#     """
#     return random.randint(1, 10)
























































#libraries
#django, web3
from django.shortcuts import render
from django.http import HttpResponse
from pricingSystem import models
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import json
import requests
# from django.core import serializers
# from module_name import sign_transaction, to_32byte_hex
import random
import numpy as np
#set up connecntion 
#for test
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
# web3 = Web3((HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")))

#the contract address and abi
# config = { "address"  : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
config = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
# with open("test/ABI.json") as f:
#     config["abi"] = json.load(f)


a = [
    {
    "constant": True,
    "inputs": [
      {
        "name": "",
        "type": "address"
      },
      {
        "name": "",
        "type": "address"
      }
    ],
    "name": "channels",
    "outputs": [
      {
        "name": "sender",
        "type": "address"
      },
      {
        "name": "recipient",
        "type": "address"
      },
      {
        "name": "collateral",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "recipient",
        "type": "address"
      }
    ],
    "name": "openChannel",
    "outputs": [],
    "payable": True,
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "constant": False,
    "inputs": [
      {
        "name": "sender",
        "type": "address"
      },
      {
        "name": "recipient",
        "type": "address"
      },
      {
        "name": "valueTransferred",
        "type": "uint256"
      },
      {
        "name": "v",
        "type": "uint8"
      },
      {
        "name": "r",
        "type": "bytes32"
      },
      {
        "name": "s",
        "type": "bytes32"
      }
    ],
    "name": "closeChannel",
    "outputs": [],
    "payable": False,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "sender",
        "type": "address"
      },
      {
        "name": "recipient",
        "type": "address"
      },
      {
        "name": "valueTransferred",
        "type": "uint256"
      },
      {
        "name": "v",
        "type": "uint8"
      },
      {
        "name": "r",
        "type": "bytes32"
      },
      {
        "name": "s",
        "type": "bytes32"
      }
    ],
    "name": "verifySignature",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": False,
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "constant": True,
    "inputs": [
      {
        "name": "sender",
        "type": "address"
      },
      {
        "name": "recipient",
        "type": "address"
      }
    ],
    "name": "getChannelCollateral",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": False,
    "stateMutability": "view",
    "type": "function"
  }
]
config['abi'] = a
#get the contract_instance
contract_instance = web3.eth.contract(address=config['address'], abi=config['abi'])



#local ETH accounts
# proxy = web3.eth.accounts[0]
# user = web3.eth.accounts[1]
# edges = [
#     web3.eth.accounts[2],
#     web3.eth.accounts[3],
#     web3.eth.accounts[4],
#     web3.eth.accounts[5],
#     web3.eth.accounts[6],
#     web3.eth.accounts[7],
#     web3.eth.accounts[8],
#     web3.eth.accounts[9],
# ]

# the accounts in rinkeby
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

# m = {
#     accounts['user']['address']: 'user',
#     accounts['proxy']['address']: 'proxy',
#     accounts['edge1']['address']: 'edge1',
#     accounts['edge3']['address']: 'edge3',
# }

# user = accounts['user']['address']
# proxy = accounts['proxy']['address']
# edges = [accounts['edge1']['address'], accounts['edge3']['address']]


# rinkeby_private_key = {
#     '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
#     '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
#     '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
#     '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
#     '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
# }

#the private_key for accounts
local_private_key = {user:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', proxy: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}
private_key = {
    user: 'd97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4',
    proxy:'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309',
    edge1:'30341350fd95867002c89d32eb2f7c1b843e8d95310bf3c5b14e5c1ccd6db44b',
    edge2:'e487dc9904ae94719b86d98edb970f82fbfb6c07098f3370c014b53749519ff2',
    edge3:'fce674c91f36e1c52988aa8db06a64fcb7b85f99a42b8171216fae71bd8d40e3'
}




depositToken = 10 #the money deposit every time
user_list = []
def index(request):
    """
    receive the address of edge and open payment channel
    input: the address of the edge
    output: open a payment channel for that edge
    """
    if request.method == 'POST':
        #get edge's address
        address = request.POST.get('address')

        #store in database
        models.EdgeInfo.objects.create(address=address, balance=depositToken)

        #build PC for edge
        tx = contract_instance.functions.openChannel(address).buildTransaction({'value': web3.toWei(1, 'ether') ,'nonce': web3.eth.getTransactionCount(proxy), 'gas':600000})
        signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[proxy])
        a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        transact_hash = web3.toHex(a)
        gas = web3.eth.waitForTransactionReceipt(transact_hash).gasUsed
        print('On regist....')
        print('The recipiet for tx:', transact_hash)
        data = {
            'gas': gas,
        }
        data = json.dumps(data,ensure_ascii=False)
        return HttpResponse(data, content_type="application/json")
    


    #refresh the pages
    else:
      user_list = models.EdgeInfo.objects.all()
      return render(request, 'index.html', {'data': user_list})

def sendCheck(request):
    """
    Receiveing the cheque signed by user and then verify the cheque
    if the cheque is legal, send the cheque to edge
    input: the cheque signed by user
    output: send edge a isometric cheque 
    """
    if request.method == 'POST':
      #get the cheque's information
      senderAddress = request.POST.get('senderAddress')
      recipientAddress = request.POST.get('recipientAddress')
      valueTransferred = int(request.POST.get('valueTransferred'))
      v = int(request.POST.get('v'))
      r = request.POST.get('r')
      s = request.POST.get('s')
      edge = request.POST.get('usedEdge')
      withdraw_pole = request.POST.get('withdraw')
      if withdraw_pole == 'True':
        withdraw_pole = True
      else:
        withdraw_pole = False
      # available_edges = request.POST.getlist('availableEdges')
      # print(available_edges)
      # edge = random.choice(available_edges)
      # print(edge)
      # if contract_instance.functions.getChannelCollateral(proxy, edge).call() == 0:
      #     requests.post("http://127.0.0.1:8000/regist/", data={'address': edge})
      #check whether the cheque is valid
      while not contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():
        pass
      print('On sendCheck....')
      print('The result for transaction', contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call())
      if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call() and withdraw_pole:


        # close the channel between proxy and edge, used for rinkeby
        tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.eth.getTransactionCount(recipientAddress), 'gas':600000, 'chainId':4})
        signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[recipientAddress])
        a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        transact_hash = web3.toHex(a)
        gas = web3.eth.waitForTransactionReceipt(transact_hash).gasUsed
        print('The recipiet for tx:', transact_hash)

        # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
        # print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
        # _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, local_private_key)
        while contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call():
          pass

        #send to edge
        _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, private_key)
        r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':recipientAddress, 
        'recipientAddress':edge, 'valueTransferred': valueTransferred, 'v': signed_message.v, 'r': to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole})
        # print(r.status_code)
        gas2 = json.loads(r.text)['gas']
        data = {
            'gas': gas + gas2,
        }
        data = json.dumps(data,ensure_ascii=False)
        return HttpResponse(data, content_type="application/json")

      else:
        _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, private_key)
        r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':recipientAddress, 
          'recipientAddress':edge, 'valueTransferred': valueTransferred, 'v': signed_message.v, 'r': to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole})
        return HttpResponse('No transaction online!')
        # print(r.status_code)
        # return HttpResponse("valid transaction!")
      # else:
      #   return HttpResponse("Invalid transaction!")
    else:
      return HttpResponse("use POST!")

# def msgcheck(requests):
#     """
#     receive the signature from users, if it is from users, then send a cheque to edge
#     """
#     if request.method == 'POST':
#         senderAddress = request.POST.get('address')
#         signed_message = request.POST.get('signed_message')
#         v = int(request.POST.get('v'))
#         r = request.POST.get('r')
#         s = request.POST.get('s')
#         if web3.eth.account.recoverHash(information, signature = signed_message.signature) == senderAddress:
#             #close the channel between proxy and edge
#             tx = contract_instance.functions.openChannel(proxy).buildTransaction({'value':web3.toWei(2, 'ether'), 'nonce': web3.eth.getTransactionCount(edge3)})
#             # # # nonce = web3.eth.getTransactionCount(proxy)  
#             signed_txn = web3.eth.account.signTransaction(tx, private_key=accounts['edge3']['pass'])
#             web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#             # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
#             print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
#             #signed a new cheque
#             _, signed_message = sign_transaction(proxy, edge, valueTransferred)

#             #send to edge
#             r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':proxy, 
#                 'recipientAddress':edge, 'valueTransferred':valueTransferred, 'v':signed_message.v, 'r':to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s)})
#             print(r.status_code)

def selectEdge(requests):
    if requests.method == 'POST':
        edgesWiFi = requests.POST.getlist('edgesWiFi')
        costForEdges = [np.random.random() for _ in range(5)]
        # costForEdges = [np.random.random() for _ in range(len(edgesWiFi))]
        # min_cost = 1
        # for i in range(len(costForEdges)):
        #   if costForEdges[i] < min_cost:
        #     min_cost = costForEdges[i]
        min_cost = min(costForEdges)
        edge = edgesWiFi[0]
        # edge = edgesWiFi[0]
        #refresh the page
        data = {
            'edge': edge,
            'price': min_cost
        }
        data = json.dumps(data,ensure_ascii=False)
    return HttpResponse(data, content_type="application/json")
        
        #choose a edge from edgesWiFi




def receiveCheck(request):
    """
    for edge to receive the cheque and close the PC to get eth
    input : cheque signed by proxy
    output : close PC and get eth
    """
    if request.method == 'POST':
      senderAddress = request.POST.get('senderAddress')
      recipientAddress = request.POST.get('recipientAddress')
      valueTransferred = int(request.POST.get('valueTransferred'))
      v = int(request.POST.get('v'))
      r = request.POST.get('r')
      s = request.POST.get('s')
      withdraw_pole = request.POST.get('withdraw')
      if withdraw_pole == 'True':
        withdraw_pole = True
      else:
        withdraw_pole = False
      

      print('On receiveCheck....')
      print(contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call())
      while not contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():
        pass
      print(withdraw_pole)
      if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call() and withdraw_pole:


        # close PC to get money for rinkeby
        tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.eth.getTransactionCount(recipientAddress), 'gas':600000, 'chainId':4})
        signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[recipientAddress])
        a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        transact_hash = web3.toHex(a)
        gas = web3.eth.waitForTransactionReceipt(transact_hash).gasUsed
        
        print('The recipiet for tx:', transact_hash)
        while contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call():
          pass
        print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call())
        # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
        # print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
        data = {
            'gas': gas,
        }
        data = json.dumps(data,ensure_ascii=False)
        return HttpResponse(data, content_type="application/json")

      else:
        return HttpResponse("Invalid transaction!")
    else:
      return HttpResponse("use Post!")
        


    


def sign_transaction(user_address, taker_address, deposit_money, _privatekey):
    """
    to sign a cheque
    input: signer's address, receiver's address, amount
    output: the hash of the message and the signed message
    """
    message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
    signed_message = web3.eth.account.signHash(message_hash, private_key=_privatekey[user_address])
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