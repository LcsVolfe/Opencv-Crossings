import numpy as np
import cv2

cap = cv2.VideoCapture('bio_size.mp4')

while(True):
    ret, frame = cap.read()
    kernel = np.ones((5,5), np.uint8) 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
    

    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('video', 200, 200)
    cv2.imshow('main', thresh)    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()