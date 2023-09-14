import cv2
import numpy as np
img=cv2.imread("d1.jpg")
re_img=cv2.resize(img,(0,0),fx=0.4,fy=0.4)
g_img=cv2.cvtColor(re_img,cv2.COLOR_BGR2GRAY)
cv2.putText(g_img,"old",(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255))
cv2.imshow("old",g_img)
g1=cv2.GaussianBlur(g_img,(3,3),0,0)
g2=cv2.GaussianBlur(g_img,(5,5),0,0)
g3=cv2.GaussianBlur(g_img,(9,9),0,0)
g_all=np.hstack(g1,g2,g3)
# cv2.imshow("G",g_all)

k=np.array([[-1,0,0],
          [0,0,0],
          [0,0,1]])

g_img16=np.int16(g_img)
# cv2.imshow('ck1',cv2.filter2D(g_img16,-1,k)+128)
tr_1=np.unit8(np.clip(cv2.filter2D(g_img16,-1,k)+128,0,255))
tr_2=np.unit8(cv2.filter2D(g_img16,-1,k)+128)
tr_3=cv2.filter2D(g_img,-1,k)

cv2.imshow('ck1',tr_1)
cv2.imshow('ck1',tr_2)
cv2.imshow('ck1',tr_3)
cv2.waitKey()
