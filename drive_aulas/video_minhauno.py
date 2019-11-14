import numpy as np
import cv2

#cap = cv2.VideoCapture('bio.mp4')
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #gray = cv2.cvtColor(gray, cv2.COLOR_HSV2BGR)
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2YCR_CB)
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2YCR_CB)
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2HSV)
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2RGB)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()