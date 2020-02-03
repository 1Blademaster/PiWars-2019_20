import RPi.GPIO as GPIO
import numpy as np
import time

class Robot():
    
    GPIO.setmode(GPIO.BCM)
    
    #motor 1 ---> o---o <--- motor 2
    #              | |
    #              | |
    #motor 3 ---> o---o <--- motor 4

    motor1f = 23
    motor1b = 24
    motor1e = 4
    motor2f = 17
    motor2b = 27
    motor2e = 22
    motor3f = 16
    motor3b = 20
    motor3e = 21
    motor4f = 14
    motor4b = 15
    motor4e = 18

    motors = np.array([
        [motor1f, motor1b, motor1e], # Motor 1
        [motor2f, motor2b, motor2e], # Motor 2
        [motor3f, motor3b, motor3e],
        [motor4f, motor4b, motor4e],
    ])    

    for i in range(0, len(motors)):
        for j in range(0, len(motors[i])):
            GPIO.setup(int(motors[i, j]), GPIO.OUT)

    pwmMotors = [
        GPIO.PWM(motor1e, 100),
        GPIO.PWM(motor2e, 100),
        GPIO.PWM(motor3e, 100),
        GPIO.PWM(motor4e, 100),
    ]

    for motor in pwmMotors:
        motor.start(0)

    def __init__(self):
        pass
    
    def shutdown(self):
        print('Shutting down the robot')
        for motor in self.pwmMotors:
            motor.stop()
        GPIO.cleanup()

    def forward(self, timeSleep=None, speed=100):
        if timeSleep:
            print('Going forward for {} seconds'.format(timeSleep))
        else:
            print('Going forward forever')
        
        # Turn all motors forward on
        for i in range(0, len(self.motors)): # Loop through all the motors in the array
            GPIO.output(int(self.motors[i, 0]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(speed)

        if timeSleep:
            time.sleep(timeSleep)

            # Turn all motors off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

            print('Stopped going forwards')

    def backward(self, timeSleep=None, speed=100):
        if timeSleep:
            print('Going backward for {} seconds'.format(timeSleep))
        else:
            print('Going backward forever')
        
        # Turn all motors backward on
        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.HIGH)
            GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(speed)

        if timeSleep:
            time.sleep(timeSleep)

            # Turn all motors off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

            print('Stopped going forwards')

    def turnLeft(self, timeSleep=None, speed=100):
        if timeSleep:
            print('Turning left for {} seconds'.format(timeSleep))
        else:
            print('Turning left forever')
        
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
            motor.ChangeDutyCycle(speed)
        
        if timeSleep:
            time.sleep(timeSleep)
            
            # All motors go off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)
            
            print('Stopped turning left')

    def turnRight(self, timeSleep=None, speed=100):
        if timeSleep:
            print('Turning right for {} seconds'.format(timeSleep))
        else:
            print('Turning right forever')
        
        for i in range(0, len(self.motors)):
            if i % 2 == 0: # If motor is divisible by 2, then it is on left side of robot
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.HIGH)
                GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
            else:
                GPIO.output(int(self.motors[i, 0]), GPIO.HIGH)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.HIGH)
        
        for motor in self.pwmMotors:
            motor.ChangeDutyCycle(speed)
            
        if timeSleep:
            time.sleep(timeSleep)
            
            # All motors go off
            for i in range(0, len(self.motors)):
                GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
                GPIO.output(int(self.motors[i, 2]), GPIO.LOW)
            
            print('Stopped turning right')

    def stop(self):

        print('Stopping all motors')

        for i in range(0, len(self.motors)):
            GPIO.output(int(self.motors[i, 0]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 1]), GPIO.LOW)
            GPIO.output(int(self.motors[i, 2]), GPIO.LOW)

        print('All motors stopped')

if __name__ == '__main__':
    robot = Robot()

    robot.turnRight(timeSleep=0.1)
    robot.turnLeft(timeSleep=0.2)

    robot.shutdown()
