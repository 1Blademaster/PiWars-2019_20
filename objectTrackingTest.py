import numpy as np
import imutils
import cv2

colorLower = (104, 193, 68)
colorUpper = (115, 255, 255)

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()

    frame = imutils.resize(frame, width=800)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(mask, None, iterations=1)

    maskFrame = cv2.bitwise_and(frame, frame, mask=mask)

    # find contours in the mask and initialize the current
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) #This sets the variable center to the location of the center in a tuple of (x, y)

        cv2.circle(frame, center, 5, (0, 0, 255), -1) #Displays the center location of the object

        if center[0] < 300:
            print('Object is on left')
        if center[0] > 600:
            print('Object is on right')

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask Frame", maskFrame)

    key = cv2.waitKey(1)
    if key == 27:
        break


# cleanup the camera and close any open windows
cam.release()
cv2.destroyAllWindows()
