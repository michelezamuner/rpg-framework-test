from position import Position
from tag.positioned import Positioned
from component import Component
from component.decorator import Action
from move import Move

class Mobile(Component):
  UP = Position(0, 1)
  DOWN = Position(0, -1)
  LEFT = Position(-1, 0)
  RIGHT = Position(1, 0)
    
  @Action(Move)
  def move(self, direction):
    self._model.setPos(self._model.getPos().add(direction))
        
from factory import Factory