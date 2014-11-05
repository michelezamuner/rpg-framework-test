import curses

def main(stdscr):
    global curses
    win = curses.newwin(5, 40, 7, 20)
    win.border(0)
    win.addstr(4, 5, 'Python curses in action!')
    win.refresh()
    win.getch()

curses.wrapper(main)
