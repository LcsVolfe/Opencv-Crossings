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

    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)    
    canny = cv2.Canny(gradient, 175, 65)
    #cv2.imshow('tratamento',gradient)
    
    
    filter = False


    # file_path = 'bioterio.png'
    # img = cv2.imread(file_path)

    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(gray,90,150,apertureSize = 3)
    # kernel = np.ones((3,3),np.uint8)
    # edges = cv2.dilate(edges,kernel,iterations = 1)
    # kernel = np.ones((5,5),np.uint8)
    # edges = cv2.erode(edges,kernel,iterations = 1)

    cv2.imwrite('edge.png',canny)

    lines = cv2.HoughLines(canny,1,np.pi/1,1)

    if not lines.any():
        print('No lines were found')
        exit()

    if filter:
        rho_threshold = 15
        theta_threshold = 0.1

        # how many lines are similar to a given one
        similar_lines = {i : [] for i in range(len(lines))}
        for i in range(len(lines)):
            for j in range(len(lines)):
                if i == j:
                    continue

                rho_i,theta_i = lines[i][0]
                rho_j,theta_j = lines[j][0]
                if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
                    similar_lines[i].append(j)

        # ordering the INDECES of the lines by how many are similar to them
        indices = [i for i in range(len(lines))]
        indices.sort(key=lambda x : len(similar_lines[x]))

        # line flags is the base for the filtering
        line_flags = len(lines)*[True]
        for i in range(len(lines) - 1):
            if not line_flags[indices[i]]: # if we already disregarded the ith element in the ordered list then we don't care (we will not delete anything based on it and we will never reconsider using this line again)
                continue

            for j in range(i + 1, len(lines)): # we are only considering those elements that had less similar line
                if not line_flags[indices[j]]: # and only if we have not disregarded them already
                    continue

                rho_i,theta_i = lines[indices[i]][0]
                rho_j,theta_j = lines[indices[j]][0]
                if abs(rho_i - rho_j) < rho_threshold and abs(theta_i - theta_j) < theta_threshold:
                    line_flags[indices[j]] = False # if it is similar and have not been disregarded yet then drop it now

    print('number of Hough lines:', len(lines))

    filtered_lines = []

    if filter:
        for i in range(len(lines)): # filtering
            if line_flags[i]:
                filtered_lines.append(lines[i])

        print('Number of filtered lines:', len(filtered_lines))
    else:
        filtered_lines = lines

    for line in filtered_lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(fr,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imwrite('hough.jpg',fr)

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