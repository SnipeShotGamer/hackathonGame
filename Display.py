import pygame 

class Display:
  __inited = False
  def __init__(self):
    raise NotImplementedError('This is a singleton. It may not be instantiated. Used "Init" instead, doofus.')

  @classmethod
  def Init(cls, size = (640, 480), caption = ''):
    if (cls.__inited):
      return

    cls.__caption = caption
    cls.__size = size
    cls.__display = pygame.display.set_mode(size, pygame.HWSURFACE)

  @classmethod
  def SetSize(cls, size):
    cls.__size = size
    cls.__display = pygame.display.set_mode(size)

  @classmethod
  def SetMaxSize(cls):
    cls.__size = cls.GetMaxSize()
    cls.__display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

  @classmethod
  def GetMaxSize(cls):
    info = pygame.display.Info()
    return (info.current_w, info.current_h)

  @classmethod
  def GetDisplay(cls):
    return cls.__display

  @classmethod
  def SetCaption(cls, caption):
    cls.__caption = caption
    pygame.display.set_caption(caption)

  @classmethod
  def GetCaption():
    return cls.__caption

  @classmethod
  def Update(cls):
    pygame.display.update()

  @classmethod
  def Reset(cls, size = (640, 480)):
    cls.__inited = False
    cls.Init(size)