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

#set up connecntion 
#for test
# web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
web3 = Web3((HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")))

#the contract address and abi
config = { "address"  : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
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
accounts = {
    'user': {
        'address': '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1',
        'pass': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01'
    },
    'proxy': {
        'address': '0xD7397b3894DF7168E7a103508659FC6eC5580F6b',
        'pass': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'
    },
    'edge1': {
        'address': '0x383B9f270bC983fB7A848B744b8A23eB5eF99699',
        'pass': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1'
    },
    'edge2': {
        'address': '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149',
        'pass': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c'
    },
    'edge3': {
        'address': '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761', 
        'pass': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
    }

}

m = {
    accounts['user']['address']: 'user',
    accounts['proxy']['address']: 'proxy',
    accounts['edge1']['address']: 'edge1',
    accounts['edge2']['address']: 'edge2',
    accounts['edge3']['address']: 'edge3',
}

user = accounts['user']['address']
proxy = accounts['proxy']['address']
edges = [accounts['edge1']['address'], accounts['edge2']['address'], accounts['edge3']['address']]


rinkeby_private_key = {
    '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
    '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
    '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
    '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
    '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
}

#the private_key for accounts
local_private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', user: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}




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
        contract_instance.functions.openChannel(address).transact({'from':proxy, 'value':deposit_money*10})
    

    user_list = models.EdgeInfo.objects.all()

    #refresh the pages
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
        # available_edges = request.POST.getlist('availableEdges')
        # print(available_edges)
        # edge = random.choice(available_edges)
        # print(edge)
        # if contract_instance.functions.getChannelCollateral(proxy, edge).call() == 0:
        #     requests.post("http://127.0.0.1:8000/regist/", data={'address': edge})
        #check whether the cheque is valid
        if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():


            # close the channel between proxy and edge, used for rinkeby
            tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.toHex(web3.eth.getTransactionCount(recipientAddress)), web3.toHex('gas':600000), 'chainId':None})
            signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[recipientAddress])
            a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print('The recipiet for tx:', a)


            #signed a new cheque
            _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, rinkeby_private_key)


            # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
            # print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)
            # _, signed_message = sign_transaction(recipientAddress, edge, valueTransferred, local_private_key)


            #send to edge
            r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':recipientAddress, 
                'recipientAddress':edge, 'valueTransferred':valueTransferred, 'v':signed_message.v, 'r':to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s)})
            print(r.status_code)
            # return HttpResponse("valid transaction!")
        else:
            return HttpResponse("Invalid transaction!")

    return render(request, 'sendCheck.html')

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

        edge = edgesWiFi[0]
        #refresh the page
        data = {
            'edge': edge
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
        if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():


            # close PC to get money for rinkeby
            tx = contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).buildTransaction({'nonce': web3.toHex(web3.eth.getTransactionCount(recipientAddress)), 'gas':web3.toHex(600000), 'chainId':None})
            signed_txn = web3.eth.account.signTransaction(tx, private_key=rinkeby_private_key[recipientAddress])
            a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
            print('The recipiet for tx:', a)


            # contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
            # print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)

        else:
            return HttpResponse("Invalid transaction!")
    return render(request, 'edge.html')
        
    


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