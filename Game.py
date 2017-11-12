import pygame

pygame.init()

class Game:
  def __init__(self):
    # TODO move to class
    pygame.display.set_mode()
    w, h = pygame.display.get_surface().get_size()
    self.screen = pygame.display.set_mode((w, h))

    # TODO get from config (probably within displaying class)
    pygame.display.set_caption("")

    # TODO move to class
    self.clock = pygame.time.Clock()

    self.Start()

  def Start(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()

      keys = pygame.key.get_pressed()

      pygame.display.update()
      self.clock.tick(60)

  def Quit(self):
    pygame.quit()
    quit()

game = Game()