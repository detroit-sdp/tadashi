#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def laser_scan_callback(data):
	if data.ranges[0] < 0.5 and data.ranges[0] > 0.1:
		print "Move out the way"
	else:
		print "Free to move"

	print(data.ranges[0])

def read_laser_scan_data():
	rospy.Subscriber('scan', LaserScan, laser_scan_callback)

def move(speed=1):
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	mc = Twist()
	mc.linear.x = speed
	mc.angular.z = 0
	pub.publish(mc)
	# if (speed > 0):
	# 	print("Moving forward")
	# else:
	# 	print("Moving backwards")

def turn(speed=0.75):
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	mc = Twist()
	mc.linear.x = 0
	mc.angular.z = speed
	pub.publish(mc)
	# if speed == 0.75:
	# 	print("Turning right")
	# else:
	# 	print("Turning left")

def stop():
	pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
	mc = Twist()
	mc.linear.x = 0
	mc.angular.z = 0
	pub.publish(mc)
	# print("Stopped")

def scan(ranges):
	if len(ranges) == 720:
		print("True")
