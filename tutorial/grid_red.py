import cv2 as cv
import numpy as np



# #blurring and smoothin
# img1=cv2.imread('grids_red.png',1)

# hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

# #lower red
# lower_red = np.array([0,50,50])
# upper_red = np.array([10,255,255])


# #upper red
# lower_red2 = np.array([170,50,50])
# upper_red2 = np.array([180,255,255])

# mask = cv2.inRange(hsv, lower_red, upper_red)
# res = cv2.bitwise_and(img1,img1, mask= mask)


# mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
# res2 = cv2.bitwise_and(img1,img1, mask= mask2)

# img3 = res+res2
# img4 = cv2.add(res,res2)
# img5 = cv2.addWeighted(res,0.5,res2,0.5,0)


# kernel = np.ones((15,15),np.float32)/225
# smoothed = cv2.filter2D(res,-1,kernel)
# smoothed2 = cv2.filter2D(img3,-1,kernel)

# cv2.imshow('Original',img1)
# cv2.imshow('Averaging',smoothed)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)
# cv2.imshow('mask2',mask2)
# cv2.imshow('res2',res2)
# cv2.imshow('res3',img3)
# cv2.imshow('res4',img4)
# cv2.imshow('res5',img5)
# cv2.imshow('smooth2',smoothed2)




# cv2.waitKey(0)
# cv2.destroyAllWindows()

#######################################


kernel = np.ones((5,5), np.uint8) 

img = cv.imread('grids_red.png')
# img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
RGB2HSV = cv.cvtColor(img, cv.COLOR_RGB2HSV)
# img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# edges = cv.Canny(img,90,150,apertureSize = 3)
# kernel = np.ones((3,3),np.uint8)
# edges = cv.dilate(edges,kernel,iterations = 1)
# kernel = np.ones((5,5),np.uint8)
# edges = cv.erode(edges,kernel,iterations = 1)

gradient = cv.morphologyEx(RGB2HSV, cv.MORPH_GRADIENT, kernel)    
canny = cv.Canny(gradient, 175, 65)

blurred = cv.GaussianBlur(img, (9, 9), 0)
blurred1 = cv.GaussianBlur(RGB2HSV, (9, 9), 0)

hsv = cv.cvtColor(blurred, cv.COLOR_RGB2HSV)
hsv1 = cv.cvtColor(blurred1, cv.COLOR_RGB2HSV)

gradient=cv.morphologyEx(blurred,cv.MORPH_GRADIENT,kernel)
gradient1=cv.morphologyEx(hsv1,cv.MORPH_GRADIENT,kernel)




cv.imshow('gradient',gradient)
cv.imshow('gradient1',gradient1)
# cv.imshow("canny", canny)
# cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
