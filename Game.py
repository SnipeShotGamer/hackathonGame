import pygame
from EventEmitter import EventEmitter

class Game:
  def __init__(self, _ee, _ew):
    emitter = EventEmitter.EventEmitter(None, None)

    pygame.init()

    # TODO move to class
    pygame.display.set_mode()
    w, h = pygame.display.get_surface().get_size()
    pygame.display.set_mode((w, h))

    # TODO get from config (probably within displaying class)
    pygame.display.set_caption("")

    # TODO move to class
    self.clock = pygame.time.Clock()

    self._eventEmitter = _ee
    self._eventWatcher = _ew

    self.Start()

  def Start(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.Quit()
          
      pygame.display.update()
      self.clock.tick(60)

  def Quit(self):
    pygame.quit()
    quit()

game = Game(None, None)