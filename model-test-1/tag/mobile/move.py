from event import Event

class Move(Event):
  
  def __init__(self, model, direction):
    super(Move, self).__init__(model)
    if not direction.isDirection():
      raise ValueError(self.__module__ + ' requires a direction.')
    self._dir = direction
    self._pos = model.getPos().add(direction)
    
  def getPos(self):
    return self._pos
  
  def getDir(self):
    return self._dir 