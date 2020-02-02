#Getting colours from pixels on screen
import cv2

cap = cv2.VideoCapture(0) #Set the video source 

while True:
	_, frame = cap.read() #Capture the frame from the video source
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #Convert it to RGB from BGR

	print(rgb[1, 1]) #Print out the RGB value of the pixel (1, 1)

	cv2.imshow("Frame", frame) #Display the video in a GUI

	key = cv2.waitKey(1) #If a key is pressed, close the GUI and end the program
	if key == 27: #27 is ESCAPE
		break

cap.release()
cv2.destroyAllWindows()