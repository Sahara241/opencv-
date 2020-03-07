#More Mouse Event Examples in OpenCV Python
import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]       
        green = img[x,y,1]       
        red = img[x,y,2]
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)
        
        mycolorimage[:] = [blue,green,red]
        cv2.imshow('color',mycolorimage)

# 
#        cv2.circle(img,(x,y),3,(255,0,0),-1)
#        points.append((x,y))
#    if len(points) >=2:
#        cv2.line(img,points[-1],points[-2],(255,255,0),5)


img=cv2.imread('lena.jpg')
#img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()