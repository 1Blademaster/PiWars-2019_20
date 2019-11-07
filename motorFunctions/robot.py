import numpy as np
import time

class Robot():

    motor1f = 14  # Input Pin yellow
    motor1b = 6   # Input Pin white
    motor1e = 10   # Enable Pin blue

    motors = np.array([
        [motor1f, motor1b, motor1e],
    ])

    for i in range(0, len(motors)):
        for j in range(0, len(motors[i])):
            GPIO.setup(motor[i, j], GPIO.OUT)

    def __init__(self):
        pass

    def forward(self, time):
        print(f'going forward for {time} seconds')

        for i in range(0, len(motors)):
            GPIO.output(self.motors[i, 0], GPIO.HIGH)
            GPIO.output(self.motors[i, 1], GPIO.LOW)
            GPIO.output(self.motors[i, 2], GPIO.HIGH)

        time.sleep(time)

        for i in range(0, len(motors)):
            GPIO.output(self.motors[i, 0], GPIO.LOW)
            GPIO.output(self.motors[i, 1], GPIO.LOW)
            GPIO.output(self.motors[i, 2], GPIO.LOW)

        print('stopped going forwards')

    def backward(self):
        pass

    def turnRight(self):
        pass

    def turnLeft(self):
        pass
