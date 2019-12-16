from robot import Robot

def square():
    print('Creating a square')
    for i in range(4):
        robot.forward(timeSleep=2)
        robot.turnRight(timeSleep=1.3)

def circle():
    print('Creating a circle')
    robot.turnRight()

def octagon():
    print('Creating an octagon')
    for i in range(0, 8):
        robot.forward(timeSleep=2)
        robot.turnRight(timeSleep=1)

if __name__ == "__main__":
    robot = Robot()

    square()

    robot.shutdown()
