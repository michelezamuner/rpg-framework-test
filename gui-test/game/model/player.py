from physical import Physical

class Player(Physical):
  
  """
  @param event: game.dispatcher.Event
  """
  def moveUp(self):
    newPos = self.getPos().add(self._body.DIR_UP)
    self._dispatcher.dispatch(
      self._dispatcher.events.move(self, newPos))
    result = self._makeMove(self._body.DIR_UP)

  """
  @param event: game.dispatcher.Event
  """
  def moveDown(self):
    self._makeMove(self._body.DIR_DOWN)

  """
  @param event: game.dispatcher.Event
  """
  def moveLeft(self):
    self._makeMove(self._body.DIR_LEFT)

  """
  @param event: game.dispatcher.Event
  """
  def moveRight(self):
    self._makeMove(self._body.DIR_RIGHT)

  def _makeMove(self, dir):
    result = self._body.move(dir)
    if self._body.MOV_BLOCKED == result:
      self.log('The way is blocked!')
    elif self._body.MOV_FREE == result:
      self.log('x: ' + str(self.getPos().x) + ', y: ' + str(self.getPos().y))
    else:
      raise ValueError('Unexpected result from move.')