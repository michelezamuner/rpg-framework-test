from . import Model
from physics.body import Body

class Physical(Model):

  """
  @param dispatcher: game.Dispatcher
  @param physics: physics.Physics
  @param shape: tuple<physics.Position> | list<physics.Position>
  @param pos: physics.Position
  """
  def __init__(self, dispatcher, physics, shape, pos):
    super(Physical, self).__init__(dispatcher)
    self._body = Body(physics, shape, pos)
      
  """
  @return physics.Position
  """
  def getPos(self):
    return self._body.getPos()

  """
  @param pos: physics.Position
  """
  def setPos(self, pos):
    self._body.setPos(pos)
    
  """
  @return tuple<physics.Position> | list<physics.Position>
  """
  def getShape(self):
    return self._body.getShape()