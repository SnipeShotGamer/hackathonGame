import pygame
from Clock import Clock
from Inventory import Inventory
from Config import Config
from Display import Display

pygame.init()

class Game:
  def __init__(self):
    Config.Init()
    Display.Init()

    self.screen = Display.GetDisplay()

    Display.SetCaption(Config.Get("GameSettings")["Caption"])

    self.Clock = Clock().SetTick(60)

    self.Start()

  def Start(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()

      keys = pygame.key.get_pressed()

      Display.Update()
      self.Clock.Tick()

  def Quit(self):
    pygame.quit()
    quit()

game = Game()