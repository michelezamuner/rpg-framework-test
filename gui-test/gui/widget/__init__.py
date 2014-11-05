class Widget(object):

  """
  @param screen: curses.window
  """
  def render(self, screen):
    raise NotImplementedError('Calling abstract method gui.Widget.render().')
    
  def _draw(self, screen, pos, string):
    screen.move(pos.y, pos.x)
    screen.addstr(string)