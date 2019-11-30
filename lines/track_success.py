import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('v.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    
    # APLICA TRATAMENTO PARA BINARIZAR IMAGEM
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)[1]

    # ENCONTRA CONTORNOS NA IMAGEM
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)


    # LOOP NO CONTORNO PARA ENCONTRAR O CENTER_ID
    for c in cnts:
        # ENCONTRA O CENTRO DA IMAGEM
        M = cv2.moments(c)
        
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0

        print(cX, cY, '\n')
    
        width, height, aux = frame.shape
        
        #VER SE ESTA DE UM LADO OU DE OUTRO
        if cX < (width/2):
            print( 'esquerda' )
        else:
            print( 'direita' )
            
        cv2.line(frame, (int(width/2), 0), (int(width/2), height), (255, 100, 0), 3)
        
        # DESENHA ENCIMA DO CENTER_ID
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        cv2.circle(thresh, (cX, cY), 7, (255, 255, 255), -1)
        cv2.putText(frame, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
        
        cv2.imshow("Image", frame)
    
    
    # cv2.imshow('frame',thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()