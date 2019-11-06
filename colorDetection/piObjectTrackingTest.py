import cv2
import numpy as np
import time
from imutils.video import VideoStream
import imutils
import utils.colors as c

cap = VideoStream(src=0, usePiCamera=True, framerate=32).start()

time.sleep(0.5)

print('--- Press ESC to end the video feed ---')

while True:
    frame = cap.read()

    frame = imutils.resize(frame, width=800)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    col = c.lightBlue

    # hue, saturation, value
    colorLower = np.array([col[0, 0], col[0, 1], col[0, 2]])
    colorUpper = np.array([col[1, 0], col[1, 1], col[1, 2]])

    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=1)
    mask = cv2.dilate(mask, None, iterations=1)

    maskFrame = cv2.bitwise_and(frame, frame, mask=mask)

    # find contours in the mask and initialize the current
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None

    if len(cnts) > 0:
        maxCNT = max(cnts, key=cv2.contourArea)
        maxM = cv2.moments(maxCNT)
        maxCenter = (int(maxM["m10"] / maxM["m00"]), int(maxM["m01"] / maxM["m00"])) #This sets the variable center to the location of the center in a tuple of (x, y)

        cv2.circle(frame, maxCenter, 5, (0, 255, 0), -1)
        
        if len(cnts) > 5:
            cnts = cnts[:5]

        for cnt in cnts:
            if np.all(cnt != maxCNT):
                M = cv2.moments(cnt)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

                cv2.circle(frame, center, 5, (0, 0, 255), -1) #Displays the center location of the object
        if maxCenter[0] < 150:
            print('Object is on far left')
        if maxCenter[0] < 350:
            print('Object is on left')
        if maxCenter[0] > 450:
            print('Object is on right')
        if maxCenter[0] > 650:
            print('Object is on far right')
        if maxCenter[0] >= 350 and maxCenter[0] <= 450:
            print('Object is in center')

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask Frame", maskFrame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.stop()
cv2.destroyAllWindows()
