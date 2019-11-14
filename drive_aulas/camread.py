import cv2
import numpy
def nothing(x):
    pass
def show_webcam(mirror=False):
	cv2.namedWindow('python')
	# create trackbars for color change
	cv2.createTrackbar('R','python',0,255,nothing)
	cv2.createTrackbar('G','python',0,255,nothing)
	cv2.createTrackbar('B','python',0,255,nothing)
	# create switch for ON/OFF functionality
	switch = '0 : OFF \n1 : ON'
	cv2.createTrackbar(switch, 'python',0,1,nothing)
	cam=cv2.VideoCapture(1)
	while True:
		ret, img = cam.read()
		if ret == False:
			break
		if mirror:
			img = cv2.flip(img, 1)
		#img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
		#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		r = cv2.getTrackbarPos('R','python')
		g = cv2.getTrackbarPos('G','python')
		b = cv2.getTrackbarPos('B','python')
		s = cv2.getTrackbarPos(switch,'python')
		# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		bimg,gimg,rimg = cv2.split(img)
		if s == 0:
			img[:] = 0
		else:
			img = cv2.merge((bimg-b,gimg-g,rimg-r))
		cv2.imshow('python', img)
		if cv2.waitKey(1) == 27:
			break 
	cv2.destroyAllWindows()
show_webcam(mirror=True)