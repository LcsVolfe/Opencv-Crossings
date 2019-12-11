import numpy as np
import cv2

img = cv2.imread('img.png')
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_red = np.array([0,120,70])
high_red = np.array([180,255,255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(img, img, mask=red_mask)

cv2.imshow('hsv_frame',hsv_frame)
cv2.imshow('red_mask',red_mask)
cv2.imshow('red',red)

cv2.waitKey(0)
cv2.destroyAllWindows()
