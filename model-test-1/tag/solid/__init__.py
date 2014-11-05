from component import Component
from component.decorator import Action, Extension, Reaction
from tag.mobile import Mobile, Move
from tag.positioned import Positioned
from push import Push
from block import Block

class Solid(Component):

  '''
  Try to push in the direction of move.
  If this fails, and another model was pushing this
  one, block it as well.
  '''
  @Action(Push)
  def push(self, move):
    if self.wasPushed() and self.wasBlocked():
      self.block(self._model._external_push.getMove())
  
  @Action(Block)
  def block(self, move):
    move.cancel()
  
  def wasPushed(self):
    return hasattr(self._model, '_external_push')
  
  def wasBlocked(self):
    return self._model._self_push.getMove().isCanceled()
    
  @Extension(Move)
  def _move(self, move):
    self.push(move)
    
  '''
  When pushed, if this is mobile, try to move.
  Otherwise, block who was pushing.
  '''
  @Reaction(Push, lambda com, evt: com._model.getPos().equals(evt.getPos()))
  def _onPush(self, push):
    if self._model.hasComponent(Mobile):
      self._model.move(push.getDir())
    else:
      self.block(push.getMove())

from factory import Factory