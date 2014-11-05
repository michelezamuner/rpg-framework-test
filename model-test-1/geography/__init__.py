class Geography(object):
  
  def __init__(self):
    self._positions = {}
    
  def setModel(self, model, pos):
    pos = pos.toTuple()
    if pos not in self._positions:
      self._positions[pos] = [model]
    else:
      self._positions[pos].append(model)
      
  def getModels(self, pos):
    pos = pos.toTuple()
    return self._positions[pos] if pos in self._positions else None