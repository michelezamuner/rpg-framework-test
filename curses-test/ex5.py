import slc_gui

def main(screen):
  global slc_gui
  screen.move(5, 5)
  screen.addstr('Premere "p" e "<Home>" per stampare dei messaggi, "q" per uscire.')
  c = screen.getch()
  if ord('p') == c:
    screen.move(15, 5)
    screen.addstr('Ciao', slc_gui.curses.color_pair(1))
  if slc_gui.curses.KEY_HOME == c:
    screen.move(0, 0)
    screen.addstr('Pippo', slc_gui.curses.color_pair(1))
  if ord('q') == c:
    return slc_gui.QUIT

slc_gui.run(main)
