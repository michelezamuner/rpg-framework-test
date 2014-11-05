from . import Decorator

class Action(Decorator):
  def __call__(self, method):
    def call(this, *args):
      model = this._model
      event = self._eventClass(model, *args)
      print str(model) + ' ' + method.__module__ + ' self = ' + str(event)
      model.saveEvent('self', event)
      this._dispatch(event)
      model._signal(event)
      if not event.isCanceled():
        method(this, *args)
    return call