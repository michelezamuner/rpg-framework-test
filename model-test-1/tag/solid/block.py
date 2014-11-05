from event import Event

class Block(Event):
  def __init__(self, model, move):
    super(Block, self).__init__(model)
    self._move = move;