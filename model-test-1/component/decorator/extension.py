from . import Decorator

class Extension(Decorator):
  def __call__(self, method):
    signalName = self._eventClass.getName()
    def call(this, event):
      print str(this._model) + ' ' + method.__module__ + ' self = ' + str(event)
      this._model.saveEvent('self', event)
      method(this, event)
    call.signalName = signalName
    return call