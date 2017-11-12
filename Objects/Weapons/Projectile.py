import pygame
import GameObject

class Projectile(GameObject, pygame.sprite.Sprite):
	def __init__(self, pos, vel, size, texture, damage):
		self.vel = vel
		self.pos = pos
		self.size = size
		self.texture = texture
		self.damage = damage

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