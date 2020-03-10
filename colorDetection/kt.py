from getkey import getkey
from robot import Robot

r = Robot()

while True:
	k = getkey()
	if k == 'w':
		r.forward()
	elif k == 's':
		r.backward()
	elif k == 'a':
		r.turnLeft()
	elif k == 'd':
		r.turnRight()
	elif k == 'q':
		r.stop()
		break

r.shutdown()
