import cv2
import sys
import numpy as np
 
camera = cv2.imread('grid_red.png', cv2.IMREAD_GRAYSCALE)
# Setup BlobDetector
params = cv2.SimpleBlobDetector_Params()	 	 
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(camera)

# Uncomment to resize to fit output window if needed
#im = cv2.resize(im, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow("Output", camera)

k = cv2.waitKey(1) & 0xff

camera.release()
cv2.destroyAllWindows()
