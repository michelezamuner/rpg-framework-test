from loader import Loader

class Factory(Loader):
  
  def create(self, model):
    return self.__class__(model)
  
  def getComponentClass(self):
    return self.loadLocal(self.__module__.split('.')[1].capitalize())
  
  def getDependencies(self):
    return ()