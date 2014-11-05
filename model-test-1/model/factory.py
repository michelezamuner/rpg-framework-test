from . import Model

class Factory(object):
  
  def __init__(self, dispatcher):
    self._dispatcher = dispatcher
    
  def create(self, components):
    model = Model(self._dispatcher)
    for component in components:
      model.addComponent(component)
    return model