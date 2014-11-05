from tag.positioned import Factory as PositionedFactory
from . import Mobile

class Factory(PositionedFactory):
  
  def create(self, model):
    return Mobile(model)
  
  def getDependencies(self):
    return (PositionedFactory(self._geography), )