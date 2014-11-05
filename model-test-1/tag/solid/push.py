from tag.mobile import Move

class Push(Move):
  def __init__(self, model, move):
    super(Push, self).__init__(model, move.getDir())
    self._move = move
    
  def getMove(self):
    return self._move