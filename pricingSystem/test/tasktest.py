import cv2
import requests
import json
import base64
def send_task():
    """
    send a picture to server and receive response.
    """
    a = cv2.imread('image/test2.jpeg')
    a = bytearray(a)
    a = a.decode('base64')
    r = requests.post('http://192.168.0.172:8099/detect', json = {'image': a})
    return r
def send_task():
	with open('image/test2.jpeg', 'rb') as imageFile:
		image2str = base64.b64encode(imageFile.read())
	a = image2str.decode('ascii')
	r = requests.post('http://192.168.0.172:8099/detect', json = {'image': a})
	return r


r = send_task()
print(r.text)
print(r.status_code)