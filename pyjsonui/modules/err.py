from . import console
from contextlib import redirect_stderr
import sys
def error_catcher():
  log=''
  sys.stderr = open('err.txt', 'w')
  while True:
    f=open('err.txt', 'r+')
    a=f.read()
    dt=''
    if a.find('e')!=-1:
      tx=a.split('\n')
      for i in tx:
        if i.find('line')!=-1:
          dst=i
          break
      tx=tx[-2].split(':')[1:]  
      for i in tx:
        dt+=':'+i
      dt=dst+'\n'+a
      print(console.format(dt,category='Error'))
    
    f.truncate(0)
    f.close()