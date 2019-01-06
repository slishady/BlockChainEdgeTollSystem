import cv2
import requests
import json
import base64

# def send_task():
with open('image/test2.jpeg', 'rb') as imageFile:
	image2str = base64.b64encode(imageFile.read())
a = image2str.decode('ascii')
r = requests.post('http://faceai.jiangxingai.com:8099/detect', data = json.dumps({'image': a}))

# r = requests.get('http://faceai.jiangxingai.com:8099/detect')
# print(r.status_code)
# print(r.text)
# print(json.loads(r.text)['data']['recognitions'][0]['position']['Xmax'])
# print(r.status_code)
print(r.text)
left_up = (json.loads(r.text)['data']['recognitions'][0]['position']['Ymax'], json.loads(r.text)['data']['recognitions'][0]['position']['Xmin'])
right_down = (json.loads(r.text)['data']['recognitions'][0]['position']['Ymin'], json.loads(r.text)['data']['recognitions'][0]['position']['Xmax'])
# print(left_up)
# print(right_down)
{"Xmax": 393,"Xmin": 344,"Ymax": 329,"Ymin": 285}
img = cv2.imread('image/test2.jpeg')
print(img.shape)
# left_up = (640, 480)
# right_down = (1, 1)
cv2.rectangle(img, left_up, right_down, (0,255,0), 4)
# cv2.putText(img, 'the face box', left_up, 2, (0,255,0), 4)
cv2.imwrite('image/test9.jpeg', img)




# r = requests.get('http://faceai.jiangxingai.com:8099/detect')
# print(r.status_code)
# print(r.text)