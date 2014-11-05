from event.keypress import KeyPress
from event.move import Move
from event.quit import Quit
from event.log import Log
from event.loglist import LogList

'''
@property move: game.dispatcher.event.Move
@property keyPress: game.dispatcher.event.KeyPress
@property quit: game.dispatcher.event.Quit
@property log: game.dispatcher.event.Log
@property logList: game.dispatcher.event.LogList
'''
class Events(object):
  
  def __init__(self):
    self.move = Move
    self.keyPress = KeyPress
    self.quit = Quit
    self.log = Log
    self.logList = LogList