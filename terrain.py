import pygame 
from settings import *
import random

enemies = [
	'graphics/players/Enemy.PNG',
	'graphics/players/Player.PNG'
]

class Tile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/terrain/minecraft block 2d.jfif').convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"], sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)

class Palm(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/terrain/palm.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"], sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)

class Cloud(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/terrain/cloud.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"] * 3, sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)

class FakeTile(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/terrain/fake_block.jfif').convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"], sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)
	
class Lava(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/terrain/lava.jfif').convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"], sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)

class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos,groups):
		super().__init__(groups)
		self.image = pygame.image.load(random.choice(enemies)).convert_alpha()
		self.image = pygame.transform.scale(self.image, (sizes["TILE_SIZE"], sizes["TILE_SIZE"]))
		self.rect = self.image.get_rect(topleft = pos)