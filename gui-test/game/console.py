class Console(object):
  
  '''
  @param dispatcher: game.Dispatcher
  '''
  def __init__(self, dispatcher):
    dispatcher.addListener(
      dispatcher.events.log.getName(), self.onLog)
    dispatcher.addListener(
      dispatcher.events.logList.getName(), self.onLogList)
    self._messages = []
    
  """
  @return list<string>
  """
  def getMessages(self):
    return self._messages
    
  """
  @param message: string
  """
  def log(self, message):
    self._messages.append(message)

  """
  @param list: tuple<string> | list<string>
  """
  def logList(self, list):
    self._messages.append('(' + ', '.join(str(i) for i in list) + ')')
    
  '''
  @param event: game.dispatcher.event.Log
  '''
  def onLog(self, event):
    self.log(event.getMessage())
    
  '''
  @param event: game.dispatcher.event.LogList
  '''
  def onLogList(self, event):
    self.logList(event.getList())