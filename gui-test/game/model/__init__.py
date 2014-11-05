class Model(object):

  """
  @param dispatcher: game.Dispatcher
  """
  def __init__(self, dispatcher):
    self._dispatcher = dispatcher
    
  """
  @param message: string
  """
  def log(self, message):
    self._dispatcher.dispatch(self._dispatcher.events.log(message))