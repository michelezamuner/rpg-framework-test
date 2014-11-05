from . import Event

class Move(Event):
  
  """
  @param model: game.Model
#   @param pos: physics.Position
  @param pos: game.geography.Position
  """
  def __init__(self, model, pos):
    self._model = model
    self._pos = pos
    
  """
#   @return: physics.Position
  @return: game.geography.Position
  """
  def getPos(self):
    return self._pos
  
  """
  @return: game.Model
  """
  def getModel(self):
    return self._model