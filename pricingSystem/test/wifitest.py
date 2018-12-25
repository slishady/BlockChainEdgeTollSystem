import pywifi
import sys
import time
from pywifi import *
from pywifi import const
import cv2
from wifi import Cell, Scheme
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


def deswifi(wifi_name):
    """
    connect with the specific wifi
    input: the wifi_name want to connect
    output: the successful connection
    """
    wifi=PyWiFi()#创建一个wifi对象
    ifaces=wifi.interfaces()[0]#取第一个无限网卡
    print(ifaces.name())#输出无线网卡名称
    ifaces.disconnect()#断开网卡连接
    time.sleep(3)#缓冲3秒
  
    profile1=Profile()#配置文件
    profile1.ssid=wifi_name#wifi名称
    profile1.auth=const.AUTH_ALG_OPEN#需要密码
    profile1.akm.append(const.AKM_TYPE_WPA2PSK)#加密类型
    profile1.cipher=const.CIPHER_TYPE_CCMP#加密单元

    ifaces.remove_all_network_profiles()#删除其他配置文件
    tmp_profile=ifaces.add_network_profile(profile1)#加载配置文件

    ifaces.connect(tmp_profile)#连接
    time.sleep(10)#尝试10秒能否成功连接
    isok=True
    if ifaces.status()==const.IFACE_CONNECTED:
        print("成功连接")
    else:
        print("失败")
    ifaces.disconnect()#断开连接
    time.sleep(1)
    return isok

def find_wifi():
    all_wifi = Cell.all('wlan0')
    for wifi in all_wifi:
        print(wifi.ssid)


#get all WIFI connenction
# bies()
# deswifi('1')
# for wifi in bessis:
#     print(wifi.ssid)
#select Edge
# edgesWiFi = [node for node in bessis if node.ssid.startswith('JXEdge')]

# data = {'edgesWiFi' : edgesWiFi}
# r = requests.post("http://127.0.0.1:8000/selectEdge/", data=data)


# #connect to the corresponding wifi
# edge = json.loads(r.text)['edge']
# deswifi(edge)


# #开启摄像头拍摄一个照片
# snapshot()

def test_wifi_connect(passwordstr):
    wifi=pywifi.PyWiFi()#初始化
    ifaces=wifi.interfaces()[0]#创建取出第一个无限网卡
    #print(ifaces.name())#输出无限网卡名
    ifaces.disconnect()#断开无限网卡连接
    time.sleep(3)#断开以后缓冲3秒

    profile=pywifi.Profile()#配置文件
    profile.ssid="1"#wifi名称
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

bies()
print(test_wifi_connect('20690539'))
