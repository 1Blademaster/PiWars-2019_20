#https://stackoverflow.com/questions/31460267/python-opencv-color-tracking/31465462#31465462

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
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    col = c.red

    # hue, saturation, value
    lower_col_0 = np.array([col[0, 0], col[0, 1], col[0, 2]])
    upper_col_0 = np.array([col[1, 0], col[1, 1], col[1, 2]])
    lower_col_1 = np.array([0, 0, 0])
    upper_col_1 = np.array([0, 0, 0])

    mask_0 = cv2.inRange(hsv, lower_col_0 , upper_col_0)
    mask_0 = cv2.erode(mask_0, None, iterations=2)
    
    mask_0 = cv2.dilate(mask_0, None, iterations=2)

    mask_1 = cv2.inRange(hsv, lower_col_1 , upper_col_1 )
    mask_1 = cv2.erode(mask_1, None, iterations=2)
    mask_1 = cv2.dilate(mask_1, None, iterations=2)

    masks = cv2.bitwise_or(mask_0, mask_1)
    mask = cv2.bitwise_or(frame, frame, mask=mask_0)

    if np.all(frame[1, 1] == [255, 255, 253]):
        print('hi')

    cv2.imshow("Frame", frame)
    cv2.imshow("Masked Frame", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.stop()
cv2.destroyAllWindows()
