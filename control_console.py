import movement
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
	if speed <= 0:
		return False
	elif speed > 2:
		return False
	
	return True

def check_valid_duration(duration):
	if duration <= 0:
		return False
	elif duration > 5:
		answer = input("Warning are you sure you would like to run for " + str(duration) + " seconds? (yes/no):")
		while answer != "yes" and answer != "no":
			answer = input("Please enter yes or no:")
		
		if answer == "yes":
			return True
		elif answer == "no":
			return False
	return True


if __name__ == "__main__":
	while True:
		direction = input("Enter a direction (forward/back/right/left):")

		while check_valid_direction(direction) == 0:
			direction = input("Please enter a valid direction (forward/back/right/left):")

		speed = float(input("Enter a speed (less than 2):"))

		while not(check_valid_speed(speed)):
			speed = float(input("Please enter a valid speed (0<speed<=2):"))

		duration = float(input("Enter a duration (be mindful of surroundings):"))

		while not(check_valid_duration(duration)):
			duration = float(input("Please enter a valid duration (>0):"))

		direction = check_valid_direction(direction)
		start_time = time()

		if (direction == 1):
			while time() < start_time + duration:
				movement.move(speed)
				movemnet.scan()
		elif (direction == 2):
			while time() < start_time + duration:
				movement.move(-1*speed)
				movemnet.scan()
		elif (direction == 3):
			while time() < start_time + duration:
				movement.turn(speed)
				movemnet.scan()
		elif (direction == 4):
			while time() < start_time + duration:
				movement.turn(-1*speed)
				movemnet.scan()


		movement.stop()

		answer = input("Continue?")

		if answer == "no" or answer == "No" or answer == "nO" or answer == "NO" or answer == "n" or answer == "N":
			break
else:
	movement.stop()