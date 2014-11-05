from component import Factory as ComponentFactory
from . import Positioned

class Factory(ComponentFactory):
  
  def __init__(self, geography):
    self._geography = geography
    
  def create(self, model):
    return Positioned(model, self._geography)