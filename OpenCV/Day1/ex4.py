import cv2
data=cv2.VideoCapture('m_v.avi')
# print(data.isOpened)
if data.isOpened()==False:
    print("파일 로드 불가")
while True:
    ret,img = data.read()
    if ret==False:
        print("동영상 출력이 완료 되었습니다.")
        break
    cv2.imshow('m',img)
    key=cv2.waitKey(200)
    if key==27:
        print("동영상이 지루해")
        break
data.release()
cv2.destroyAllWindows()