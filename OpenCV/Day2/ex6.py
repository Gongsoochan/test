import cv2
img=cv2.imread('cube.jpg')
cv2.imshow("img",img)
cv2.waitKey(0)
t,tr_img=cv2.threshold(img[:,:,2],0,255,cv2.THRESH_BINARY)
print(cv2.THRESH_BINARY)
print(cv2.THRESH_OTSU)
cv2.imshow("img",tr_img)
cv2.waitKey(0)