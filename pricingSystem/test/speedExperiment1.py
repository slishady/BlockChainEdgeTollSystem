# #designed for check the improvement in transaction speed

# #library
# from web3 import Web3, HTTPProvider
# import json
# import requests
# import pywifi
# from pywifi import *
# from pywifi import const
# import cv2
# import base64
# from utils import utils
# import time
# import numpy as np
# target_times = 100
# factor = 1000000000
# def sign_transaction(user_address, taker_address, deposit_money):
#     """
#     to sign a cheque
#     input: signer's address, receiver's address, amount
#     output: the hash of the message and the signed message
#     """
#     message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
#     signed_message = web3.eth.account.signHash(message_hash, private_key=private_key[user_address])
#     return (message_hash,signed_message)



# # def send_task():
# #     with open('image/test2.jpeg', 'rb') as imageFile:
# #         image2str = base64.b64encode(imageFile.read())
# #     a = image2str.decode('ascii')
# #     r = requests.post('http://192.168.0.172:8099/detect', json = {'image': a})
# #     return r


# # def snapshot():
# #     """enable the camera and take a photo"""
# #     cap = cv2.VideoCapture(0)
# #     while(1):
# #         # get a frame
# #         ret, frame = cap.read()
# #         # show a frame
# #         cv2.imshow("capture", frame)
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             cv2.imwrite("/image/test.jpeg", frame)
# #             break
# #     cap.release()
# #     cv2.destroyAllWindows()



# # def bies():
# #     """
# #     search for the wifi connection can be made
# #     input: None
# #     output: the wife can connected by machine
# #     """
# #     wifi=PyWiFi()#创建一个无限对象
# #     ifaces=wifi.interfaces()[0]#取一个无限网卡
# #     ifaces.scan() #扫描
# #     bessis=ifaces.scan_results()
# #     for data in bessis:
# #         print(data.ssid)#输出wifi名称
# #     return bessis


# # def connect(network_name, passwordstr):
# #     """

# #     """
# #     wifi=pywifi.PyWiFi()#初始化
# #     ifaces=wifi.interfaces()[0]#创建取出第一个无限网卡
# #     #print(ifaces.name())#输出无限网卡名
# #     ifaces.disconnect()#断开无限网卡连接
# #     time.sleep(3)#断开以后缓冲3秒

# #     profile=pywifi.Profile()#配置文件
# #     profile.ssid=network_name#wifi名称
# #     profile.auth=const.AUTH_ALG_OPEN#需要密码连接
# #     profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密
# #     profile.cipher=const.CIPHER_TYPE_CCMP#机密单元
# #     profile.key=passwordstr #wifi密钥

# #     ifaces.remove_all_network_profiles()#删除其他所有配置文件
# #     tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

# #     ifaces.connect(tmp_profile)#连接
# #     time.sleep(15)#10秒内能否连接上
# #     isok = True
# #     if ifaces.status()==const.IFACE_CONNECTED:
# #         print("连接成功")
# #     else:
# #         print("连接失败")

# #         ifaces.disconnect()#断开连接
# #         time.sleep(1)

# #     return isok

    
# # # from utils import sign_transaction, to_32byte_hex

# # def sign_transaction(user_address, taker_address, deposit_money):
# #     """
# #     to sign a cheque
# #     input: signer's address, receiver's address, amount
# #     output: the hash of the message and the signed message
# #     """
# #     message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
# #     signed_message = web3.eth.account.signHash(message_hash, private_key=private_key[user_address])
# #     return (message_hash,signed_message)


# # def to_32byte_hex(val):
# #     """
# #     for data type conversion
# #     To invoke the solidity's function correctly
# #     """
# #     return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))


# # def get_random_number():
# #     """
# #     input: None
# #     output: return a random integer in 1 - 9
# #     """
# #     return random.randint(1, 10)








# #get contract's address and abi
# # configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
# configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
# with open("ABI.json") as f:
#     configForRinkeby["abi"] = json.load(f)


# #set provider
# # web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
# web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

# #get the contract
# contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])

# #the private key for accounts

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


# edge = edge3


# edge_address = {
#     '1' : edge,
#     'TP-LINK_4423': edge
# }

# password_map = {
#     '1' : '20690539',
#     'TP-LINK_4423':'jiangxing123'
# }


# for num_of_tasks in range(10, target_times+1):
#     print('#%i' %num_of_tasks)
#         #get contract's address and abi
#     # configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
#     configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
#     with open("ABI.json") as f:
#         configForRinkeby["abi"] = json.load(f)


#     #set provider
#     # web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
#     web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

#     #get the contract
#     contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])

#     #the private key for accounts

#     accounts = {
#         'proxy': {
#             'address': '0xD7397b3894DF7168E7a103508659FC6eC5580F6b',
#             'pass': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc'
#         },
#         'edge1': {
#             'address': '0x383B9f270bC983fB7A848B744b8A23eB5eF99699',
#             'pass': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1'
#         },
#         'user': {
#             'address': '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149',
#             'pass': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c'
#         },
#         'edge3': {
#             'address': '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761', 
#             'pass': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
#         }
#     }

#     private_key = {
#         '0x78FCd70C3615f66AB0cCF2c10fffCC644Ad0C9b1': '2696b52850e466f01f0bbd0c0a1dbf62ce0698dd6c7f21f5fe916f6bb60baa01',
#         '0xD7397b3894DF7168E7a103508659FC6eC5580F6b': '24b89be74328404b533e15821ffbaaa95682e1bec49120bc5ec7d9e78c4eb5cc',
#         '0x383B9f270bC983fB7A848B744b8A23eB5eF99699': '6a80e963028eab8fe909faba2e6e9ddd9ecf97858a710692e89b62ee24bfbfe1',
#         '0x3B67e9a0cCc44d74Fe09F7816978b846215bF149': 'a40c701d7557dbcdc3eacf51b794b10d65a8c9d7cb3dc4277e623a1d82142c2c',
#         '0x3D8e54A9bA85FF7848aa3D1929e520BcdBbe8761': '0e308916509918a76d1f2e7973904380378d06691b8507ed9a67027fc9d2ebc0'
#     }

#     user = accounts['user']['address']
#     proxy = accounts['proxy']['address']
#     edge1 = accounts['edge1']['address']
#     edge3 = accounts['edge3']['address']


#     edge = edge3


#     edge_address = {
#         '1' : edge,
#         'TP-LINK_4423': edge
#     }

#     password_map = {
#         '1' : '20690539',
#         'TP-LINK_4423':'jiangxing123'
#     }

#     # num_of_tasks = target_times
#     print('-----------------------------------------------------')
#     #check each account's balance
#     print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
#     print("The balance for user before transaction:", web3.eth.getBalance(user))
#     print("The balance for contract before transaction:", web3.eth.getBalance(configForRinkeby['address']))
#     print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
#     total_gas = 0

#     begin = time.time()
#     #each edge register first:
#     r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})
#     total_gas += json.loads(r.text)['gas']

#     #user build PC itself
#     tx = contract_instance.functions.openChannel(proxy).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
#     signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
#     a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#     transaction_hash = web3.toHex(a)
#     gas = web3.eth.waitForTransactionReceipt(transaction_hash).gasUsed
#     total_gas += gas
#     print('-----------------------------------------------------')

#     # check the balance in payment channel
#     print('The balance for each channel')
#     print("before transaction:")
#     print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
#     print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
#     valueTransferred = 1
#     money_saved = 0
#     withdraw_pole = False
#     total_valueTransferred = 0
#     #the payment channel one:
#     for task_index in range(1, num_of_tasks+1):
#         if num_of_tasks == task_index:
#             withdraw_pole = True
#         #get all WIFI connenction
#         bessis = utils.bies()

#         #select Edge
#         edgesWiFi = [node.ssid for node in bessis if node.ssid in 'TP-LINK_4423']

#         data = {'edgesWiFi' : edgesWiFi}
#         r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)
#         print(r.text)


#         #connect to the corresponding wifi
#         edge = json.loads(r.text)['edge']
#         utils.connect(edge, password_map[edge])
#         money_saved += (1 - json.loads(r.text)['price'])
#         amount = json.loads(r.text)['price']

#         #开启摄像头拍摄一个照片
#         # utils.snapshot()



#         #拍摄完照片后调用edge的函数,并把图片传递
#         r = utils.send_task()
#         print('The task, ', r.status_code)





#         valueTransferred = int(amount*1000)
#         total_valueTransferred += valueTransferred
#         if withdraw_pole:
#             valueTransferred = total_valueTransferred
#         #得到结果后，sign一个signature给proxy, proxy签支票给edge
#         hashmes, signed_message = sign_transaction(user, proxy, valueTransferred)
#         #submit the cheque to proxy
#         data = {'senderAddress':user, 
#         'recipientAddress':proxy, 'usedEdge':edge_address[edge], 'valueTransferred' : valueTransferred, 'v' : signed_message.v, 
#         'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
#         #user send cheque to proxy
#         r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)
#         if withdraw_pole == True:

#             total_gas += json.loads(r.text)['gas']
#         # valueTransferred += 1
#         print('tx%i finished' % task_index)
#     end = time.time()
#     time_cost = end - begin
#     print(time_cost)
#     print(total_gas)
#     new_time_cost = time_cost
#     with open('data11.txt', 'a') as f:
#         f.write('#%i\n' %num_of_tasks)
#         f.write('%i, '% new_time_cost)
#         f.write('%i, '% total_gas)
#         f.write('%f'% money_saved)
#         f.write('\n')





















#     begin = time.time()
#     #each edge register first:
#     # r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})

#     #user build PC itself

#     print('-----------------------------------------------------')


#     # check the balance in payment channel
#     print('The balance for each channel')
#     print("before transaction:")
#     print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge3).call())
#     print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
#     valueTransferred = 1

#     # num_of_tasks = 8
#     withdraw_pole = True
#     total_gas = 0
#     money_saved = 0
#     total_valueTransferred = 0
#     #the slow one:
#     target_times = 50
#     for task_index in range(1, num_of_tasks+1):

#         # tx = contract_instance.functions.openChannel(edge3).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
#         # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
#         # web3.eth.sendRawTransaction(signed_txn.rawTransaction)

#         # while not (contract_instance.functions.getChannelCollateral(user, edge3).call()):
#         #     pass
#         #get all WIFI connenction
#         bessis = utils.bies()

#         #select Edge
#         edgesWiFi = [node.ssid for node in bessis if node.ssid in ['TP-LINK_4423', 'TP-LINK_00F8', 'TP-LINK_E65B']]

#         data = {'edgesWiFi' : edgesWiFi}
#         r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


#         #connect to the corresponding wifi
#         edge = json.loads(r.text)['edge']
#         edge = edgesWiFi[0]
#         utils.connect(edge, password_map[edge])
#         money_saved += (1 - np.random.random())


#         #开启摄像头拍摄一个照片
#         # utils.snapshot()



#         #拍摄完照片后调用edge的函数,并把图片传递
#         r = utils.send_task()
#         print('The task, ', r.status_code)





#         valueTransferred = int(np.random.random()*1000)
#         #得到结果后，sign一个signature给proxy, proxy签支票给edge
#         hashmes, signed_message = sign_transaction(user, edge_address[edge], valueTransferred)
#         # if num_of_tasks == 5:
#         withdraw_pole = True
#         #submit the cheque to proxy
#         # data = {'senderAddress':user, 
#         # 'recipientAddress':edge_address[edge], 'valueTransferred' : valueTransferred, 'v' : signed_message.v, 
#         # 'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
#         # #user send cheque to proxy
#         # r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)
#         tx = contract_instance.functions.openChannel(edge_address[edge]).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
#         signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
#         a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#         transact_hash = web3.toHex(a)   
#         gas = web3.eth.waitForTransactionReceipt(transact_hash).gasUsed
#         total_gas += gas
#         # valueTransferred += 1

#         #edge withdraw

#         # contract_instance.functions.closeChannel(user, edge_address[edge], valueTransferred, signed_message.v, utils.to_32byte_hex(signed_message.r), utils.to_32byte_hex(signed_message.s)).buildTransaction({'from': edge_address[edge], 'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
#         # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[edge_address[edge]])
#         # web3.eth.sendRawTransaction(signed_txn.rawTransaction)
#         # while contract_instance.functions.getChannelCollateral(user, edge).call():
#         #     pass
#         #submit the cheque to proxy
#         withdraw_pole = True
#         data = {'senderAddress':user, 
#         'recipientAddress':edge_address[edge],'valueTransferred':valueTransferred, 
#         'v' : signed_message.v, 'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
#         print("posting to receive cheque.....")
#         r = requests.post("http://127.0.0.1:8000/edge/", data=data)
#         total_gas += json.loads(r.text)['gas']
#         print('tx%i finished' % task_index)
#     end2 = time.time()
#     time_cost2 = end2 - begin
#     print(time_cost2)
#     print(total_gas)
#     with open('data12.txt', 'a') as f:
#         f.write('#%i\n' %num_of_tasks)
#         f.write('%i, '% time_cost2)
#         f.write('%i, '% total_gas)
#         f.write('%f' % money_saved)
#         f.write('\n')




#     print()
#     print("after transaction:")
#     print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge_address[edge]).call())
#     print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
#     print('-----------------------------------------------------')
#     print("The balance for proxy after transaction:", web3.eth.getBalance(proxy))
#     print("The balance for user after transaction:", web3.eth.getBalance(user))
#     print("The balance for edge after transaction:", web3.eth.getBalance(edge_address[edge]))
















#designed for check the improvement in transaction speed

#library
from web3 import Web3, HTTPProvider
import json
import requests
import pywifi
from pywifi import *
from pywifi import const
import cv2
import base64
from utils import utils
import time
import numpy as np
target_times = 100
factor = 1000000000
def sign_transaction(user_address, taker_address, deposit_money):
    """
    to sign a cheque
    input: signer's address, receiver's address, amount
    output: the hash of the message and the signed message
    """
    message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
    signed_message = web3.eth.account.signHash(message_hash, private_key=private_key[user_address])
    return (message_hash,signed_message)



# def send_task():
#     with open('image/test2.jpeg', 'rb') as imageFile:
#         image2str = base64.b64encode(imageFile.read())
#     a = image2str.decode('ascii')
#     r = requests.post('http://192.168.0.172:8099/detect', json = {'image': a})
#     return r


# def snapshot():
#     """enable the camera and take a photo"""
#     cap = cv2.VideoCapture(0)
#     while(1):
#         # get a frame
#         ret, frame = cap.read()
#         # show a frame
#         cv2.imshow("capture", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             cv2.imwrite("/image/test.jpeg", frame)
#             break
#     cap.release()
#     cv2.destroyAllWindows()



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


# def connect(network_name, passwordstr):
#     """

#     """
#     wifi=pywifi.PyWiFi()#初始化
#     ifaces=wifi.interfaces()[0]#创建取出第一个无限网卡
#     #print(ifaces.name())#输出无限网卡名
#     ifaces.disconnect()#断开无限网卡连接
#     time.sleep(3)#断开以后缓冲3秒

#     profile=pywifi.Profile()#配置文件
#     profile.ssid=network_name#wifi名称
#     profile.auth=const.AUTH_ALG_OPEN#需要密码连接
#     profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi加密
#     profile.cipher=const.CIPHER_TYPE_CCMP#机密单元
#     profile.key=passwordstr #wifi密钥

#     ifaces.remove_all_network_profiles()#删除其他所有配置文件
#     tmp_profile=ifaces.add_network_profile(profile)#加载配置文件

#     ifaces.connect(tmp_profile)#连接
#     time.sleep(15)#10秒内能否连接上
#     isok = True
#     if ifaces.status()==const.IFACE_CONNECTED:
#         print("连接成功")
#     else:
#         print("连接失败")

#         ifaces.disconnect()#断开连接
#         time.sleep(1)

#     return isok

    
# # from utils import sign_transaction, to_32byte_hex

# def sign_transaction(user_address, taker_address, deposit_money):
#     """
#     to sign a cheque
#     input: signer's address, receiver's address, amount
#     output: the hash of the message and the signed message
#     """
#     message_hash = web3.soliditySha3(['address', 'address', 'uint256'], [user_address, taker_address, deposit_money])
#     signed_message = web3.eth.account.signHash(message_hash, private_key=private_key[user_address])
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








#get contract's address and abi
configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
# configForRinkeby = { "address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
with open("ABI.json") as f:
    configForlocal["abi"] = json.load(f)


#set provider
web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
# web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

#get the contract
contract_instance = web3.eth.contract(address=configForlocal["address"], abi=configForlocal['abi'])

#the private key for accounts

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


num_lists = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
for num_of_tasks in range(10, target_times+1):
    if num_of_tasks not in num_lists:
        continue
    print('#%i' %num_of_tasks)
        #get contract's address and abi
    # configForlocal = { "address"  : "0x6a814a5848C10423AF50047c85c7896EEB31675c"}
    # configForRinkeby = {"address" : "0xb18C59EdeC97517AE53b8d0319d7dAEE29cE5FF3"}
    # with open("ABI.json") as f:
    #     configForRinkeby["abi"] = json.load(f)


    # #set provider
    # web3 = Web3(HTTPProvider("http://127.0.0.1:7545")) #connect to local network
    # # web3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/5590c756ce4d47269bcc0a2d462f8215")) #connect to the rinkeby network

    # #get the contract
    # contract_instance = web3.eth.contract(address=configForRinkeby["address"], abi=configForRinkeby['abi'])

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
    edge_address = {
        '1' : edge,
        'TP-LINK_4423': edge
    }

    password_map = {
        '1' : '20690539',
        'TP-LINK_4423':'jiangxing123'
    }

    # num_of_tasks = target_times
    print('-----------------------------------------------------')
    #check each account's balance
    print("The balance for proxy before transaction:", web3.eth.getBalance(proxy))
    print("The balance for user before transaction:", web3.eth.getBalance(user))
    print("The balance for contract before transaction:", web3.eth.getBalance(configForlocal['address']))
    print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
    total_gas = 0

    begin = time.time()
    #each edge register first:
    r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})
    total_gas += json.loads(r.text)['gas']

    #user build PC itself
    tx = contract_instance.functions.openChannel(proxy).buildTransaction({'from': user,'value':web3.toWei(1, 'ether')})
    signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
    a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    transaction_hash = web3.toHex(a)
    gas = web3.eth.waitForTransactionReceipt(transaction_hash).gasUsed
    total_gas += gas
    print('-----------------------------------------------------')

    # check the balance in payment channel
    print('The balance for each channel')
    print("before transaction:")
    print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge).call())
    print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
    valueTransferred = 1
    money_saved = 0
    withdraw_pole = False
    total_valueTransferred = 0
    #the payment channel one:
    for task_index in range(1, num_of_tasks+1):
        if num_of_tasks == task_index:
            withdraw_pole = True
        #get all WIFI connenction
        bessis = utils.bies()

        #select Edge
        edgesWiFi = [node.ssid for node in bessis if node.ssid in 'TP-LINK_4423']

        data = {'edgesWiFi' : edgesWiFi}
        r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)
        print(r.text)


        #connect to the corresponding wifi
        edge = json.loads(r.text)['edge']
        utils.connect(edge, password_map[edge])
        money_saved += (1 - json.loads(r.text)['price'])
        amount = json.loads(r.text)['price']

        #开启摄像头拍摄一个照片
        # utils.snapshot()



        #拍摄完照片后调用edge的函数,并把图片传递
        r = utils.send_task()
        print('The task, ', r.status_code)





        valueTransferred = int(amount*1000)
        total_valueTransferred += valueTransferred
        if withdraw_pole:
            valueTransferred = total_valueTransferred
        #得到结果后，sign一个signature给proxy, proxy签支票给edge
        hashmes, signed_message = sign_transaction(user, proxy, valueTransferred)
        #submit the cheque to proxy
        data = {'senderAddress':user, 
        'recipientAddress':proxy, 'usedEdge':edge_address[edge], 'valueTransferred' : valueTransferred, 'v' : signed_message.v, 
        'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
        #user send cheque to proxy
        r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)
        if withdraw_pole == True:
            total_gas += json.loads(r.text)['gas']
        # valueTransferred += 1
        print('tx%i finished' % task_index)
    end = time.time()
    time_cost = end - begin
    print(time_cost)
    print(total_gas)
    new_time_cost = time_cost
    with open('truffle-data.txt', 'a') as f:
        f.write('#%i\n' %num_of_tasks)
        f.write('%i, '% new_time_cost)
        f.write('%i, '% total_gas)
        f.write('%f'% money_saved)
        f.write('\n')





















    begin = time.time()
    #each edge register first:
    # r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})

    #user build PC itself

    print('-----------------------------------------------------')


    # check the balance in payment channel
    print('The balance for each channel')
    print("before transaction:")
    print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge3).call())
    print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
    valueTransferred = 1

    # num_of_tasks = 8
    withdraw_pole = True
    total_gas = 0
    money_saved = 0
    total_valueTransferred = 0
    #the slow one:
    target_times = 50
    for task_index in range(1, num_of_tasks+1):

        # tx = contract_instance.functions.openChannel(edge3).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
        # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
        # web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        # while not (contract_instance.functions.getChannelCollateral(user, edge3).call()):
        #     pass
        #get all WIFI connenction
        bessis = utils.bies()

        #select Edge
        edgesWiFi = [node.ssid for node in bessis if node.ssid in ['TP-LINK_4423', 'TP-LINK_00F8', 'TP-LINK_E65B']]

        data = {'edgesWiFi' : edgesWiFi}
        r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


        #connect to the corresponding wifi
        edge = json.loads(r.text)['edge']
        edge = edgesWiFi[0]
        utils.connect(edge, password_map[edge])
        money_saved += (1 - np.random.random())


        #开启摄像头拍摄一个照片
        # utils.snapshot()



        #拍摄完照片后调用edge的函数,并把图片传递
        r = utils.send_task()
        print('The task, ', r.status_code)





        valueTransferred = int(np.random.random()*1000)
        #得到结果后，sign一个signature给proxy, proxy签支票给edge
        hashmes, signed_message = sign_transaction(user, edge_address[edge], valueTransferred)
        # if num_of_tasks == 5:
        withdraw_pole = True
        #submit the cheque to proxy
        # data = {'senderAddress':user, 
        # 'recipientAddress':edge_address[edge], 'valueTransferred' : valueTransferred, 'v' : signed_message.v, 
        # 'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
        # #user send cheque to proxy
        # r = requests.post("http://127.0.0.1:8000/sendCheck/", data=data)
        tx = contract_instance.functions.openChannel(edge_address[edge]).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
        signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
        a = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        transact_hash = web3.toHex(a)   
        gas = web3.eth.waitForTransactionReceipt(transact_hash).gasUsed
        total_gas += gas
        # valueTransferred += 1

        #edge withdraw

        # contract_instance.functions.closeChannel(user, edge_address[edge], valueTransferred, signed_message.v, utils.to_32byte_hex(signed_message.r), utils.to_32byte_hex(signed_message.s)).buildTransaction({'from': edge_address[edge], 'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
        # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[edge_address[edge]])
        # web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        # while contract_instance.functions.getChannelCollateral(user, edge).call():
        #     pass
        #submit the cheque to proxy
        withdraw_pole = True
        data = {'senderAddress':user, 
        'recipientAddress':edge_address[edge],'valueTransferred':valueTransferred, 
        'v' : signed_message.v, 'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}
        print("posting to receive cheque.....")
        r = requests.post("http://127.0.0.1:8000/edge/", data=data)
        total_gas += json.loads(r.text)['gas']
        print('tx%i finished' % task_index)
    end2 = time.time()
    time_cost2 = end2 - begin
    print(time_cost2)
    print(total_gas)
    with open('data12.txt', 'a') as f:
        f.write('#%i\n' %num_of_tasks)
        f.write('%i, '% time_cost2)
        f.write('%i, '% total_gas)
        f.write('%f' % money_saved)
        f.write('\n')




    print()
    print("after transaction:")
    print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge_address[edge]).call())
    print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
    print('-----------------------------------------------------')
    print("The balance for proxy after transaction:", web3.eth.getBalance(proxy))
    print("The balance for user after transaction:", web3.eth.getBalance(user))
    print("The balance for edge after transaction:", web3.eth.getBalance(edge_address[edge]))







