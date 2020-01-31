#!/usr/bin/env python
import movement, rospy
from time import time

def check_valid_direction(d):
	if d == "forward":
		return 1
	elif d == "back":
		return 2
	elif d == "right":
		return 3
	elif d == "left":
		return 4
	else:
		return 0

def check_valid_speed(speed):
	if speed < 0:
		return False
	elif speed > 2:
		return False
	
	return True

def check_valid_duration(duration):
	if duration <= 0:
		return False
	elif duration > 5:
		answer = raw_input("Warning are you sure you would like to run for " + str(duration) + " seconds? (yes/no):")
		while answer != "yes" and answer != "no":
			answer = raw_input("Please enter yes or no:")
		
		if answer == "yes":
			return True
		elif answer == "no":
			return False
	return True


if __name__ == "__main__":
	rospy.init_node('example_script',anonymous=True)

	while True:
		direction = raw_input("Enter a direction (forward/back/right/left):")

		while check_valid_direction(direction) == 0:
			direction = raw_input("Please enter a valid direction (forward/back/right/left):")

		speed = float(raw_input("Enter a speed (less than 2):"))

		while not(check_valid_speed(speed)):
			speed = float(raw_input("Please enter a valid speed (0<speed<=2):"))

		duration = float(raw_input("Enter a duration (be mindful of surroundings):"))

		while not(check_valid_duration(duration)):
			duration = float(raw_input("Please enter a valid duration (>0):"))

		direction = check_valid_direction(direction)
		start_time = time()

		if (direction == 1):
			while time() < start_time + duration:
				movement.move(speed)
				# movement.scan()
		elif (direction == 2):
			while time() < start_time + duration:
				movement.move(-1*speed)
				# movement.scan()
		elif (direction == 3):
			while time() < start_time + duration:
				movement.turn(speed)
				# movement.scan()
		elif (direction == 4):
			while time() < start_time + duration:
				movement.turn(-1*speed)
				# movement.scan()


		movement.stop()

		answer = raw_input("Continue?")

		while answer != "yes" and answer != "no":
			answer = raw_input("Please enter yes/no:")

		if answer == "no":
			break
else:
	movement.stop()
