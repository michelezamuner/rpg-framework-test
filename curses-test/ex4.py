# ATTENZIONE! Le coordinate a cui si sposta il cursore
# nella chiamata a move() devono essere compatibili con
# l'attuale dimensione della shell.
# Se si ottiene un errore legato a quel metodo, provare
# ad ingrandire la finestra della shell.

import curses

def main(stdscr):
  global curses
  curses.curs_set(0)        # Nascondi il cursore
  stdscr.border(0)          # Nascondi il bordo
  stdscr.move(10, 5)        # Sposta il cursore (y, x)
  stdscr.addstr('Prova', curses.A_UNDERLINE)
  stdscr.refresh()
  stdscr.getch()

curses.wrapper(main)
