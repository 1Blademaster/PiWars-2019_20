import RPi.GPIO as GPIO 

from time import sleep 

  
#front axle 1 is left, 2 is right 
GPIO.setmode(GPIO.BCM) 

  

Motor1f = 12   # Input Pin yellow 

Motor1b = 7   # Input Pin white

Motor1e = 16   # Enable Pin blue

Motor2f = 20   # input white

Motor2b = 21   # input grey

Motor2e = 8    # enable purpel

  

GPIO.setup(Motor1f,GPIO.OUT) 

GPIO.setup(Motor1b,GPIO.OUT) 

GPIO.setup(Motor1e,GPIO.OUT) 

GPIO.setup(Motor2f,GPIO.OUT) 

GPIO.setup(Motor2b,GPIO.OUT) 

GPIO.setup(Motor2e,GPIO.OUT)

GPIO.output(Motor1f,GPIO.LOW)
GPIO.output(Motor1e,GPIO.LOW)

print("FORWARD M1 ,M2")

GPIO.output(Motor2f,GPIO.HIGH) 

GPIO.output(Motor2b,GPIO.LOW) 

GPIO.output(Motor2e,GPIO.HIGH)

#GPIO.output(Motor1f,GPIO.HIGH) 

#GPIO.output(Motor1b,GPIO.LOW) 

#GPIO.output(Motor1e,GPIO.HIGH)

sleep(3)

print ("FORWARD MOTION m1")

GPIO.output(Motor2f,GPIO.LOW) 

GPIO.output(Motor2b,GPIO.LOW) 

GPIO.output(Motor2e,GPIO.LOW)

GPIO.output(Motor1f,GPIO.HIGH) 

GPIO.output(Motor1b,GPIO.LOW) 

GPIO.output(Motor1e,GPIO.HIGH)


  

sleep(3) 

  

print ("BACKWARD MOTION m1")
GPIO.output(Motor2f,GPIO.LOW) 

GPIO.output(Motor2b,GPIO.LOW) 

GPIO.output(Motor2e,GPIO.LOW)


GPIO.output(Motor1f,GPIO.LOW) 

GPIO.output(Motor1b,GPIO.HIGH) 

GPIO.output(Motor1e,GPIO.HIGH) 

  

sleep(3) 

  

print ("STOP m1") 

GPIO.output(Motor1e,GPIO.LOW)

sleep(3)

print ("FORWARD MOTION m2")

GPIO.output(Motor2f,GPIO.HIGH) 

GPIO.output(Motor2b,GPIO.LOW) 

GPIO.output(Motor2e,GPIO.HIGH)


  

sleep(3) 

  

print ("BACKWARD MOTION m2")

GPIO.output(Motor2f,GPIO.LOW) 

GPIO.output(Motor2b,GPIO.HIGH) 

GPIO.output(Motor2e,GPIO.HIGH)

sleep(3)
print ("STOP m2") 
print ("STOP both")

print("Wait")
sleep(2)

print("left turn")

GPIO.output(Motor1f,GPIO.LOW) 

GPIO.output(Motor1b,GPIO.HIGH) 

GPIO.output(Motor1e,GPIO.HIGH)

GPIO.output(Motor2f,GPIO.HIGH) 

GPIO.output(Motor2b,GPIO.LOW) 

GPIO.output(Motor2e,GPIO.HIGH)

sleep(3)



    

GPIO.cleanup()



