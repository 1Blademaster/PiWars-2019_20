import RPi.GPIO as GPIO
import numpy as np
import time

class Robot():
    
    GPIO.setmode(GPIO.BCM)
    
    #motor 0 ---> o---o <--- motor 1
    #              | |
    #              | |
    #motor 2 ---> o---o <--- motor 3

    motor1f = 12 # Input Pin yellow
    motor1b = 7 # Input Pin white
    motor1e = 16 # Enable Pin blue
    motor2f = 20 # Input Pin white
    motor2b = 21 # Input Pin grey
    motor2e = 8 # Enable Pin purple

    motors = np.array([
        [motor1f, motor1b, motor1e],
        [motor2f, motor2b, motor2e],
    ])

    for i in range(0, len(motors)):
        for j in range(0, len(motors[i])):
            GPIO.setup(int(motors[i, j]), GPIO.OUT)

    def __init__(self):
        pass
    
    def shutdown(self):
        print('Shutting down the robot')
        GPIO.cleanup()

    def forward(self, timeSleep):
        print(f'Going forward for {timeSleep} seconds')
        
        # Turn all motors forward on
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)

        time.sleep(int(timeSleep))

        # Turn all motors off
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

        print('Stopped going forwards')

    def backward(self, timeSleep):
        print(f'Going forward for {timeSleep} seconds')
        
        # Turn all motors backward on
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)

        time.sleep(int(timeSleep))

        # Turn all motors off
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

        print('Stopped going forwards')

    def turnRight(self, timeSleep):
        print(f'Turning right for {timeSleep} seconds')
        
        # Motor 0 go forwards
        GPIO.output(int(self.motors[0, 0]), GPIO.HIGH)
        GPIO.output(int(self.motors[0, 1]), GPIO.LOW)
        GPIO.output(int(self.motors[0, 2]), GPIO.HIGH)
        
        # Motor 1 go backwards
        GPIO.output(int(self.motors[1, 0]), GPIO.LOW)
        GPIO.output(int(self.motors[1, 1]), GPIO.HIGH)
        GPIO.output(int(self.motors[1, 2]), GPIO.HIGH)
        
        time.sleep(int(timeSleep))
        
        # All motors go off
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)
        
        print('Stopped turning right')

    def turnLeft(self, timeSleep):
        
        print(f'Turning left for {timeSleep} seconds')
        
        # Motor 0 go backwards
        GPIO.output(int(self.motors[0, 0]), GPIO.LOW)
        GPIO.output(int(self.motors[0, 1]), GPIO.HIGH)
        GPIO.output(int(self.motors[0, 2]), GPIO.HIGH)
        
        # Motor 1 go forwards
        GPIO.output(int(self.motors[1, 0]), GPIO.HIGH)
        GPIO.output(int(self.motors[1, 1]), GPIO.LOW)
        GPIO.output(int(self.motors[1, 2]), GPIO.HIGH)
        
        time.sleep(int(timeSleep))
        
        # All motors go off
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)
        
        print('Stopped turning left')

robot = Robot()

robot.turnRight(3)
robot.turnLeft(3)

robot.shutdown()
