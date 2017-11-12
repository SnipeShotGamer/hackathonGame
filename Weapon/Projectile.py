import pygame
from EventEmitter import EventEmitter
from EventWatcher import EventWatcher

class Projectile(EventWatcher, pygame.sprite.Sprite):
	def __init__(self, pos, vel, size, texture):
		self.vel = vel
		self.pos = pos
		self.size = size
		self.texture = texture

	def Draw(self):
		pygame.draw.rect(self.texture, (255,255,255), [self.pos[0], self.pos[1], self.size, self.size])

	def Update(self):
		self.pos[0] + self.vel[0]
		self.pos[1] - self.vel[1]

	def Collides(self, collideObj):
		if(instanceof(collideObj, Player)):
			self.Emit("delete")
		else if(instanceof(collideObj, WorldObject)):
			self.Emit("delete")