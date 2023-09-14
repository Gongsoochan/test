import cv2
img=cv2.imread("d1.jpg")
ck_img=img[300:400,300:500,:]
cv2.rectangle(img,(300,300),(500,400),(255,0,0),3)
cv2.imshow('img',img)
i1=cv2.resize(ck_img,(0,0),fx=5,fy=5,interpolation=cv2.INTER_NEAREST)
i2=cv2.resize(ck_img,(0,0),fx=5,fy=5,interpolation=cv2.INTER_LINEAR)
i3=cv2.resize(ck_img,(0,0),fx=5,fy=5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('ck_img',ck_img)
cv2.imshow('i1',ck_img)
cv2.imshow('i2',ck_img)
cv2.imshow('i3',ck_img)
cv2.waitKey()
