from tag.positioned import Factory as PositionedFactory
from . import Solid

class Factory(PositionedFactory):
  
  def create(self, model):
    return Solid(model)
    
  def getDependencies(self):
    return (PositionedFactory(self._geography), )