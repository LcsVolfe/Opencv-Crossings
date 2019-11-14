import cv2
import numpy as np
img = cv2.imread("token.png")
roi = img[10: 395, 10: 20]
x = 154
y = 252
width = 455 - x
height = 395 - y
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
cap = cv2.VideoCapture('token.mp4')
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while True:
    _, frame = cap.read()
    fr = cv2.resize(frame, (600,600))

    hsv = cv2.cvtColor(fr, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    cv2.polylines(fr, [pts], True, (255, 0, 0), 2)
    cv2.imshow("Frame", fr)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()