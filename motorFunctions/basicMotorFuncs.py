import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1f = 14  # Input Pin yellow
Motor1b = 6   # Input Pin white
Motor1e = 10   # Enable Pin blue

GPIO.setup(Motor1f, GPIO.OUT)
GPIO.setup(Motor1b, GPIO.OUT)
GPIO.setup(Motor1e, GPIO.OUT)

print ("FORWARD MOTION m1")

GPIO.output(Motor1f, GPIO.HIGH)
GPIO.output(Motor1b, GPIO.LOW)
GPIO.output(Motor1e, GPIO.HIGH)

sleep(3)

print ("BACKWARD MOTION m1")

GPIO.output(Motor1f, GPIO.LOW)
GPIO.output(Motor1b, GPIO.HIGH)
GPIO.output(Motor1e, GPIO.HIGH)

sleep(3)

print ("STOP m1")

GPIO.output(Motor1e,GPIO.LOW)

sleep(3)

print ("STOP both")

GPIO.cleanup()
