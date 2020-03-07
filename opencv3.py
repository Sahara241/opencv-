#Draw geometric shapes on images using Python OpenCV
#import numpy as np
import cv2

img=cv2.imread('lena.jpg',1)

#img=np.zeros([500,500,3],np.uint8)
img=cv2.line(img,(0,0),(220,210),(255,0,0),4)
img=cv2.arrowedLine(img,(5,0),(230,215),(0,255,0),4)

img=cv2.rectangle(img,(240,210),(290,290),(0,0,255),3)
img=cv2.rectangle(img,(310,210),(360,290),(0,0,255),-1)

font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'opencv',(135,490),font,3,(255,255,0),6,cv2.LINE_AA)
img=cv2.circle(img,(300,350),30,(0,0,255),3)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
