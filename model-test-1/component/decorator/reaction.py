from . import Decorator

class Reaction(Decorator):
  def __init__(self, eventClass, condition):
    super(Reaction, self).__init__(eventClass)
    self.condition = condition
    
  def __call__(self, method):
    eventName = self._eventClass.getName()
    def call(this, event):
      model = this._model
      if model != event.getModel() and self.condition(this, event):
        print str(model) + ' ' + method.__module__ + ' external = ' + str(event)
        model.saveEvent('external', event)
        method(this, event)
    call.eventName = eventName
    return call