import cv2
import matplotlib.pyplot as plt
data=cv2.imread('car1.jpg',cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img',data)
# cv2.waitKey(0)
# print(data.shape)
# print(data[0,0])
# d=data
# print(id(data),id(data))
# cv2.line(data,(50,50),(50,100),0,5)
# cv2.line(data,(50,50),(100,50),4,5)
# cv2.line(data,(50,100),(100,100),4,5)
# cv2.line(data,(100,100),(100,100),4,5)
# cv2.imshow('img',data)
# cv2.waitKey(0)
# cv2.line((0,0),(200,200),0,10)
print("변환전")
print(data[0,0])
print(data[250,250])
ret,th_img=cv2.threshold(data,127,255,cv2.THRESH_BINARY)
print("변환전")
print(th_img[0,0])
print(th_img[250,250])
# print(cv2.THRESH_BINARY)
# print(cv2.THRESH_MASK)
# print(cv2.THRESH_BINARY)
# cv2.imshow('img',th_img)
# cv2.waitKey(0)
