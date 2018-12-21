#libraries
#django, web3
from django.shortcuts import render
from django.http import HttpResponse
from pricingSystem import models
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
import json
import requests


# from module_name import sign_transaction, to_32byte_hex
import random

#the contract address and abi
config = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
with open("/Users/a931759898/Desktop/test/1.json") as f:
    config["abi"] = json.load(f)



#set up connecntion
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
# web3 = Web3((HTTPProvider("https://rinkeby.etherscan.io")))


#local ETH accounts
proxy = web3.eth.accounts[0]
user = web3.eth.accounts[1]
edge = web3.eth.accounts[2]




#the private_key for accounts
private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', user: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}

#get the contract_instance
contract_instance = web3.eth.contract(address=config["address"], abi=config['abi'])




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
        available_edges = request.POST.getlist('availableEdges')
        print(available_edges)
        edge = random.choice(available_edges)
        print(edge)
        # if contract_instance.functions.getChannelCollateral(proxy, edge).call() == 0:
        #     requests.post("http://127.0.0.1:8000/regist/", data={'address': edge})
        #check whether the cheque is valid
        if contract_instance.functions.verifySignature(senderAddress, recipientAddress, valueTransferred, v, r, s).call():
            #close the channel between proxy and edge
            contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
            print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)

            #signed a new cheque
            _, signed_message = sign_transaction(proxy, edge, valueTransferred)

            #send to edge
            r = requests.post("http://127.0.0.1:8000/edge/", data = {'senderAddress':proxy, 
                'recipientAddress':edge, 'valueTransferred':valueTransferred, 'v':signed_message.v, 'r':to_32byte_hex(signed_message.r), 's':to_32byte_hex(signed_message.s)})
            print(r.status_code)
        else:
            return HttpResponse("Invalid transaction!")

    #refresh the page
    data = {
        'edge': edge
    }
    return HttpResponse(json.dumps(data, content_type="application/json"))
    # return render(request, 'sendCheck.html')





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
            #close PC to get money
            contract_instance.functions.closeChannel(senderAddress, recipientAddress, valueTransferred, v, r, s).transact({'from':recipientAddress})
            print(contract_instance.functions.getChannelCollateral(senderAddress, recipientAddress).call() == 0)

        else:
            return HttpResponse("Invalid transaction!")
    return render(request, 'edge.html')
        
    


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