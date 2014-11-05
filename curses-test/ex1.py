import curses

def main(stdscr):
  stdscr.border(0)
  stdscr.addstr(12, 25, 'Python curses in action!')
  stdscr.refresh()
  stdscr.getch()

curses.wrapper(main)
