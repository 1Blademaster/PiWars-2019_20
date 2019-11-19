from robot import robot

def square():
    print('Creating a square')
    for i in range(0, 4):
        robot.foward(timeSleep=3)
        robot.turnRight(timeSleep=5)

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

    octagon() # Draws an octagon