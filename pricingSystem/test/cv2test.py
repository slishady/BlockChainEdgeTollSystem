import cv2
from web3 import Web3, HTTPProvider
def snapshot():
    """enable the camera and take a photo"""
    cap = cv2.VideoCapture(0)
    while(1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("./image/test2.jpeg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

snapshot()
