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

    self.Clock = Clock().SetTick(60)

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

      keys = pygame.key.get_pressed()

      self.Clock.Tick()

    Display.Update()

  def CheckCollisions(self):
    self.x = 0

  def Quit(self):
    pygame.quit()
    quit()