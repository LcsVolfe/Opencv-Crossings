import cv2
import numpy as np

img = cv2.imread('grids_red.png')
img1 = cv2.imread('img.png')
newimg = cv2.resize(img,(600,600))
newimg2 = cv2.resize(img1,(600,600))


sub = cv2.absdiff(newimg2,newimg)

cv2.imshow("img", sub)
cv2.waitKey(0)
cv2.destroyAllWindows()