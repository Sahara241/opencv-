#Canny Edge Detection in OpenCV
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('ronaldo.jpg',0)
img2=cv2.imread('lena.jpg',0)

canny=cv2.Canny(img,100,200)
lena=cv2.Canny(img2,100,200)

titles=['image','image2','canny','canny2']
images=[img,canny,img2,lena]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

#The canny edge detection algorthm in steps:
#      1.)Noise reduction
#      2.)Gradient calculation
#      3.)Non-maximum supression
#      4.)Double threshold
#      5.)Edge Tracking by Hysteresis