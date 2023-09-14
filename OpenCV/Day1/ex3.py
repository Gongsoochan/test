import cv2
import numpy as np
cam=cv2.VideoCapture(0)

if cam.isOpened()==False:
    print("연결 불가")
    exit(1)
ret, img=cam.read()
if ret==False:
    print("캡처불가")
    exit(1)

codec = cv2.VideoWriter_fourcc('M','J','P','G')
fps=30.0
h,w=img.shape[:2]
m_v=cv2.VideoWriter("m_v.avi",codec,fps,(w,h))

if m_v.isOpened==False:
    print("동영상을 만들 수 없습니다.")
    exit(1)

while True:
    ret, img=cam.read()
    if ret==False:
        print("캡처불가")
        break
    m_v.write(img)
    cv2.imshow('m_v',img)
    key=cv2.waitKey(1)
    if key==27:
        break


cam.release()
m_v.release()
cv2.destroyAllWindows()