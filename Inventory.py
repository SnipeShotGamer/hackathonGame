class Inventory:
  def __init__(self):
    raise NotImplementedError('This is a singleton. It may not be instantiated. Used "Init" instead, doofus.')

  @classmethod
  def Init(cls):
    cls.__items = []
    cls.__opened = False
    cls.__armor = []

  @classmethod
  def Opened(cls):
    return cls.__opened

  @classmethod
  def Open():
    cls.__opened = True

  @classmethod
  def Close():
    cls.__opened = False