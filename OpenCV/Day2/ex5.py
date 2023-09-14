import cv2
import matplotlib.pyplot as plt
img=cv2.imread('cube.jpg')
hb=print(cv2.calcHist([img],[0],None,[256],[0,256]))
hg=print(cv2.calcHist([img],[1],None,[256],[0,256]))
hr=print(cv2.calcHist([img],[2],None,[256],[0,256]))
print(img.shape)
rim=img[:,:,2]
gim=img[:,:,1]
bim=img[:,:,0]
print(rim.shape,gim.shape,bim.shape)
f_rg=rim.reshape(-1)
print(f_rg.shape)
plt.plot(hb,'b-')
plt.plot(hg,'g-')
plt.plot(hr,'r-')
plt.show()
plt.hist(f_rg)
plt.show()