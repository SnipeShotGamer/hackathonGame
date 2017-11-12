class EventWatcher:
  def __init__(self, events = []):
    self.__listeningTo = []
    self.__events = events

  def AttachTo(self, *eventEmitters):
    for eventEmitter in eventEmitters:
      InstanceOf(eventEmitter, EventEmitter)
      self.__listeningTo.append(eventEmitter)

  def CheckEvents(self):
    for emitter in self.__listeningTo:
      for event in emitter.GetEvents():
        self.Notify(event)

  def Notify(self, event):
    try:
      self.__events.index(event.action)
      getattr(self, event.action)(event)
    except ValueError:
      pass