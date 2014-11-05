from body import Body

class Physics:

  def __init__(self):
    self._map = {}
  
  """
  @param pos: physics.Position
  @return physics.Body | None
  """
  def getBody(self, pos):
    p = (pos.x, pos.y)
    return self._map[p] if p in self._map else None
  
  """
  @param body: physics.Body
  """
  def addBody(self, body):
    self._loadShape(body)
  
  """
  @param body: physics.Body
  @param oldPos: physics.Position
  """
  def update(self, body, oldPos):
    self._unloadShape(body, oldPos)
    self._loadShape(body)
  
  def _loadShape(self, body):
    for part in body.getShape():
      pos = body.getPos().add(part)
      self._map[(pos.x, pos.y)] = body
      
  def _unloadShape(self, body, pos):
    for part in body.getShape():
      partPos = pos.add(part)
      del self._map[(partPos.x, partPos.y)]