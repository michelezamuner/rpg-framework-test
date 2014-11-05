import curses

def main(stdscr):
  global curses
  # Ridefinisce la coppia di colori n. 1
  # (foreground, background)
  curses.init_pair (1, curses.COLOR_RED, curses.COLOR_WHITE)

  curses.curs_set(0)
  stdscr.border(0)
  stdscr.move(15, 5)
  stdscr.addstr('Prova', curses.A_UNDERLINE | curses.color_pair(1))
  stdscr.refresh()
  stdscr.getch()

curses.wrapper(main)
