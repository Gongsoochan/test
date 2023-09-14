import cv2
img=cv2.imread('cube.jpg')
# cv2.rectangle(이미지,시작점,종료점,(B,G,R),선굵기)
cv2.rectangle(img,(100,100),(200,200),(100,250,200),10)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()