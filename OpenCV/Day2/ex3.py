import cv2
img=cv2.imread('cube.jpg')
cv2.imshow('img',img)
cv2.circle(img,(100,100),5,(0,0,255),-1)
cv2.circle(img,(100,100),5,(0,0,255),-1)
cv2.circle(img,(100,100),5,(0,0,255),-1)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()


import cv2
img=cv2.imread('cube.jpg')
r=(0,0,255)
g=(0,255,0)
ck=[r,g]
def f(event,x,y,flags,p):
    global ck
    if event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),5,ck[0],-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        ck.reverse()

    cv2.imshow('img',img)

# def draw(event,x,y,f,p):
#     global ix,iy
#     if event==cv2.EVENT_LBUTTONDOWN:
#         ix,iy=x,y
#     elif event==cv2.EVENT_LBUTTONUP:
#         cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),5)
#     cv2.imshow('img',img)

# cv2.namedWindow('img')
# cv2.imshow('img',img)
# cv2.setMouseCallback('img',draw)

# while True:
#     if cv2.waitKey(1)==ord('a'):
#         cv2.destroyAllWindows()
#         break