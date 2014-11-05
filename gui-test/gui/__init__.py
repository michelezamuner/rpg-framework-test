import curses

class Gui(object):
    
  """
  @param dispatcher: game.Dispatcher
  """
  def __init__(self, dispatcher):
    self._widgets = []
    
    dispatcher.addListener(
      dispatcher.events.quit.getName(), self._onQuit)
    self._dispatcher = dispatcher
    
    self._running = False
    self._keysCache = {}
    
  def run(self):
    self._running = True
    curses.wrapper(self._mainCycle)
  
  """
  @param event: game.dispatcher.Event
  """
  def _onQuit(self, event):
    self._running = False

  """
  @param widget: gui.Widget
  """
  def addWidget(self, widget):
    self._widgets.append(widget)
    
  """
  @param key: curses key code | string[1] | integer
  @return String 
  """
  
  def _mainCycle(self, screen):
    curses.curs_set(0)
    screen.border(0)
    
    while(self._running):
      screen.clear()
      
      for widget in self._widgets:
        widget.render(screen)
        
      screen.refresh()
      
      self._dispatcher.dispatch(
        self._dispatcher.events.keyPress(
          self._getKey(screen.getch())))
      
  def _getKey(self, code):
    if code in self._keysCache:
      return self._keysCache[code]
    
    key = self._getKeyFromCode(code)
    if None == key: key = self._getKeyFromCurses(code)
    if None == key: raise ValueError('Invalid keyboard code.')
    
    self._keysCache[code] = key
    return key
  
  @staticmethod
  def _getKeyFromCode(code):
    try:
      return chr(code)
    except ValueError:
      return None
    
  @staticmethod
  def _getKeyFromCurses(code):
    for key in vars(curses):
      if code == getattr(curses, key):
        return key
    return None