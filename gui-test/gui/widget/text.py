from . import Widget

class Text(Widget):
  
  """
  @param text: string
  @param pos: physics.Position
  """
  def __init__(self, text, pos):
    self._pos = pos
    self._text = text
  
  """
  @inherit
  """
  def render(self, screen):
    self._draw(screen, self._pos, self._text)