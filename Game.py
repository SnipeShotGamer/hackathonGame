import pygame

from Clock import Clock
from Inventory import Inventory
from Config import Config
from Display import Display
from Objects import GameObject
from Contracts import InstanceOf

class Game:
  def __init__(self):
    pygame.init()

    Config.Init()
    Display.Init()

    self.__screen = Display.GetDisplay()

    Display.SetCaption(Config.Get("GameSettings")["Caption"])

    self.Clock = Clock().SetTick(int(Config.Get("GameSettings")["Fps"]))

    self.__gameObjects = []

  def AddGameObjects(self, *objects):
    for obj in objects:
      InstanceOf(obj, GameObject.GameObject)
      self.__gameObjects.append(obj)

  def Start(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()

      self.CheckCollisions()

      keys = pygame.key.get_pressed()

      self.Clock.Tick()

      Display.Update()

  def CheckCollisions(self):
    objs = self.__gameObjects

    for firstObject in range(len(objs)):
      for secondObject in range(i, len(objs)):
        collisionState = CollisionState()

        if (objs[firstObject].x > objs[secondObject].x and objs[firstObject].x < objs[secondObject].x + objs[secondObject].width):
          collisionState.Left = True
        elif (objs[firstObject].x + objs[firstObject].width > objs[secondObject].x and objs[firstObject].x + objs[firstObject].width < objs[secondObject].x + objs[secondObject].width):
          collisionState.Right = True

        # We must not be colliding on the left or right
        if (collisionState.Left or collisionState.Right):
          continue

        if (objs[firstObject].y > objs[secondObject].y and objs[secondObject].y < objs[secondObject].y + objs[secondObject].height):
          collisionState.Top = True
        elif (objs[firstObject].y + objs[firstObject].height > objs[secondObject].y and objs[firstObject].y + objs[firstObject].height < objs[secondObject].y + objs[secondObject].height):
          collisionState.Bottom = True

        # We must not be colliding on the top or bottom
        if (collisionState.Top or collisionState.Bottom):
          continue

        objs[firstObject].Colliding(objs[secondObject], collisionState)

  def Quit(self):
    pygame.quit()
    quit()

Game().Start()