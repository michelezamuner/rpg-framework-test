class Active(object):
  
  def __init__(self, dispatcher):
    self._dispatcher = dispatcher
    
  def getDispatcher(self):
    return self._dispatcher
    
  def _addListener(self, name, listener):
    self._dispatcher.addListener(name, listener)
    
  def _dispatch(self, event):
    self._dispatcher.dispatch(event)