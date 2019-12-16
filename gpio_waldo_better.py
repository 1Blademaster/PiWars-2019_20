import RPi.GPIO as GPIO 

from time import sleep 

  
#front axle 1 is left, 2 is right 
GPIO.setmode(GPIO.BCM) 

  

Motor1f = 2   # Input Pin yellow 

Motor1b = 3   # Input Pin white

Motor1e = 4   # Enable Pin bl
  

GPIO.setup(Motor1f,GPIO.OUT) 

GPIO.setup(Motor1b,GPIO.OUT) 

GPIO.setup(Motor1e,GPIO.OUT) 

print("FORWARD M1")

GPIO.output(Motor1f,1) 

GPIO.output(Motor1b,0) 

GPIO.output(Motor1e,1)

sleep(7.5)

GPIO.output(Motor1f, 0)
GPIO.output(Motor1e, 0)
GPIO.output(Motor1b, 0)

print('off')

GPIO.cleanup()



