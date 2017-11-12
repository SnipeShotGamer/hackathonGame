from threading import Thread
import pygame

class Clock:
  def __init__(self, tick = 60):
    self.__clock = pygame.time.Clock()
    self.__tick = tick

  def Timeout(self, milliseconds, func, args = None):
    def _timeout(_self, args):
      totalTime = 0

      while True:
        _self.__clock.tick(_self.__tick)

        totalTime += _self.__clock.get_time()

        if (totalTime >= milliseconds):
          func(args)
          return

    thread = Thread(target = _timeout, args = (self, args))
    thread.start()

    return self

  def SetTick(self, tick):
    self.__tick = tick

    return self

  def Tick(self):
    self.__clock.tick(self.__tick)

    return self