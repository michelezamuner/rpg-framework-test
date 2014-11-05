class Loader(object):
  
  @staticmethod
  def loadModule(moduleName, obj):
    return __import__(moduleName, globals(), locals(), [obj], -1)
  
  @classmethod
  def load(cls, moduleName, obj):
    return getattr(cls.loadModule(moduleName, obj), obj)
  
  @classmethod
  def loadLocal(cls, obj):
    return cls.load(cls.__module__, obj)