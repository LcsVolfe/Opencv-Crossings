import numpy as np
import cv2

cap = cv2.VideoCapture('bio_cut.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    fr = cv2.resize(frame, (600,600))

    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5,5), np.uint8) 

    #erode = cv2.erode(gray, kernel, iterations=1)
    #canny = cv2.Canny(gray, 175, 65)
    #opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)    
    #closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    #gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    #tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    #blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    #cv2.imshow('erode',erode)
    #cv2.imshow('canny',canny)
    #cv2.imshow('opening',opening)
    #cv2.imshow('closing',closing)
    #cv2.imshow('gradient',gradient)
    #cv2.imshow('tophat',tophat)
    #cv2.imshow('blackhat',blackhat)
    
    
    
    ############### TESTES

    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)    
    canny = cv2.Canny(gradient, 175, 65)
    cv2.imshow('tratamento',gradient)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()