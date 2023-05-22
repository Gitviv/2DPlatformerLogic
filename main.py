import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((sizes["SCREEN_WIDTH"],sizes["SCREEN_HEIGHT"]))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

level = Level()

while True:
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			break
	
	screen.fill(BG_COLOR)
	level.run()
	pygame.display.flip()

	# drawing logic
	pygame.display.update()
	clock.tick(60)