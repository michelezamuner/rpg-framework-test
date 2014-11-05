class Decorator(object):
  def __init__(self, eventClass):
    self._eventClass = eventClass
    
from action import Action
from extension import Extension
from reaction import Reaction    