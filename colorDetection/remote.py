from robot import Robot
from pynput.keyboard import Key, Listener
import sys
import os

def onPress(key):
	try:
		if key == Key.esc:
			pass
			#sys.exit()

		if key == Key.up:
			r.forward()
			print(' : moving forwards')
		elif key == Key.down:
			r.backward()
			print(' : moving backwards')
		elif key == Key.left:
			r.turnLeft()
			print(' : turning left')
		elif key == Key.right:
			r.turnRight()
			print(' : turning right')
	except Exception as e:
		print('Error: {0}'.format(e))

def onRelease(key):
	r.stop()
	print('stopped moving')

if __name__ == '__main__':
	r = Robot()
	with Listener(on_press=onPress, on_release=onRelease) as listener:
		try:
			listener.join()
		except:
			r.shutdown()
