from . import Widget

class Char(Widget):
  
  """
  @param model: game.model.Physical
  @param char: string[1]
  """
  def __init__(self, model, char):
    self._model = model
    self._char = char
    
  """
  @inherit
  """
  def render(self, screen):
    for part in self._model.getShape():
      self._draw(screen, self._model.getPos().add(part), self._char)