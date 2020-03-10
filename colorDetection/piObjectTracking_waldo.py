import cv2
import numpy as np
import time
from imutils.video import VideoStream
import imutils
import utils.colors as c
from robot import Robot
import RPi.GPIO as GPIO


cap = VideoStream(src=0, usePiCamera=True, framerate=32).start()

time.sleep(0.5)

print('--- Press ESC to end the video feed ---')

robot = Robot()
status = None
n = 1
servoval = 0
servoval = float(servoval)

global degrees
degrees = 120
global status1
status1 = "yes"
def degcheck():
    if degrees == 10  or degrees == 180:
        
        status1 = "No"
    else:
        status1 = "Yes"
def servomove():
    pass
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm = GPIO.PWM(3, 50)
    pwm.start(0)
    duty = (degrees/12.9)+2
    print(degrees, duty)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.2)
    pwm.stop()
    GPIO.cleanup()

degrees = 120
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm = GPIO.PWM(3, 50)
pwm.start(0)
duty = (degrees/12.9)+2
print(degrees, duty)
pwm.ChangeDutyCycle(duty)
time.sleep(0.2)
pwm.stop()



while True:
    GPIO.setmode(GPIO.BOARD)
    
    try:
        frame = cap.read()

        frame = imutils.resize(frame, width=800 ,height=800)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        col = c.red2

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
            # centre value: 350 <= x <= 450
            if maxCenter[0] < 150:
                print('Object is on far left')
                robot.turnLeft(timeSleep=0.2, speed=100)
                robot.forward(timeSleep=0.1, speed=100)
                status = "fl"
            elif maxCenter[0] < 350:
                print('Object is on left')
                robot.turnLeft(timeSleep=0.1, speed=100)
                robot.forward(timeSleep=0.1, speed=100)
                status = "l"
            elif maxCenter[0] > 450:
                print('Object is on right')
                robot.turnRight(timeSleep=0.1, speed=100)
                robot.forward(timeSleep=0.1, speed=100)
                status = "r"
            elif maxCenter[0] > 650:
                print('Object is on far right')
                robot.turnRight(timeSleep=0.2, speed=100)
                robot.forward(timeSleep=0.1, speed=100)
                status = "fr"
            if maxCenter[1] < 150:
                print('Object is very high')
                status = "vh"
                if status1 == "Yes":
                    print("moving servo down a lot")
                    degrees -= 10
                    servomove()
                    degcheck()
                    
            elif maxCenter[1] < 350:
                print('Object is high')
                status = "h"
                if status1 == "yes":
                    print("moving servo a bit up")
                    degrees -= 5
                    servomove()
                    degcheck()

            elif maxCenter[1] > 450:
                print('Object is low')
                status = "l"
                if status1 == "yes":
                    print("moving servo a bit down")
                    degrees += 5
                    servomove()
                    degcheck()
         
            elif maxCenter[1] > 650:
                print('Object is very low')
                status = "vl"
                if status1 == "yes":
                    print("moving servo down a lot")
                    degrees += 10
                    servomove()
              
            elif maxCenter[0] >= 350 and maxCenter[0] <= 450 and maxCenter[1] >= 350 and maxCenter[1] <= 450 :
                print('Object is in center')
             
     
        else:
            print('Object not in frame')
            status = "not in frame"
            robot.forward(timeSleep=0.2, speed=100)
            robot.turnRight(timeSleep=0.2, speed=100)
            
            
            if degrees == 180 and status == "not in frame":
                robot.forward(timeSleep=0.2, speed=100)
                time.sleep(5)
                degrees = 120
                servomove()
        
    
        cv2.imshow("Masked Frame", maskFrame)
        key = cv2.waitKey(1)
        if key == 27:
            break

        time.sleep(0.05)

    except KeyboardInterrupt:
        print('Ending object tracking')
        break

cap.stop()
cv2.destroyAllWindows()
robot.shutdown()

