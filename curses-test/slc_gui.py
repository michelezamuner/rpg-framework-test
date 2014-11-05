QUIT = 100
import curses

def _init(screen):
  global curses
  curses.curs_set(0)
  screen.border(0)
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  
  while (1):
    ret = _init.main(screen)
    if (QUIT == ret):
      break
    
def run(main):
  global curses
  _init.main = main
  curses.wrapper(_init)
