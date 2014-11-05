from component import Component
from position import Position

class Positioned(Component):
  
  def __init__(self, model, geography):
    super(Positioned, self).__init__(model)
    self._geography = geography
    self._pos = Position(0, 0)
    self._geography.setModel(model, self._pos)
    
  def getGeography(self):
    return self._geography
    
  def getPos(self):
    return self._pos
  
  def setPos(self, pos):
    self._pos = pos
    self._geography.setModel(self._model, self._pos)
    
from factory import Factory