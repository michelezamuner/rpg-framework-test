from position import Position as P
from event import Dispatcher
from model import Factory as ModelFactory
from tag.mobile import Mobile, Factory as MobileFactory
from tag.solid import Factory as SolidFactory
from geography import Geography

dispatcher = Dispatcher()

modelFactory = ModelFactory(dispatcher)
geography = Geography()
mobileFactory = MobileFactory(geography)
solidFactory = SolidFactory(geography)
player = modelFactory.create((mobileFactory, solidFactory))
player.setName('Player')
ball = modelFactory.create((mobileFactory, solidFactory))
ball.setName('Ball')
wall = modelFactory.create((solidFactory, ))
wall.setName('Wall')

player.setPos(P(0, 0))
ball.setPos(P(0, 1))
wall.setPos(P(0, 2))

player.move(Mobile.UP)
print 'Player ' + str(player.getPos())
print 'Ball ' + str(ball.getPos())
print 'Wall ' + str(wall.getPos())

wall.setPos(P(0, 3))
player.move(Mobile.UP)
print 'Player ' + str(player.getPos())
print 'Ball ' + str(ball.getPos())
print 'Wall ' + str(wall.getPos())