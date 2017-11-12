import pygame
from EventEmitter import EventEmitter
from EventWatcher import EventWatcher

class Player(Sprite, EventWatcher, EventEmitter):

class PlayerO(Player):

class PlayerS(Player):
	RIGHT = 0
	LEFT = 1

	def __init__(self, pos, vel, size, texture, facing = RIGHT):
		self.pos = pos
		self.vel = vel
		self.size = size
		self.texture = texture
		self.facing = facing

	def Update(self):
		if(vel[0] < 0):
			facing = LEFT
		if(vel[0] > 0):
			facing = RIGHT

	def Draw(self):

	def KeyDown(self, key):
		if(key == pygame.key.K_SPACE):
			vel[1] += 20

		if(key == pygame.key.K_a):
			vel[0] -= 5

		if(key == pygame.key.K_d):
			vel[0] += 5

		if(key == pygame.key.K_LCTRL):

		if(key == pygame.key.K_LSHIFT):

	def Collides(self, collideObj):