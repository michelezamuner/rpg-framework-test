from . import Widget

class Console(Widget):
  
  DEFAULT_MAX_LINES = 5
  
  """
  @param console: game.Console
  @param pos: physics.Position
  """
  def __init__(self, console, pos):
    self._console = console
    self._pos = pos
    self._maxLines = self.DEFAULT_MAX_LINES
    
  """
  @param maxLines: integer
  """
  def setMaxLines(self, maxLines):
    self._maxLines = maxLines
    
  """
  @inherit
  """
  def render(self, screen):
    msg = self._console.getMessages()
    tot = self._maxLines if self._maxLines < len(msg) else len(msg)
      
    for i in range(0, tot):
      self._draw(screen, self._pos.add((0, i)), msg[-(i+1)])