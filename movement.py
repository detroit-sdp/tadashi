#!/usr/bin/env python
# import rospy
# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan
from time import time
import pygame, sys

pygame.init()

screen = pygame.display.set_mode((100,2))
pygame.display.set_caption("My First Game")

# def laser_scan_callback(data):
# 	print data.ranges

# def read_laser_scan_data():
# 	rospy.Subscriber('scan', LaserScan, laser_scan_callback)

def move(speed=1):
	# pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	# mc = Twist()
	# mc.linear.x = speed
	# mc.angular.z = 0
	# pub.publish(mc)
	if (speed == 1):
		print("Moving forward")
	else:
		print("Moving backwards")

def stop():
	# pub = rospy.Publisher('cmd_stop', Twist, queue_size = 10)
	# mc = Twist()
	# mc.linear.x = 0
	# mc.angular.z = 0
	# pub.publish(mc)
	return 1

def turn(speed=0.75):
	# pub = rospy.Publisher('cmd_trn', Twist, queue_size = 10)
	# mc = Twist()
	# mc.linear.x = 0
	# mc.angular.z = speed
	# pub.publish(mc)
	if speed == 0.75:
		print("Turning right")
	else:
		print("Turning left")


if __name__ == '__main__':
	clock = pygame.time.Clock()
	carryOn = True

	while carryOn:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				carryOn = False
			elif event.type==pygame.KEYDOWN:
				if event.key==pygame.K_q:
					carryOn=False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			turn(-0.75)
		if keys[pygame.K_RIGHT]:
			turn()
		if keys[pygame.K_UP]:
			move()
		if keys[pygame.K_DOWN]:
			move(-1)

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()
	sys.exit()

else:
	stop()