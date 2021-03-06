import RPi.GPIO as GPIO
import numpy as np
import time

class Robot():
    
    GPIO.setmode(GPIO.BCM)
    
    #motor 1 ---> o---o <--- motor 2
    #              | |
    #              | |
    #motor 3 ---> o---o <--- motor 4

    motor1f = 12 # Input Pin yellow
    motor1b = 7 # Input Pin white
    motor1e = 16 # Enable Pin blue
    motor2f = 20 # Input Pin white
    motor2b = 21 # Input Pin grey
    motor2e = 8 # Enable Pin purple

    isRunning = False

    motors = np.array([
        [motor1f, motor1b, motor1e], # Motor 1
        [motor2f, motor2b, motor2e], # Motor 2
    ])

    for i in range(0, len(motors)):
        for j in range(0, len(motors[i])):
            GPIO.setup(int(motors[i, j]), GPIO.OUT)
        
    pwmMotors = [
        GPIO.PWM(motor1e, 100),
        GPIO.PWM(motor2e, 100),
    ]

    for motor in pwmMotors:
        motor.start(0)

    def __init__(self):
        pass
    
    def shutdown(self):
        if self.isRunning:
            print('Cannot shutdown, there is something running')
        else:
            print('Shutting down the robot')
            for motor in self.pwmMotors:
                motor.stop()
            GPIO.cleanup()

    def forward(self, timeSleep=None, speed=100):
        print('Going forward for {timeSleep} seconds') # F string to make formatting easy
        
        # Turn all motors forward on
        for i in range(0, len(self.motors)): # Loop through all the motors in the array
            GPIO.output(int(self.motors[i, 0]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(speed)

        self.isRunning = True

        if timeSleep:
            time.sleep(int(timeSleep))

            # Turn all motors off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

            self.isRunning = False

            print('Stopped going forwards')


    def backward(self, timeSleep=None, speed=100):
        print('Going forward for {timeSleep} seconds')
        
        # Turn all motors backward on
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(speed)

        self.isRunning = True

        if timeSleep:
            time.sleep(int(timeSleep))

            # Turn all motors off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

            self.isRunning = False
            
            print('Stopped going forwards')

    def turnRight(self, timeSleep=None):
        print('Turning right for {timeSleep} seconds')
        
        for i in range(0, len(self.motors)):
            if i % 2 == 0: # If motor is divisible by 2, then it is on left side of robot
                GPIO.output(int(self.motors[i, 0]), GPIO.HIGH)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
            else:
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.HIGH)
                GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)     
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(100)

        self.isRunning = True
                
        if timeSleep:
            time.sleep(int(timeSleep))
            
            # All motors go off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

            self.isRunning = False
            
            print('Stopped turning right')

    def turnLeft(self, timeSleep=None):
        
        print('Turning left for {timeSleep} seconds')
        
        for i in range(0, len(self.motors)):
            if i % 2 == 0: # If motor is divisible by 2, then it is on left side of robot
                GPIO.output(int(self.motors[0, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[0, 1]), GPIO.HIGH)
                GPIO.output(int(self.motors[0, 2]), GPIO.HIGH)
            else:
                GPIO.output(int(self.motors[1, 0]), GPIO.HIGH)
                GPIO.output(int(self.motors[1, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[1, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(100)
            
        if timeSleep:
            time.sleep(int(timeSleep))
            
            # All motors go off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)
            
            print('Stopped turning left')

    def stop(self):

        print('Stopping all motors')

        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

        self.isRunning = False

        print('All motors stopped')

if __name__ == '__main__':
    robot = Robot()

    robot.forward() # Moves the robot forwards for 5 seconds at 100% speed
    robot.shutdown()
    print('h')
