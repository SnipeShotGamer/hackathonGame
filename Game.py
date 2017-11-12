import pygame
from Clock import Clock
from Inventory import Inventory
from Config import Config

pygame.init()

class Game:
  def __init__(self):
    Config.Init()

    # TODO move to class
    pygame.display.set_mode()
    w, h = pygame.display.get_surface().get_size()
    self.screen = pygame.display.set_mode((w, h))

    pygame.display.set_caption(Config.Get("GameSettings")["Caption"])

    self.Clock = Clock().SetTick(60)

    self.Start()

  def Start(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()

      keys = pygame.key.get_pressed()

      pygame.display.update()
      self.Clock.Tick()

  def Quit(self):
    pygame.quit()
    quit()

game = Game()