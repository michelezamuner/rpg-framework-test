class Position(object):
  
  POS_X = 0
  POS_Y = 1
    
  """
  @param x: integer
  @param y: integer
  """
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  """
  @param pos: physics.Position | tuple[2] | list[2]
  @return physics.Position
  """
  def add(self, pos):
    result = self._addPos(pos)
    if None == result: result = self._addTuple(pos)
    if None == result: raise TypeError('Invalid position')
  
    return result
  
  def __str__(self):
    return '(' + str(self.x) + ',' + str(self.y) + ')'

  def _addPos(self, pos):
    try:
      return Position(self.x + pos.x, self.y + pos.y)
    except AttributeError:
      return None
  
  def _addTuple(self, pos):
    try:
      return Position(self.x + pos[self.POS_X], self.y + pos[self.POS_Y])
    except TypeError:
      return None