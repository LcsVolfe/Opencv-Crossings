import cv2 
import numpy as np 

img = cv2.imread('grids_red.png')
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
ret, tresh = cv2.threshold(hsv,16,255,cv2.THRESH_BINARY)

canny = cv2.Canny(tresh, 50, 50 )

cv2.imshow("shapes", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()