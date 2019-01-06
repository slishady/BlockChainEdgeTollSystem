import requests

edgesWiFi = ['TP-LINK_4423']
data = {'edgesWiFi' : edgesWiFi}
r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)
print(r.text)