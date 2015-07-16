# rong bee color ID

# import packages
import cv2
import numpy as np
import math
import argparse

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True,help="full path to image")
args = vars(ap.parse_args())

# load the image and clone it
frameOriginal = cv2.imread(args["image"])

frame = frameOriginal.copy()


def takePhotos(frame,folder):
	for i in range(1,3):
		for j in range(1,4):
			cropped = frame[1728*(i-1):1727*i,1728*(j-1):1727*j]
			name = "picture" + str(i) + str(j) + ".jpg"
			cv2.imwrite(folder+name,cropped)
			print i,j

# find empty cells
def findEmpty(image):
	
	#takePhotos(image,"/Users/lukereding/Desktop/original/")
	
	imageCropped1 = image[550:1475,1250:2175]
	cv2.imwrite("/Users/lukereding/Desktop/originalCropped1.jpg",imageCropped1)
	
	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	#takePhotos(hsv,"/Users/lukereding/Desktop/hsv/")
	#cv2.imwrite("/Users/lukereding/Desktop/hsv.jpg",hsv)
	lab = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#takePhotos(lab,"/Users/lukereding/Desktop/lab/")
	# biltaeral filter
	filtered = cv2.bilateralFilter(hsv,20,20,20)

	blur = cv2.blur(filtered,(20,20))

	# define range of green color in HSV
	lowerGreen = np.array([30,0,0])
	upperGreen = np.array([255,91,73])

	# Threshold the HSV image to get only green colors
	mask = cv2.inRange(blur, lowerGreen,upperGreen)
	#takePhotos(mask,"/Users/lukereding/Desktop/mask/")
	
	maskCropped = mask[550:1475,2175:3100]
	#cv2.imwrite("/Users/lukereding/Desktop/test.jpg",maskCropped)

	contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

	print "original number of contours: " + str((len(contours)))

	cv2.imwrite("/Users/lukereding/Desktop/maskWithContours.jpg",mask)
	
	# find the contours
	contoursToKeep = []
	for i in contours:
		i = i.astype(np.int64)
		area = cv2.contourArea(i)
		# x and y are the coordinates of the top left hand corner of the bounding rectangle
		arclen = cv2.arcLength(i, True)
		if arclen > 0 :
			circularity = (4 * math.pi * area) / (arclen * arclen)
			if area > 5000 and circularity > 0.5:
				print round(area,2), round(circularity,2)
				cv2.drawContours(mask,[i],0,(215,184,0),3)
				contoursToKeep.append(i)
				box = cv2.boundingRect(i)
				obj_center=((box[0] + (box[2] / 2), box[1] + (box[3] / 2)))
				cv2.circle(frame,obj_center,15,(255,255,255),-1)

	print str(len(contoursToKeep)) + " empty cells"
	
	frameCropped=frame[1475:2400,2175:3100]
	takePhotos(frame,"/Users/lukereding/Desktop/circles/")
	#cv2.imwrite("/Users/lukereding/Desktop/circles.jpg",frameCropped)
	takePhotos(mask,"/Users/lukereding/Desktop/contours/")
	maskCropped2 = mask[1475:2400,1250:2175]
	#cv2.imwrite("/Users/lukereding/Desktop/contoursKept.jpg",maskCropped2)
	return mask

def findBrood(image):
	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	# biltaeral filter
	filtered = cv2.bilateralFilter(hsv,20,20,20)

	blur = cv2.blur(filtered,(20,20))

	# define range of green color in HSV
	lowerGreen = np.array([12,77,199])
	upperGreen = np.array([18,174,255])

	# Threshold the HSV image to get only green colors
	mask = cv2.inRange(blur, lowerGreen,upperGreen)

	#cv2.imwrite("/Users/lukereding/Desktop/test.jpg",mask)

	contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

	print "original number of contours: " + str((len(contours)))

	#cv2.imwrite("/Users/lukereding/Desktop/maskWithContours.jpg",mask)
	
	# find the contours
	contoursToKeep = []
	for i in contours:
		i = i.astype(np.int64)
		area = cv2.contourArea(i)
		# x and y are the coordinates of the top left hand corner of the bounding rectangle
		arclen = cv2.arcLength(i, True)
		if arclen > 0 :
			circularity = (4 * math.pi * area) / (arclen * arclen)
			if area > 5000 and circularity > 0.3:
				print area, circularity
				cv2.drawContours(mask,[i],0,(11,64,26),3)
				contoursToKeep.append(i)
				box = cv2.boundingRect(i)
				obj_center=((box[0] + (box[2] / 2), box[1] + (box[3] / 2)))
				cv2.circle(image,obj_center,15,(0,255,0),-1)

	print str(len(contoursToKeep)) + " brood cells" 
	
	return mask

	#cv2.imwrite("/Users/lukereding/Desktop/circles.jpg",frame)

	#cv2.imwrite("/Users/lukereding/Desktop/contoursKept.jpg",mask)

def findPollen(image):
	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
	blur = cv2.medianBlur(hsv,9)

	# biltaeral filter
	filtered = cv2.bilateralFilter(blur,20,20,20)
	
	# define range of green color in HSV
	lowerGreen = np.array([0,113,0])
	upperGreen = np.array([16,197,133])

	# Threshold the HSV image to get only green colors
	mask = cv2.inRange(blur, lowerGreen,upperGreen)

	#cv2.imwrite("/Users/lukereding/Desktop/test.jpg",mask)

	contours = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]

	print "original number of contours: " + str((len(contours)))

	#cv2.imwrite("/Users/lukereding/Desktop/maskWithContours.jpg",mask)
	
	# find the contours
	contoursToKeep = []
	for i in contours:
		i = i.astype(np.int64)
		area = cv2.contourArea(i)
		# x and y are the coordinates of the top left hand corner of the bounding rectangle
		arclen = cv2.arcLength(i, True)
		if arclen > 0 :
			circularity = (4 * math.pi * area) / (arclen * arclen)
			if area > 5000:
				print area, circularity
				cv2.drawContours(mask,[i],0,(151,45,20),3)
				contoursToKeep.append(i)
				box = cv2.boundingRect(i)
				obj_center=((box[0] + (box[2] / 2), box[1] + (box[3] / 2)))
				cv2.circle(frame,obj_center,15,(255,0,0),-1)

	print str(len(contoursToKeep)) + " pollen(?) cells" 
	
	return(mask)

	#cv2.imwrite("/Users/lukereding/Desktop/circles.jpg",frame)

	#cv2.imwrite("/Users/lukereding/Desktop/contoursKept.jpg",mask)

# find the number of empty cells, put a red dot in each
emptied = findEmpty(frame)
# find the number of brood cells, put a green dot in each
brooded = findBrood(frame)
# find the number of pollen? cells, put a green dot in each
pollened = findPollen(frame)

cv2.imwrite("/Users/lukereding/Desktop/theFinalie.tif",brooded)

cv2.destroyAllWindows()