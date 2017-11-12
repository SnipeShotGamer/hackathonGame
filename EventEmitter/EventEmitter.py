class EventEmitter:
  def __init__(self, parents):
    self._parents = parents

  def Emit(self, event):
    for parent in parents:
      parent.emit(event)