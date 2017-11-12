import pygame

class Game:
  def __init__(self, _ee, _ew):
    pygame.init()

    # TODO move to class
    w, h = pygame.display.get_surface().get_size()
    pygame.display.set_mode((w, h))

    # TODO get from config (probably within displaying class)
    pygame.display.set_caption("")

    # TODO move to class
    clock = pygame.time.Clock()

    self._eventEmitter = _ee
    self._eventWatcher = _ew

    self.start()

  def Start():
    while True:
      pygame.display.flip()
      clock.tick(60)

  def Quit():
    pygame.quit()
    quit()