import cv2
import numpy as np
img=cv2.imread("cube.jpg")
tr_img=cv2.resize(img,(0,0),fx=0.25,fy=0.25)
cv2.imshow('img',img)
cv2.imshow('tr_img',img)
print(img.shape,tr_img.shape)
cv2.imshow('tr_img10',tr_img-10)
cv2.imshow('tr_img10',tr_img-20)
cv2.imshow('tr_img10',tr_img-30)
def g_tr(f,g=1.0):
    s_f=f/255.0
    return np.nint8(255*(s_f**g))
end_data=np.hstack(g_tr(tr_img,0.5),g_tr(tr_img,0.7),g_tr(tr_img,1.0),g_tr(tr_img,2.0),g_tr(tr_img,3.0))
cv2.imshow('g_all_data',end_data)

cv2.waitKey()