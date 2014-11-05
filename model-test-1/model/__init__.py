from event import Dispatcher, Active
from component import Component

class Model(Active):
  
  def __init__(self, dispatcher):
    super(Model, self).__init__(dispatcher)
    self._components = []
    self._signalManager = Dispatcher()
    self._name = ''
    
  def setName(self, name):
    self._name = name
    
  def __str__(self):
    return '[' + self._name + ']'
    
  def addComponent(self, factory):
    for dep in factory.getDependencies():
      if not self.hasComponent(dep.getComponentClass()):
        self.addComponent(dep)
        
    component = factory.create(self)
    self._components.append(component)
    
  def hasComponent(self, componentClass):
    for component in self._components:
      if component.__class__ == componentClass:
        return True
    return False

  def _addExtension(self, signalName, extension):
    self._signalManager.addListener(signalName, extension)
    
  def _signal(self, signal):
    self._signalManager.dispatch(signal)
    
  def saveEvent(self, eventType, event):
    eventAttr = '_' + eventType + '_' + event.getClassName()
    setattr(self, eventAttr, event)
  
  '''
  Search amongst components for a method
  named "name", and execute it.
  
  @param string name Name of called method.
  @throws AttributeError if name not found.
  '''
  def __getattr__(self, name):
    for component in self._components:
      if hasattr(component, name):
        method = getattr(component, name)
        return lambda *args: \
          method() if () == args else method(*args)
        
    raise AttributeError("'" + self.__class__.__name__ +
      "': object has no attribute '" + name + "'")
    
from factory import Factory