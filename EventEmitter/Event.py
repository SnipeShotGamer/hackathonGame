class Event:
  def __init__(self, action, origin, *involvedObjects):
    self.action = action
    self.origin = origin
    self.involvedObjects = involvedObjects