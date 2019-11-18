import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor1f = 12 # Input Pin yellow
motor1b = 7 # Input Pin white
motor1e = 16 # Enable Pin blue

GPIO.setup(motor1f, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)
GPIO.setup(motor1e, GPIO.OUT)

pwm = GPIO.PWM(motor1e, 100)
pwm.start(0)

print('Starting motor fowards at 25% speed')

GPIO.output(motor1f, True)
GPIO.output(motor1b, False)
pwm.ChangeDutyCycle(25)
GPIO.output(motor1e, True)

time.sleep(2)

print('Starting motor backwards at 75% speed')

GPIO.output(motor1f, False)
GPIO.output(motor1b, True)
pwm.ChangeDutyCycle(75)
GPIO.output(motor1e, True)

time.sleep(2)

print('Stopping motor')

GPIO.output(motor1f, False)
GPIO.output(motor1b, False)
GPIO.output(motor1e, False)

pwm.stop()
GPIO.cleanup()