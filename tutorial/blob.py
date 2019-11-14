import numpy as np
import cv2

cap = cv2.VideoCapture('bio_size.mp4')

while(True):
    ret, frame = cap.read()

    params = cv2.SimpleBlobDetector_Params()
 
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 300


    detector = cv2.SimpleBlobDetector_create(params)

    gray = cv2.cvtColor(frame, cv2.IMREAD_GRAYSCALE)
    keypoints = detector.detect(gray)
    imgKeyPoints = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('video', 200, 200)
    
    cv2.imshow('main', imgKeyPoints)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# # Read in the image in grayscale
# img = cv2.imread('token.png', cv2.IMREAD_GRAYSCALE)

# # Determine which openCV version were using
# if cv2.__version__.startswith('2.'):
#     detector = cv2.SimpleBlobDetector()
# else:
#     detector = cv2.SimpleBlobDetector_create()

# # Detect the blobs in the image
# keypoints = detector.detect(img)
# print(len(keypoints))

# # Draw detected keypoints as red circles
# imgKeyPoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# # Display found keypoints
# cv2.imshow("Keypoints", imgKeyPoints)
# cv2.waitKey(0)

# cv2.destroyAllWindows()