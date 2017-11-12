from Contracts import InstanceOf

class EventEmitter:
  def __init__(self, parents, children):
    self._parents = parents
    self._children = children

  def Emit(self, event):
    for parent in self._parents:
      InstanceOf(parent, EventEmitter)
      parent.emit(event)

    return event

  def AddChild(self, child):
    InstanceOf(child, EventEmitter)
    self._children.append(child)