
'''from pyjsonui import console
from time import sleep
a=console.progressbar(0)
for i in range(101):
  sleep(0.1)
  a.update(i)'''
'''import curses. #number of rows and columns

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
curses.endwin()

print("Rows:    %d" % num_rows)
print("Columns: %d" % num_cols)'''

'''
import curses #cursor settings

screen = curses.initscr()

curses.curs_set(0)
screen.addstr(2, 2, "Hello, I disabled the cursor!")
screen.refresh()
curses.napms(3000)

curses.curs_set(1)
screen.addstr(3, 2, "And now the cursor is back on.")
screen.refresh()
curses.napms(3000)
'''
'''
import pyjsonui
print(pyjsonui.console.get_size())
print('hi')'''
import pyjsonui
pyjsonui.console.bind('w',function=lambda: print('up'),nooutput=True)
pyjsonui.console.bind('s',function=lambda: print('down'),nooutput=True)
pyjsonui.console.bind('a',function=lambda: print('left'),nooutput=True)
pyjsonui.console.bind('d',function=lambda: print('right'),nooutput=True)