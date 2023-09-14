import cv2
img=cv2.imread('cube.jpg')

def draw(event,x,y,f,p):
    global ix,iy
    if event==cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),5)
    cv2.imshow('img',img)

cv2.namedWindow('img')
cv2.imshow('img',img)
cv2.setMouseCallback('img',draw)

while True:
    if cv2.waitKey(1)==ord('a'):
        cv2.destroyAllWindows()
        break