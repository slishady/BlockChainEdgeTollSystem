import random
from web3 import Web3
#library
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from eth_account.messages import defunct_hash_message
import json
import requests
import random
import numpy as np
import pywifi
import sys
import time
from pywifi import *
from pywifi import const
import cv2
import base64

web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215"))
def connect(network_name, passwordstr):
    """

    """
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
    # for data in bessis:
    #     print(data.ssid)#输出wifi名称
    return bessis


def snapshot():
    """enable the camera and take a photo"""
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("../image/test.jpeg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()


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



def send_task():
    with open('image/1.jpeg', 'rb') as imageFile:
        image2str = base64.b64encode(imageFile.read())
    a = image2str.decode('ascii')
    r = requests.post('http://faceai.jiangxingai.com:8099/detect', json = {'image': a})
    return r