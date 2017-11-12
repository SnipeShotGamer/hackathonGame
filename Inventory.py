class Inventory:
  __inited = False
  
  def __init__(self):
    raise NotImplementedError('This is a singleton. It may not be instantiated. Used "Init" instead, doofus.')

  @classmethod
  def Init(cls):
    if (cls.__inited):
      return

    cls.__inited = True
    cls.__items = []
    cls.__opened = False
    cls.__armor = []

  @classmethod
  def Opened(cls):
    return cls.__opened

  @classmethod
  def Open(cls):
    cls.__opened = True

  @classmethod
  def Close(cls):
    cls.__opened = False

  @classmethod
  def Reset(cls):
    cls.__inited = False
    cls.Init()