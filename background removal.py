# import cv2 to capture videofeed
import cv2

import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(1)

# setting framewidth and frameheight as 640 X 480
#camera.set(3 , 640)
#camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mounteverest.jpg')

# resizing the mountain image as 640 X 480
mountain = cv2.resize(mountain, (640, 480))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([])
        upper_bound = np.array([])
        
        # thresholding image
        lower_bound = np.array([129,81,55])
        upper_bound = np.array([89,24,21])
        # inverting the mask
        mask_1 = cv2.inRange(frame_rgb, lower_bound, upper_bound)
        cv2.imshow("mask_1", mask_1)
        # bitwise and operation to extract foreground / person
        
        #Selecting only the part that does not have mask one and saving in mask 2
        mask_2 = cv2.bitwise_not(mask_1)
        res_1 = cv2.bitwise_and(frame, frame,mask=mask_2)
        # final image 
        final_image = np.where(res_1 == 0 , mountain , res_1)

        # show it
        cv2.imshow('frame' , frame)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()