from dispatcher import Dispatcher
from active import Active

class Event(object):
  
  def __init__(self, model):
    self._model = model
    self._canceled = False
    
  def getModel(self):
    return self._model
  
  def isCanceled(self):
    return self._canceled
  
  def cancel(self):
    self._canceled = True
    
  def resume(self):
    self._canceled = False
    
  @classmethod
  def getName(cls):
    return str(cls)
  
  @classmethod
  def getClassName(cls):
    return cls.__name__.lower()