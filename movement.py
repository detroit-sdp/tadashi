#!/usr/bin/env python
# import rospy
# from geometry_msgs.msg import Twist
# from sensor_msgs.msg import LaserScan

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
	print("Stopped")

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
