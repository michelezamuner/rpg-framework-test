from physics import Physics
from physics.position import Position
from model.player import Player
from model.wall import Wall

class Scene(object):
  
  """
  @param dispatcher: game.Dispatcher
  """
  def __init__(self, dispatcher):
    self._dispatcher = dispatcher
    self._physics = Physics()
    self._models = []
  
  """
  @param shape: tuple<physics.Position> | list<physics.Position>
  @param pos: physics.Position
  @return game.model.Player
  """
  def createPlayer(self, shape, pos):
    player = Player(self._dispatcher, self._physics, shape, pos)
    self._addModel(player)
    return player
  
  """
  @param path: tuple<physics.Position> | list<physics.Position>
  @param pos: physics.Position
  @return game.model.Wall
  """
  def createWall(self, path, pos):
    # Convert path to shape
    shape = []
    i = 0
    while i < len(path) - 1:
      currentNode = path[i]
      nextNode = path[i + 1]
      if (currentNode.x != nextNode.x and currentNode.y != nextNode.y):
        raise Exception('Invalid path.')
      if (currentNode.x == nextNode.x):
        x = currentNode.x
        first = min(currentNode.y, nextNode.y)
        last = max(currentNode.y, nextNode.y)
        for y in range(first, last):
          shape.append(Position(x, y))
      else:
        y = currentNode.y
        first = min(currentNode.x, nextNode.x)
        last = max(currentNode.x, nextNode.x)
        for x in range(first, last):
          shape.append(Position(x, y))
        
      i += 1
    
    wall = Wall(self._dispatcher, self._physics, shape, pos)
    self._addModel(wall)
    return wall
  
  """
  @return physics.Physics
  """
  def getPhysics(self):
    return self._physic

  def _addModel(self, model):
    if model in self._models:
      raise Exception('Duplicated model.')
    
    self._models.append(model)