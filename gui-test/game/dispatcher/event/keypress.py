from . import Event

class KeyPress(Event):
  KEY_Q_LOW = 'q'
  KEY_UP = 'KEY_UP'
  KEY_DOWN = 'KEY_DOWN'
  KEY_LEFT = 'KEY_LEFT'
  KEY_RIGHT = 'KEY_RIGHT'
  
  '''
  @param key: string
  '''
  def __init__(self, key):
    self._key = key
    
  '''
  @return string
  '''
  def getKey(self):
    return self._key