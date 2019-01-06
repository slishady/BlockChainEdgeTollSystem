import cv2
import requests
import json

from utils import utils
def snapshot():
    """enable the camera and take a photo"""
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("/Users/a931759898/Desktop/Desktop/BlockChain/edgePricingSystem/edgePricingSystem/pricingSystem/test/image/fangjian2.jpeg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

r = requests.post('http://127.0.0.1:8000/selectEdge/', data={'edgesWiFi': [1,2,3]})
print(json.loads(r.text)['edge'])