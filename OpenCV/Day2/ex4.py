import cv2
img=cv2.imread("cube.jpg")
cv2.imshow("all",img)
cv2.imshow("B",img[:,:,0])
cv2.imshow("G",img[:,:,1])
cv2.imshow("R",img[:,:,2])
cv2.waitKey(0)

import cv2


def cut(event,x,y,f,p):
    global sx,sy,ex,ey,img
    if event==cv2.EVENT_LBUTTONDOWN:
        sx,sy=x,y
    if event==cv2.EVENT_LBUTTONUP:
        sx,sy=x,y
        img=img[sy:ey,sx:ex,2]
    cv2.imshow('img',img)



cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.setMouseCallback('img',cut)