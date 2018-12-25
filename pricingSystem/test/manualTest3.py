#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
import numpy as np
# import pywifi
# import sys
# import time
# from pywifi import *
# from pywfi import const
# import cv2
private_key = {
    '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
    '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
    '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
    '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
    '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
}

def snapshot():
    """enable the camera and take a photo"""
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("/image/test.jpeg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()



# def bies():
#     """
#     search for the wifi connection can be made
#     input: None
#     output: the wife can connected by machine
#     """
#     wifi=PyWiFi()#创建一个无限对象
#     ifaces=wifi.interfaces()[0]#取一个无限网卡
#     ifaces.scan() #扫描
#     bessis=ifaces.scan_results()
#     for data in bessis:
#         print(data.ssid)#输出wifi名称
#     return bessis


# def deswifi(wifi_name):
#     """
#     connect with the specific wifi
#     input: the wifi_name want to connect
#     output: the successful connection
#     """
#     wifi=pywifi.PyWifi()#创建一个wifi对象
#     ifaces=wifi.iinterifaces()[0]#取第一个无限网卡
#     print(ifaces.name())#输出无线网卡名称
#     ifaces.disconnect()#断开网卡连接
#     time.sleep(3)#缓冲3秒
  
#     profile=pywifi.profile()#配置文件
#     profile.ssid=wifi_name#wifi名称
#     profile.auth=const.AUTH_ASG_OPEN#需要密码
#     profile.akm.append(const.AKM_TYPE_WPA2SK)#加密类型
#     profile.cipher=const.CIPHER_TYPE_CCMP#加密单元

#     ifaces.remove_all_network_profiles()#删除其他配置文件
#     tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

#     ifaces.connect(tmp_profile)#连接
#     time.sleep(10)#尝试10秒能否成功连接
#     isok=True
#     if ifaces.status()==const.IFACE_CONNECTED:
#     print("成功连接")
#     else:
#     print("失败")
#     ifaces.disconnect()#断开连接
#     time.sleep(1)
#     return isok

    
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
# configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
with open("ABI.json") as f:
    configForRinkeby["abi"] = json.load(f)


#set provider
# web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

#get the contract
contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])

#the private key for accounts

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


# #assume user is moving, and the available edges are not fixed
# num_of_available_edges = random.randint(1, 8)

# #


# #get all available edges
# available_edges = np.random.choice(edges, replace=False, size=num_of_available_edges)
# print(available_edges.tolist())

user = accounts['user']['address']
proxy = accounts['proxy']['address']
edge1 = accounts['edge1']['address']
edge2 = accounts['edge2']['address']
edge3 = accounts['edge3']['address']


edge = edge3



print('-----------------------------------------------------')
#check each account's balance
print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
print("The balance for user before transaction:", web3.eth.getBalance(user))
print("The balance for edge before transaction:", web3.eth.getBalance(edge))
print("The balance for contract before transaction:", web3.eth.getBalance(configForRinkeby['address']))
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())


#user build PC itself
tx = contract_instance.functions.openChannel(proxy).buildTransaction({'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':60000000})
signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print('-----------------------------------------------------')


# check the balance in payment channel
print('The balance for each channel')
print("before transaction:")
print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())


# #get all WIFI connenction
# bessis = bies()

# #select Edge
# edgesWiFi = [node for node in bessis if node.ssid.startswith('JXEdge')]

# data = {'edgesWiFi' : edgesWiFi}
# r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


# #connect to the corresponding wifi
# edge = json.loads(r.text)['edge']
# deswifi(edge)


# #开启摄像头拍摄一个照片
# snapshot()



# #拍摄完照片后调用edge的函数,并把图片传递





#得到结果后，sign一个signature给proxy, proxy签支票给edge
valueTransferred = 1
hashmes, signed_message = sign_transaction(user, proxy, valueTransferred)
#submit the cheque to proxy
data = {'senderAddress':user, 
'recipientAddress':proxy, 'usedEdge':edge,'valueTransferred':valueTransferred, 'v' : signed_message.v, 'r' : to_32byte_hex(signed_message.r), 's' : to_32byte_hex(signed_message.s)}
#user send cheque to proxy
r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)







print()
print("after transaction:")
print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
print('-----------------------------------------------------')
print("The balance for proxy after transaction:", web3.eth.getBalance(proxy))
print("The balance for user after transaction:", web3.eth.getBalance(user))
print("The balance for edge after transaction:", web3.eth.getBalance(edge))



