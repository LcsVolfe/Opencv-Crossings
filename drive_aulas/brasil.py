import numpy as np
import cv2
w=700
h=400
img = np.zeros((h,w,3), np.uint8)
img[:] = (0,200,0)
pts = np.array([[20,h/2],[w/2,20],[w-20,h/2],[w/2,h-20]], np.int32)
cv2.fillPoly(img,[pts],(0,255,255))
cv2.circle(img,(w/2,h/2), h/4, (255,0,0), -1)
cv2.imshow('image',img)
cv2.waitKey(0)