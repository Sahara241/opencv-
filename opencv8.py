#cv.split, cv.merge, cv.resize, cv.add, cv.addWeighted, ROI
import cv2
img=cv2.imread('lena.jpg')
img2=cv2.imread('messi5.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))

eye = img[247:247,293:293]
img[299:299,335:335] = eye

img=cv2.resize(img,(512,512))
img2=cv2.resize(img2,(512,512))

#dst=cv2.add(img,img2)
dst=cv2.addWeighted(img,.3,img2,.7,0)
cv2.imshow('image',dst)   

cv2.waitKey(0)
cv2.destroyAllWindows()                                             