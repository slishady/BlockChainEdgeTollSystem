# -*- coding: UTF-8 -*-
#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
# import numpy as np
import pywifi
import sys
import time
from pywifi import *
from pywifi import const
import cv2
import base64

def send_task():
    """
    send image to server and receive result
    """
    with open('image/test2.jpeg', 'rb') as imageFile:
        image2str = base64.b64encode(imageFile.read())
    a = image2str.decode('ascii')
    r = requests.post('http://192.168.0.172:8099/detect', json = {'image': a})
    return r

def snapshot():
    """
    enable the camera and take a photo
    """
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



def bies():
    """
    search for the wifi connection can be made
    input: None
    output: the wife can connected by machine
    """
    wifi=PyWiFi()#创建一个无限对象
    ifaces=wifi.interfaces()[0]#取一个无限网卡
    ifaces.scan() #扫描
    bessis=ifaces.scan_results()
    for data in bessis:
        print(data.ssid)#输出wifi名称
    return bessis


def connect(network_name, passwordstr):
    wifi=pywifi.PyWiFi()#初始化
    ifaces=wifi.interfaces()[0]#创建取出第一个无限网卡
    #print(ifaces.name())#输出无限网卡名
    ifaces.disconnect()#断开无限网卡连接
    time.sleep(3)#断开以后缓冲3秒

    profile=pywifi.Profile()#配置文件
    profile.ssid=network_name#wifi名称
    profile.auth=const.AUTH_ALG_OPEN#需要密码连接
    profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密
    profile.cipher=const.CIPHER_TYPE_CCMP#机密单元
    profile.key=passwordstr #wifi密钥

    ifaces.remove_all_network_profiles()#删除其他所有配置文件
    tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

    ifaces.connect(tmp_profile)#连接
    time.sleep(15)#10秒内能否连接上
    isok = True
    if ifaces.status()==const.IFACE_CONNECTED:
        print("连接成功")
    else:
        print("连接失败")

        ifaces.disconnect()#断开连接
        time.sleep(1)

    return isok

    
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
configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
with open("ABI.json", 'r') as f:
    configForlocal["abi"] = json.load(f)



#set provider
web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))


#the proxy for trainsiting the money
proxy = web3.eth.accounts[0]


#the sender
user = web3.eth.accounts[1]


#the receiver
edge = web3.eth.accounts[2]

#get the contract
contract_instance = web3.eth.contract(address='0xEb38F414F50750f4A32Dd34ea2405f5CE707D695', abi=configForlocal['abi'])

#the private key for accounts
# private_key = {proxy:'d97979f3ba6851531ec59f2beca5a6956f96e742d3b433484f210fdf26cfbda4', user: 'a08e5a235d53bf82413e7b38e256a7bd1ef684b766d26dc831eb766016090309'}
private_key = {proxy:'93eeceaf872686b748acda18ba68acd4c13d2b786203edee237bee8017a79105', user: '57730ecf94645a7cbeb381164e8577e1122f6e909f2b46dd839480b8916a4fc2'}


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

edge_address = {
    '1' : edges[0],
    'TP-LINK_4423': edges[0],
}

password_map = {
    '1' : '20690539',
    'TP-LINK_4423':'jiangxing123'
}

#assume user is moving, and the available edges are not fixed
# num_of_available_edges = random.randint(1, 8)

# #get all available edges
# available_edges = np.random.choice(edges, replace=False, size=num_of_available_edges)
# print(available_edges.tolist())


print('-----------------------------------------------------')
#check each account's balance
print('The transaction begin.....')
print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
print("The balance for user before transaction:", web3.eth.getBalance(user))



#user build PC itself
print('-----------------------------------------------------')
print('user begin to build PC for proxt...')
contract_instance.functions.openChannel(proxy).transact({'from':user, 'value':10, 'gas':600000})
print('the balance for channel in user and proxy:', contract_instance.functions.getChannelCollateral(user,proxy).call())
print('-----------------------------------------------------')


# check the balance in payment channel
# print('The balance for each channel')
# print("before transaction:")
# print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
print('The wifi can be connected:')
#get all WIFI connenction
bessis = bies()

#select Edge
edgesWiFi = [node.ssid for node in bessis if node.ssid == 'TP-LINK_4423']
print('-----------------------------------------------------')
print('send available wifis to proxy and connect one....')
data = {'edgesWiFi' : edgesWiFi}
r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


#connect to the corresponding wifi
edge = json.loads(r.text)['edge']
print('the selected wifi name:', edge)
print('connect to edge.....')
connect(edge, password_map[edge])

#开启摄像头拍摄一个照片
print('-----------------------------------------------------')
print('open camera and take photos......')
snapshot()


#拍摄完照片后调用edge的函数,并把图片传递
print('send pictures(tasks) to edge....')
r = send_task()
if (r.status_code == 200):
    print("user's task finished!")
else:
    print("user's task not finished!")




#user sign transaction, cost 5 coin
print('-----------------------------------------------------')
print('user begin to pay money.....')
valueTransferred = 5
hashmes, signed_message = sign_transaction(user, proxy, valueTransferred)
#submit the cheque to proxy
data = {'senderAddress':user, 
'recipientAddress':proxy, 'usedEdge': edge_address[edge], 'valueTransferred':valueTransferred, 'v' : signed_message.v, 'r' : to_32byte_hex(signed_message.r), 's' : to_32byte_hex(signed_message.s)}
r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)
print('Done! the whole transaction finished!')
print('-----------------------------------------------------')

#log out the transaction detail
print()
print("after transaction:")
# print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge_address[edge]).call())
# print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
print('-----------------------------------------------------')
print("The balance for proxy after transaction:", web3.eth.getBalance(proxy))
print("The balance for user after transaction:", web3.eth.getBalance(user))
print("The balance for edge after transaction:", web3.eth.getBalance(edge_address[edge]))



