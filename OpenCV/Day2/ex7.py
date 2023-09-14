import cv2
import numpy as np
# cv2.IMREAD_COLOR
# cv2.IMREAD_UNCHANGED
# cv2.IMREAD_GRAYSCALE
img=cv2.imread("d2.png",cv2.IMREAD_UNCHANGED)
# cv2.imshow("gj_img",img)
# cv2.waitKey()
tr_img=img[(img.shape[0]//3)*2:,:,3]
print(tr_img.shape)
cv2.imshow("tr_img",tr_img)
cv2.waitKey()
se=np.unit9([[0 for _ in range(5)]for _ in range(5)])
d1=cv2.dilate(tr_img,se,iterations=0) #팽창
print(tr_img.shape)
cv2.imshow("tr_img",tr_img)
se=np.unit8([[0,0,1,0,0],
             [0,1,1,1,0],
             [1,1,1,1,1],
             [0,1,1,1,0],
             [0,0,1,0,0]])
d1=cv2.dilate(tr_img,se,iterations=1) # 팽창
cv2.imshow("d1_img",d1)
d2=cv2.erode(tr_img,se,iterations=1) # 침식
print(d1.shape)
cv2.imshow("d1_img",d1)
cv2.waitKey()