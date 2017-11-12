from string import Template

def InstanceOf(func):
  def _instanceOf(_object, _class):
    if (not instanceof(_object, _class)):
      message = Template('$obj is not $cls.') \
        .substitute(obj=str(_object), cls=str(_class))

      raise TypeError(message)

  return _instanceOf

