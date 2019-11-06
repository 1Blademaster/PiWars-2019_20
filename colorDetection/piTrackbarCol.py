import cv2
import numpy as np
import time
from imutils.video import VideoStream
import imutils

cap = VideoStream(src=0, usePiCamera=True, framerate=32).start()

time.sleep(0.5)

def nothing(x):
    pass

hh='Hue High'
hl='Hue Low'
sh='Saturation High'
sl='Saturation Low'
vh='Value High'
vl='Value Low'
wnd='Colorbars'

cv2.namedWindow(wnd, flags = cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar(hl, wnd, 0, 179, nothing)
cv2.createTrackbar(hh, wnd, 0, 179, nothing)
cv2.createTrackbar(sl, wnd, 0, 255, nothing)
cv2.createTrackbar(sh, wnd, 0, 255, nothing)
cv2.createTrackbar(vl, wnd, 0, 255, nothing)
cv2.createTrackbar(vh, wnd, 0, 255, nothing)

while True:
    frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hul = cv2.getTrackbarPos(hl, wnd)
    huh = cv2.getTrackbarPos(hh, wnd)
    sal = cv2.getTrackbarPos(sl, wnd)
    sah = cv2.getTrackbarPos(sh, wnd)
    val = cv2.getTrackbarPos(vl, wnd)
    vah = cv2.getTrackbarPos(vh, wnd)

    hsvlow = np.array([hul, sal, val])
    hsvhigh = np.array([huh, sah, vah])

    mask = cv2.inRange(hsv, hsvlow, hsvhigh)
    screen = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow(wnd, screen)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.stop()
cv2.destroyAllWindows()
