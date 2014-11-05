from position import Position

class Body(object):
  
  DIR_UP = Position(0, -1)
  DIR_DOWN = Position(0, 1)
  DIR_LEFT = Position(-1, 0)
  DIR_RIGHT = Position(1, 0)
  MOV_FREE = 0
  MOV_BLOCKED = 1
    
  """
  @param physics: physics.Physics
  @param shape: tuple<physics.Position> | list<physics.Position>
  @param pos: physics.Position
  """
  def __init__(self, physics, shape, pos):
    self._pos = pos
    self._shape = shape
    self._physics = physics
    self._physics.addBody(self)

  """
  @return physics.Position
  """
  def getPos(self):
    return self._pos

  """
  @param pos: physics.Position
  """
  def setPos(self, pos):
    self._pos = pos
      
  """
  @return physics.Physics
  """
  def getPhysics(self):
    return self._physics
  
  """
  @return tuple<physics.Position> | list<physics.Position>
  """
  def getShape(self):
    return self._shape
  
  """
  @param dir: physics.Body.enumeration<DIR>
  """
  def move(self, dir):
    newPos = self.getPos().add(dir)
    if not self._collides(newPos):
      oldPos = self.getPos()
      self.setPos(newPos)
      self._physics.update(self, oldPos)
      return self.MOV_FREE
    else:
      return self.MOV_BLOCKED
  
  def _collides(self, newPos):
    for part in self._shape:
      body = self._physics.getBody(newPos.add(part))
      if body != None and body != self:
        return True
    return False
    