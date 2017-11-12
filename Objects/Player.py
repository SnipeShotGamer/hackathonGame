import pygame
from Objects import GameObject
from Inventory import Inventory
from Config import Config
from Display import Display

class PlayerStats():
	def __init__(self, health, level):
		self.__health = health
		self.__level = level

	def Damage(self, hp):
		self.__health -= hp

	def Heal(self, hp):
		self.__health += hp

	def HealAll(self):
		self.__health = 100

class Player(GameObject.GameObject):
	def __init__(self, x, y, width, height, stats):
		super().__init__(x, y, width, height)
		self.stats = stats

class PlayerO(Player):
	UP = 0
	RIGHT = 1
	DOWN = 2
	LEFT = 3

	def __init__(self, pos, size, texture, stats, multiplier = 1, facing = UP):
		super().__init__(pos[0], pos[1], size[0], size[1], stats)

		self.pos = pos
		self.size = size
		self.texture = texture
		self.facing = facing
		self.multiplier = multiplier

	def CanMove(self, gameState):
		return not Inventory.Opened() and gameState.GetGameState() == GameState.PLAYING

	def Update(self):
		keys = pygame.key.get_pressed()

		for key in keys:
			if (self.CanMove()):
				if (key == pygame.K_w):
					self.pos[1] -= 5 * self.multiplier
					self.facing = UP

				if(key == pygame.K_s):
					self.pos[1] += 5 * self.multiplier
					self.facing = DOWN

				if(key == pygame.K_a):
					self.pos[0] -= 5 * self.multiplier
					self.facing = LEFT

				if(key == pygame.K_d):
					self.pos[0] += 5 * self.multiplier
					self.facing = RIGHT

class PlayerS(Player):
	Config.Init()

	SPRITE_WIDTH = 16
	SPRITE_HEIGHT = 16
	SPRITE_SHEET_PATH = Config.Get("ResourcePath") 
	SPRITE_SHEET = pygame.image.load(SPRITE_SHEET_PATH)
	SPRITE_SHEET.set_clip(pygame.Rect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))

	MAX_VELOCITY_WALKING = 20
	MAX_VELOCITY_RUNNING = 30

	RIGHT = 0
	LEFT = 1

	def __init__(self, pos, vel, size, stats, multiplier = 1, facing = RIGHT):
		super().__init__(pos[0], pos[1], size[0], size[1], stats)

		Display.Init()

		self.pos = pos
		self.vel = vel
		self.size = size
		self.facing = facing
		self.maxVel = PlayerS.MAX_VELOCITY_WALKING

		self.multiplier = multiplier

		self.landed = True

	def Update(self):
		keys = pygame.key.get_pressed()

		for key in keys:
			if (key == pygame.key.K_SPACE):
				if (self.landed):
					self.vel[1] += 20 * self.multiplier

			if(key == pygame.key.K_a):
				self.vel[0] -= 5 * self.multiplier

			if(key == pygame.key.K_d):
				self.vel[0] += 5 * self.multiplier

			if(key == pygame.key.K_LSHIFT):
				self.maxVel = MAX_VELOCITY_RUNNING

		if (self.vel[0] < 0):
			self.facing = LEFT

		if (self.vel[0] > 0):
			self.facing = RIGHT

	def Draw(self):		
		display = Display.GetDisplay()
		player = PlayerS.SPRITE_SHEET.subsurface(PlayerS.SPRITE_SHEET.get_clip())
		display.blit(player, (50, 50))
		
	def Collides(self, collideObj, collisionState):
		if(instanceof(collideObj, WorldObject)):
			self.grounded = true
		if(instanceof(collideObj, Projectile)):
			self.health -= collideObj.Damage
		if(instanceof(collideObj, MeleeWeapon)):
			self.health -= collideObj.Damage
