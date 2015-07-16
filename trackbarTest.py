import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window

cv2.namedWindow('image')

image = cv2.imread("/Users/lukereding/Dropbox/rongBeePics/IMG_2736.JPG")

image = cv2.resize(image,(800, 600))

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# biltaeral filter
filtered = cv2.bilateralFilter(hsv,20,20,20)

blur = cv2.blur(filtered,(5,5))

# create trackbars for color change
cv2.createTrackbar('H','image',0,255,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('V','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    
    # get current positions of four trackbars
    H = cv2.getTrackbarPos('H','image')
    S = cv2.getTrackbarPos('S','image')
    V = cv2.getTrackbarPos('V','image')
    sw = cv2.getTrackbarPos(switch,'image')

    if sw == 0:
    	cv2.imshow("image",blur)
        image[:] = 0
        print (H,S,V)
        k = cv2.waitKey(1) & 0xFF
    	if k == 27:
    		break
    else:
    	lowerGreen = np.array([H,S,V])
    	upperGreen = np.array([16,187,255])
    	print lowerGreen
    	print upperGreen
    	masked = cv2.inRange(blur, lowerGreen,upperGreen)
    	cv2.imshow("image",masked)
    	k = cv2.waitKey(1) & 0xFF
    	if k == 27:
    		break

cv2.destroyAllWindows()