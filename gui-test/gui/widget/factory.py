from char import Char
from console import Console
from text import Text

class Factory(object):

  """
  @param model: game.model.Physical
  @param char: string[1]
  @return gui.widget.Char
  """
  @staticmethod
  def createChar(model, char):
    return Char(model, char)

  """
  @param text: string
  @param pos: physics.Position
  @return gui.widget.Text
  """
  @staticmethod
  def createText(text, pos):
    return Text(text, pos)

  """
  @param console: game.Console
  @param pos: physics.Position
  @return gui.widget.Console
  """
  @staticmethod
  def createConsole(console, pos):
    return Console(console, pos)