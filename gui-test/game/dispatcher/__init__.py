from events import Events

class Dispatcher(object):
  
  def __init__(self):
    self.events = Events()
    self._listeners = {}
    
  """
  @param event: game.dispatcher.Event
  """
  def dispatch(self, event):
    if event.getName() in self._listeners:
      for listener in self._listeners[event.getName()]:
        listener(event)
        
  """
  @param eventName: string
  @param listener: function
  """
  def addListener(self, eventName, listener):
    if eventName not in self._listeners:
      self._listeners[eventName] = [listener]
    else:
      self._listeners[eventName].append(listener)