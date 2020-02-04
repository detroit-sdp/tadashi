#!/usr/bin/env python
import rospy, pygame
from geometry_msgs.msg import Twist, Pose
from sensor_msgs.msg import LaserScan
from time import time
from math import round

class Turtlebot:
	def __init__(self):
		rospy.init_node('turtlebot', anonymous=True)

		# Publisher to publish movement and turning
		self.movement_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
		
		# Subscriber to pose (location and orientation)
		self.pose_subscriber = rospy.Subscriber('pose', Pose, self.pose_callback)

		# Subscriber to the LaserScan
		self.scan_subscriber = rospy.Subscriber('scan', LaserScan, self.scan_callback)

		# Pose of Turtlebot
		self.pose = Pose()

		def pose_callback(self, data):
			self.pose = data
			self.pose.x = round(self.pose.x, 4)
			self.pose.y = round(self.pose.y, 4)

		def scan_callback(self, data):
			print(data.ranges[0:5])

		def movement(self, controller):
			self.movement_publisher.publish(controller)



if __name__ == '__main__':

