from . import Event

class LogList(Event):
  
  '''
  @param list: tuple|list
  '''
  def __init__(self, list):
    self._list = list
    
  '''
  @return tuple|list
  '''
  def getList(self):
    return self._list