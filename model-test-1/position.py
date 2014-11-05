class Position(object):  

  def __init__(self, x, y = None):
    result = self._loadCoords(x, y) # x and y?
    if False == result:
      result = self._loadPos(x) # Position?
    if False == result:
      result = self._loadList(x)  # list/tuple?
    if False == result:
      raise ValueError('Unable to build Position.')
    
  def toTuple(self):
    return (self.x, self.y)    
  
  def equals(self, pos):
    return self.x == pos.x and self.y == pos.y

  def add(self, pos):
    return Position(self.x + pos.x, self.y + pos.y)

  def sub(self, pos, y = None):
    newPos = Position(pos, y)
    return Position(self.x - newPos.x, self.y - newPos.y)
    
  def getDirection(self, pos):
    diff = pos.sub(self)
    if 0 != diff.x and 0 != diff.y:
      raise ValueError('Direction can be calculated'
        + 'only from adjacent positions.')
    
    return Position(0, 1) if 0 == diff.x else Position(1, 0)
  
  def isDirection(self):
    hor = 1 == self.x * self.x and 0 == self.y
    # If not horizontal, return True if vertical
    if not hor:
      return 0 == self.x and 1 == self.y * self.y
    
    # It didn't return before: it's horizontal
    return True 

  def __str__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
  def _loadCoords(self, x, y):
    if None != y:
      self.x = x
      self.y = y
    else:
      return False
    
    return True

  def _loadPos(self, pos):
    try:
      x = pos.x
      y = pos.y
    except AttributeError:
      return False

    self.x = x
    self.y = y

    return True

  def _loadList(self, pos):
    try:
      x = pos[0]
      y = pos[1]
    except TypeError:
      return False

    self.x = x
    self.y = y

    return True