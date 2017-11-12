import json

class Config:
  __inited = False

  def __init__(self):
    raise NotImplementedError('This is a singleton. It may not be instantiated. Used "Init" instead, doofus.')

  @classmethod
  def Init(cls):
    if (cls.__inited):
      return

    configFile = open('config.json', 'r')
    cls.__data = json.load(configFile)
    cls.__inited = True

  @classmethod
  def Get(cls, key):
    return cls.__data[key]

  @classmethod
  def Reset(cls, key):
    cls.__inited
    cls.Init()