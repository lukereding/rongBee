
import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window

cv2.namedWindow('image')

image = cv2.imread("/Users/lukereding/Dropbox/rongBeePics/IMG_2738.JPG")

image = cv2.resize(image,(800, 600))

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#blur = cv2.medianBlur(hsv,7)

# biltaeral filter
blur = cv2.bilateralFilter(hsv,5,5,5)

# create trackbars for color change
cv2.createTrackbar('H_lower','image',0,255,nothing)
cv2.createTrackbar('S_lower','image',0,255,nothing)
cv2.createTrackbar('V_lower','image',0,255,nothing)

cv2.createTrackbar('H_upper','image',0,255,nothing)
cv2.createTrackbar('S_upper','image',0,255,nothing)
cv2.createTrackbar('V_upper','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    
    # get current positions of four trackbars
    H_lower = cv2.getTrackbarPos('H_lower','image')
    S_lower = cv2.getTrackbarPos('S_lower','image')
    V_lower = cv2.getTrackbarPos('V_lower','image')
    H_upper = cv2.getTrackbarPos('H_upper','image')
    S_upper = cv2.getTrackbarPos('S_upper','image')
    V_upper = cv2.getTrackbarPos('V_upper','image')
    sw = cv2.getTrackbarPos(switch,'image')

    if sw == 0:
    	cv2.imshow("image",blur)
        image[:] = 0
        k = cv2.waitKey(1) & 0xFF
    	if k == 27:
    		break
    else:
    	lowerGreen = np.array([H_lower,S_lower,V_lower])
    	upperGreen = np.array([H_upper,S_upper,V_upper])
    	print lowerGreen
    	print upperGreen
    	masked = cv2.inRange(blur, lowerGreen,upperGreen)
    	output = cv2.bitwise_and(hsv,hsv,mask = masked)
    	cv2.imshow("image",output)
    	k = cv2.waitKey(1) & 0xFF
    	if k == 27:
    		break

cv2.destroyAllWindows()