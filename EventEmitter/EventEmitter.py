from Contracts import InstanceOf

class EventEmitter:
  def __init__(self, facing):
    self.__parents = []
    self.__children = []

  def Emit(self, event):
    InstanceOf(event, EventEmitter)

    for parent in self.__parents:
      InstanceOf(parent, EventEmitter)
      parent.emit(event)

    self.__events.append(event)

  def AddChildren(self, *children):
    for child in children:
      InstanceOf(child, EventEmitter)
      self._children.append(child)

  def AddParents(self, *parents):
    for parent in parents:
      InstanceOf(parent, EventEmitter)
      self.__parents.append(parent)

  def GetEvents(self):
    return self.__events

  def ResetEvents(self):
    self.__events = []