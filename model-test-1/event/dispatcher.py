class Dispatcher(object):
  
  def __init__(self):
    self._listeners = {}
    
  def dispatch(self, event):
    if event.getName() in self._listeners:
      for listener in self._listeners[event.getName()]:
        listener(event)
  
  def addListener(self, name, listener):
    if name not in self._listeners:
      self._listeners[name] = [listener]
    else:
      self._listeners[name].append(listener)