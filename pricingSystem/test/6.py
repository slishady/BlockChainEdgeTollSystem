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

print(web3.net.chainId)