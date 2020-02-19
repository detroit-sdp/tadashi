#!/usr/bin/env python
import movement, pygame, sys
from rospy import init_node

pygame.init()

screen = pygame.display.set_mode((100,2))
pygame.display.set_caption("Robot control test")

if __name__ == '__main__':
	init_node('example_script',anonymous=True)
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
			try:
				movement.read_laser_scan_data()
				movement.turn()
			except rospy.ROSInterruptException:
				pass
		elif keys[pygame.K_RIGHT]:
			try:
				movement.read_laser_scan_data()
				movement.turn(-0.75)
			except rospy.ROSInterruptException:
				pass
		elif keys[pygame.K_UP]:
			try:
				movement.read_laser_scan_data()
				movement.move()
			except rospy.ROSInterruptException:
				pass
		elif keys[pygame.K_DOWN]:
			try:
				movement.read_laser_scan_data()
				movement.move(-1)
			except rospy.ROSInterruptException:
				pass
		else:
			movement.stop()

		clock.tick(25)

	pygame.quit()
	sys.exit()

else:
	movement.stop()
