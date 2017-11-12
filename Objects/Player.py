import pygame
import GameObject

class Player(Sprite, GameObject):

class PlayerO(Player):
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3
	def __init__(self, pos, size, texture, health, facing = UP):
		self.pos = pos
		self.size = size
		self.texture = texture
		self.health = health
		self.facing = facing

	def Update(self):
		keys = pygame.key.get_pressed()
		for key in keys:
			if(key == pygame.key.K_w):
				pos[1] -= 5
				self.facing = UP

			if(key == pygame.key.K_a):
				pos[0] -= 5
				self.facing = LEFT

			if(key == pygame.key.K_s):
				pos[1] += 5
				self.facing = DOWN

			if(key == pygame.key.K_d):
				pos[0] += 5
				self.facing = RIGHT

	def Draw(self):


class PlayerS(Player):
	RIGHT = 0
	LEFT = 1

	def __init__(self, pos, vel, size, texture, health, facing = RIGHT):
		self.pos = pos
		self.vel = vel
		self.size = size
		self.texture = texture
		self.facing = facing
		self.health = health
		self.acc = (0, -2)
		self.maxVel = 20
		self.keyPressedX = False
		self.grounded = True
		self.moveLeft = True
		self.moveRight = True

	def Update(self):
		keys = pygame.key.get_pressed()

		if(pygame.key.K_a in keys and pygame.key.K_d in keys):
			self.keyPressedX = False

		for key in keys:
			if(key == pygame.key.K_SPACE):
				if(grounded):
					self.vel[1] += 20

			if(key == pygame.key.K_a):
				self.vel[0] -= 5

			if(key == pygame.key.K_d):
				self.vel[0] += 5

			if(key == pygame.key.K_LCTRL):
				self.size[1] = 30
				self.maxVel = 5
				#TODO: change sprite to crouching sprite

			if(key == pygame.key.K_LSHIFT):
				self.maxVel = 30

		if(self.vel[0] < 0):
			self.facing = LEFT
		if(self.vel[0] > 0):
			self.facing = RIGHT
		if(!self.keyPressedX):
			if(self.vel[0] > 20):
				self.acc[0] = -2
			else:
				self.vel[0] = 0

		if(abs(self.acc[0]) > abs(self.vel[0])):
			self.vel[0] = 0
		else:
			self.vel[0] += self.acc[0]

		if(!grounded):
			if(abs(acc[1]) > abs(vel[1])):
				self.vel[1] = 0
			else:
				self.vel[1] += self.acc[1]

	def Draw(self):
		
	def Collides(self, collideObj):
		if(instanceof(collideObj, WorldObject)):
			self.grounded = true
		if(instanceof(collideObj, Projectile)):
			self.health -= collideObj.Damage
		if(instanceof(collideObj, MeleeWeapon)):
			self.health -= collideObj.Damage
