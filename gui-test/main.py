from gui import Gui
from gui.widget.factory import Factory as WidgetFactory
from game.dispatcher import Dispatcher
from game.scene import Scene
from game.console import Console
from physics.position import Position

dispatcher = Dispatcher()
gui = Gui(dispatcher)

console = Console(dispatcher)
scene = Scene(dispatcher)
shape = (Position(0, 0),
         Position(1, 0),
         Position(0, -1))
player = scene.createPlayer(shape, Position(3, 3))
gui.addWidget(WidgetFactory.createChar(player, 'H'))

wallPathExtern = (Position(0, 0),
                    Position(80, 0),
                    Position(80, 15),
                    Position(12, 15),
                    Position(12, 10),
                    Position(0, 10),
                    Position(0, 0))
gui.addWidget(
  WidgetFactory.createChar(
    scene.createWall(
      wallPathExtern, Position(1, 1)), '#'))

wallPathIntern = (Position(40, 0),
                  Position(40, 8),
                  Position(55, 8))
gui.addWidget(
  WidgetFactory.createChar(
    scene.createWall(
      wallPathIntern, Position(1, 1)), '#'))
gui.addWidget(
  WidgetFactory.createConsole(
    console, Position(0, 12)))

gui.addWidget(
  WidgetFactory.createText(
    'Welcome to Sloth Company\'s Dungeon Crawl!',
    Position(0, 0)))

'''
@param event: game.dispatcher.event.KeyPress
'''
def onKeyPress(event):
  key = event.getKey()
  if event.KEY_Q_LOW == key: dispatcher.dispatch(
                              dispatcher.events.quit())
  elif event.KEY_UP == key: player.moveUp()
  elif event.KEY_DOWN == key: player.moveDown()
  elif event.KEY_LEFT == key: player.moveLeft()
  elif event.KEY_RIGHT == key: player.moveRight()
  
dispatcher.addListener(
  dispatcher.events.keyPress.getName(), onKeyPress)

gui.run()