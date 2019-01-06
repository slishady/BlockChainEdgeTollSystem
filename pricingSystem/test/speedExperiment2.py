begin = time.time()
#each edge register first:
r = requests.post('http://127.0.0.1:8000/regist/', data={'address':edge3})

#user build PC itself
tx = contract_instance.functions.openChannel(proxy).buildTransaction({'from': user,'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[user])
web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print('-----------------------------------------------------')


# check the balance in payment channel
print('The balance for each channel')
print("before transaction:")
print("channel in proxy and edge", contract_instance.functions.getChannelCollateral(proxy, edge3).call())
print("channel in user and proxy", contract_instance.functions.getChannelCollateral(user, proxy).call())
valueTransferred = 1

num_of_tasks = 5
withdraw_pole = False

#the slow one:
for task_index in range(1, num_of_tasks+1):
    #get all WIFI connenction
    bessis = utils.bies()

    #select Edge
    edgesWiFi = [node.ssid for node in bessis if node.ssid == 'TP-LINK_4423']

    data = {'edgesWiFi' : edgesWiFi}
    r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


    #connect to the corresponding wifi
    edge = json.loads(r.text)['edge']
    edge = edgesWiFi[0]
    utils.connect(edge, password_map[edge])


    #开启摄像头拍摄一个照片
    # utils.snapshot()



    #拍摄完照片后调用edge的函数,并把图片传递
    r = utils.send_task()
    print('The task, ', r.status_code)






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
    web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    # valueTransferred += 1

    #edge withdraw

    # contract_instance.functions.closeChannel(user, edge_address[edge], valueTransferred, signed_message.v, utils.to_32byte_hex(signed_message.r), utils.to_32byte_hex(signed_message.s)).buildTransaction({'from': edge_address[edge], 'value':web3.toWei(1, 'ether'), 'nonce': web3.eth.getTransactionCount(user), 'gas':600000, 'chainId':4})
    # signed_txn = web3.eth.account.signTransaction(tx, private_key=private_key[edge_address[edge]])
    # web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    # while contract_instance.functions.getChannelCollateral(user, edge).call():
    #     pass
    #submit the cheque to proxy
    data = {'senderAddress':user, 
    'recipientAddress':edge_address[edge],'valueTransferred':valueTransferred, 
    'v' : signed_message.v, 'r' : utils.to_32byte_hex(signed_message.r), 's' : utils.to_32byte_hex(signed_message.s), 'withdraw': withdraw_pole}

    r = requests.post("http://127.0.0.1:8000/receiveCheck/", data=data)
    print('tx%i finished' % task_index)
end2 = time.time()
time_cost2 = end2 - begin
print(time_cost2)