#Image Gradients and Edge Detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('sudoku.png',cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
SobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
SobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

SobelX=np.uint8(np.absolute(SobelX))
SobelY=np.uint8(np.absolute(SobelY))

SobelCombined=cv2.bitwise_or(SobelX,SobelY)

titles=['image','Laplacian','SobelX','SobelY','SobelCombined']
images=[img,lap,SobelX,SobelY,SobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
