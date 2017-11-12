from string import Template

def InstanceOf(_object, _class):
  if (not isinstance(_object, _class)):
    message = Template('$obj is not $cls.') \
      .substitute(obj=str(_object), cls=str(_class))

    raise TypeError(message)

