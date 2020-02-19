#!/usr/bin/env python
import rospy, pygame, sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from time import time

class Turtlebot:
	def __init__(self):
		rospy.init_node('turtlebot', anonymous=True)

		# Publisher to publish movement and turning
		self.movement_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
		
		# Subscriber to pose (location and orientation)
		self.pose_subscriber = rospy.Subscriber('odom', Odometry, self.pose_callback)

		# Subscriber to the LaserScan
		self.scan_subscriber = rospy.Subscriber('scan', LaserScan, self.scan_callback)

		# Pose of Turtlebot
		self.pose = Odometry()

		# Current forward reading of LaserScan
		self.readings = LaserScan()

		# Rate (refreshes per second in Hz)
		self.rate = rospy.Rate(10)

		# banMove if something in front of bot
		self.banMove = False


	def pose_callback(self, data):
		"""Callback function for pose_subscriber. This updates the pose
		of the Turtlebot using the data from Odometry(). Prints current
		pose as well for debugging."""

		self.pose.pose = data.pose.pose
		# print self.pose.pose

	def scan_callback(self, data):
		"""Callback function for the scan_subscriber. This updates the
		current readings from the LaserScan (indexed from 0 to 360). Prints
		front 5 readings for debugging as well."""

		self.readings.ranges = data.ranges
		
		if self.readings.ranges[0] < 0.5 and self.readings.ranges[0] > 0.1:
			self.banMove = True
		else:
			self.banMove = False


		print self.readings.ranges[0]

	def movement(self, controller):
		self.movement_publisher.publish(controller)



if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((30,30))
	pygame.display.set_caption("Turtlebot Controller")
	clock = pygame.time.Clock()
	carryOn = True

	tb = Turtlebot()

	while carryOn:
		move = Twist()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				carryOn = False

		keys = pygame.key.get_pressed()

		if tb.banMove:
			move.linear.x = 0
			move.angular.z = 0
		elif keys[pygame.K_LEFT]:
			move.linear.x = 0
			move.angular.z = 0.75
		elif keys[pygame.K_RIGHT]:
			move.linear.x = 0
			move.angular.z = -0.75
		elif keys[pygame.K_UP]:
			move.linear.x = 1
			move.angular.z = 0
		elif keys[pygame.K_DOWN]:
			move.linear.x = -1
			move.angular.z = 0
		elif keys[pygame.K_q]:
			carryOn = False
			move.linear.x = 0
			move.angular.z = 0
		else:
			move.linear.x = 0
			move.angular.z = 0

		tb.movement(move)
		tb.rate.sleep()		# sleep

		clock.tick(30)

	pygame.quit()
	sys.exit()
