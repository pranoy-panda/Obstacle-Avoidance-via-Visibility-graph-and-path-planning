import numpy as np
import cv2

def nothing(x):
    pass


'''
global variables
'''
refPt = []
cropping = False
inf = float("9e999")
 
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
 
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being performed

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)] # reference point for cropping
		cropping = True
 
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
 
		# drawing a rectangle around the region of interest
		#cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

def fun(image): 
	print 'fun'
	clone = image.copy()
	#image2 = image
	cv2.namedWindow("image")
	cv2.setMouseCallback("image", click_and_crop)
	list_of_min_vals= []
	list_of_max_vals =[] 
	num_of_unique_colors = 4 #(white(obstacles), bot(brown), objects(yellow), end(green))
	# keep looping until the 'q' key is pressed
	for i in xrange(num_of_unique_colors):	
		clone = image.copy()
		cv2.namedWindow("image")
		cv2.setMouseCallback("image", click_and_crop)
		 
		# keep looping until the 'q' key is pressed
		while True:
			# display the image and wait for a keypress
			cv2.imshow("image", image)
			key = cv2.waitKey(1) & 0xFF
		 
			# if the 'r' key is pressed, reset the cropping region
			if key == ord("r"):
				image = clone.copy()
		 
			# if the 'c' key is pressed, break from the loop
			elif key == ord("c"):
				break
		 
		# if there are two reference points, then crop the region of interest
		# from the image and display it
		if len(refPt) == 2:
			roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
			max_val_R = roi[:,:,2].max() # max val of red channel in roi
			max_val_G = roi[:,:,1].max() # max val of green channel in roi
			max_val_B = roi[:,:,0].max() # max val of blue channel in roi

			min_val_R = roi[:,:,2].min() # min val of red channel in roi
			min_val_G = roi[:,:,1].min() # min val of green channel in roi
			min_val_B = roi[:,:,0].min() # min val of blue channel in roi
			cv2.imshow("roi", roi)
			cv2.waitKey(0)
		list_of_min_vals.append([min_val_B,min_val_G,min_val_R]) # [yellow,pink]	
		list_of_max_vals.append([max_val_B,max_val_G,max_val_R]) # [yellow,pink]
		cv2.destroyAllWindows()
	return list_of_max_vals,list_of_min_vals

def colored_object_tracker(image):

	'''
	for segmentation of colored objects from a video source, first we crop a small section of the desired
	object and then fine tune the values 
	'''
	#uncomment the below given lines for actual video feed
	'''
	cap=cv2.VideoCapture(0)
	count = 30 # need to skip first few frames(due to camera initialization)
	while count>0:
		_,image = cap.read()
		count-=1
	'''	
	#global image
	#image = cv2.imread('Capture.JPG')
	list_of_max_vals,list_of_min_vals = fun(image)
	cv2.namedWindow('image1')
	cv2.namedWindow('image2')
	# cv2.createTrackbar(trackbarName,window_name,start_value,max_value,CallBackFunction)
	cv2.createTrackbar('b_low','image1',list_of_min_vals[0][0],255,nothing)
	cv2.createTrackbar('b_high','image1',list_of_max_vals[0][0],255,nothing)
	cv2.createTrackbar('g_low','image1',list_of_min_vals[0][1],255,nothing)
	cv2.createTrackbar('g_high','image1',list_of_max_vals[0][1],255,nothing)
	cv2.createTrackbar('r_low','image1',list_of_min_vals[0][2],255,nothing)
	cv2.createTrackbar('r_high','image1',list_of_max_vals[0][2],255,nothing)
	cv2.createTrackbar('abc','image2',0,1,nothing)
	flag = 0
	for i in xrange(len(list_of_max_vals)):
		while True:
			frame = cv2.imread('Capture.JPG')
			cv2.imshow('image2',frame)
			#frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

			####################
			abc = cv2.getTrackbarPos('abc','image2')
			if abc ==1:
				list_of_max_vals[i][0] = b_low
				list_of_max_vals[i][1] = g_low
				list_of_max_vals[i][2] = r_low
				list_of_min_vals[i][0] = b_high
				list_of_min_vals[i][1] = g_high
				list_of_min_vals[i][2] = r_high
				if i == len(list_of_max_vals)-1: 
					flag = 1  # end of thresholding
					break 
				cv2.setTrackbarPos('abc','image2',0)
				cv2.setTrackbarPos('b_low','image1',list_of_min_vals[i+1][0])
				cv2.setTrackbarPos('g_low','image1',list_of_min_vals[i+1][1])
				cv2.setTrackbarPos('r_low','image1',list_of_min_vals[i+1][2])
				cv2.setTrackbarPos('b_high','image1',list_of_max_vals[i+1][0])
				cv2.setTrackbarPos('g_high','image1',list_of_max_vals[i+1][1])
				cv2.setTrackbarPos('r_high','image1',list_of_max_vals[i+1][2])
				break

			b_low = cv2.getTrackbarPos('b_low','image1')
			b_high = cv2.getTrackbarPos('b_high','image1')
			
			r_low = cv2.getTrackbarPos('r_low','image1')
			r_high = cv2.getTrackbarPos('r_high','image1')
			
			g_high = cv2.getTrackbarPos('g_high','image1')
			g_low = cv2.getTrackbarPos('g_low','image1')
			

			low=np.array([b_low,g_low,r_low])
			high=np.array([b_high,g_high,r_high])
			mask=cv2.inRange(frame,low,high)
			res=cv2.bitwise_and(frame,frame,mask=mask)

			cv2.imshow('image1',res)

			q=cv2.waitKey(10) 

		if flag == 1:
			break 
		#cap.release()
	cv2.destroyAllWindows()	 
	return list_of_max_vals,list_of_min_vals           
		
if __name__ == '__main__':
	main()