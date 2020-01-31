#!/usr/bin/env python
import movement, pygame, sys, rospy

pygame.init()

screen = pygame.display.set_mode((100,2))
pygame.display.set_caption("Robot control test")

if __name__ == '__main__':
	rospy.init_node('example_script',anonymous=True)
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
			movement.turn()
		elif keys[pygame.K_RIGHT]:
			movement.turn(-0.75)
		elif keys[pygame.K_UP]:
			movement.move()
		elif keys[pygame.K_DOWN]:
			movement.move(-1)
		else:
			movement.stop()

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()
	sys.exit()

else:
	movement.stop()
