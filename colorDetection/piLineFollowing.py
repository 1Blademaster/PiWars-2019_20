import cv2
import numpy as np
import time
from imutils.video import VideoStream
import imutils
import utils.colors as c
from robot import Robot

cap = VideoStream(src=0, usePiCamera=True, framerate=32).start()

time.sleep(0.5)

print('--- Press ESC to end the video feed ---')

robot = Robot()

while True:
    try:
        frame = cap.read()
        frame = imutils.resize(frame, width=800)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame,(5,5),0)
        _, thresh = cv2.threshold(frame,60,255,cv2.THRESH_BINARY)

        # find contours in the mask and initialize the current
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        if len(cnts) > 0:
            maxCNT = max(cnts, key=cv2.contourArea)
            maxM = cv2.moments(maxCNT)
            try:
                maxCenter = (int(maxM["m10"] / maxM["m00"]), int(maxM["m01"] / maxM["m00"])) #This sets the variable center to the location of the center in a tuple of (x, y)
            except:
                continue
            cv2.circle(frame, maxCenter, 5, (0, 255, 0), -1)

            if maxCenter[0] < 150:
                print('Object is on far left')
                robot.turnRight(timeSleep=0.2, speed=100)
            if maxCenter[0] < 350:
                print('Object is on left')
                robot.turnRight(timeSleep=0.1, speed=100)
            if maxCenter[0] > 450:
                print('Object is on right')
                robot.turnLeft(timeSleep=0.1, speed=100)
            if maxCenter[0] > 650:
                print('Object is on far right')
                robot.turnLeft(timeSleep=0.2, speed=100)
            if maxCenter[0] >= 350 and maxCenter[0] <= 450:
                robot.backward(timeSleep=0.2)
                print('Object is in center')
        else:
            print('Object not in frame')
            #robot.turnRight(timeSleep=0.2, speed=100)
            
        cv2.imshow("Masked Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    except KeyboardInterrupt:
        print('Ending object tracking')
        break

cap.stop()
cv2.destroyAllWindows()
robot.shutdown()
