import cv2
import matplotlib.pyplot as plt
data=cv2.imread('car1.jpg')
cv2.namedWindow("t") # 윈도우 만들기
cv2.imshow('t',data) # 윈도우에 그림 출력
cv2.waitKey(0) # 윈도우 실행 중 모든 키입력
cv2.destroyAllWindows() # 모든 윈도우 닫기
# print(cv2.COLOR_BGR2GRAY)
# print(cv2.COLOR_BGR2RGB)
gry_data=cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
rgb_data=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
cv2.namedWindow("m1") # 윈도우 만들기
cv2.imshow('m',gry_data) # 윈도우에 그림 출력
cv2.waitKey() # 대기
cv2.destroyAllWindows()
plt.imshow(rgb_data)
plt.show()



# print(data.shape)

# plt.imshow(data)
# plt.show()

# print(cv2.IMREAD_COLOR)



# opencv(BGR)와 matplotlib(RGB)은 color pattern이 다르다.