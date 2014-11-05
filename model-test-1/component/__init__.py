from loader import Loader
from event.active import Active
from factory import Factory

class Component(Active, Loader):

  def __init__(self, model):
    super(Component, self).__init__(model.getDispatcher())
    self._model = model
    self._registerListeners()
        
  def getModel(self):
    return self._model
  
  def _registerListeners(self):
    for methodName in dir(self):
      method = getattr(self, methodName)
      if hasattr(method, 'signalName'):
        self._model._addExtension(method.signalName, method)
      elif hasattr(method, 'eventName'):
        self._model._addListener(method.eventName, method)