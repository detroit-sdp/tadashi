import movement, pygame, sys, scipy

pygame.init()

screen = pygame.display.set_mode((100,2))
pygame.display.set_caption("Robot control test")

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
			movement.turn(-0.75)
		if keys[pygame.K_RIGHT]:
			movement.turn()
		if keys[pygame.K_UP]:
			movement.move()
		if keys[pygame.K_DOWN]:
			movement.move(-1)
		if not(scipy.any(keys)):
			movement.stop()

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()
	sys.exit()

else:
	movement.stop()