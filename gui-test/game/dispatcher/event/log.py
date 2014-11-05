from . import Event

class Log(Event):
  
  '''
  @param message: string
  '''
  def __init__(self, message):
    self._message = message
  
  '''
  @return string
  '''
  def getMessage(self):
    return self._message