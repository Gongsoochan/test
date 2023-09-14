import cv2
import numpy as np
cam=cv2.VideoCapture(0)
# cam.read()
# print(cam.isOpened())
if cam.isOpened()==False:
    print("연결 불가")
    exit(1)
# print("실행")
while True:
    ret,img=cam.read()
    if ret==False:
        print("캡처불가")
        break
    cv2.imshow('t',img)
    key=cv2.waitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()