from pyjsonui import app,canvas,rectangle
from time import sleep
a1=app(windowsize='500x300',bg='gradient',bginfo=('#AABBCC','#FFEEDD'))
c=canvas(a1,size='500x300')
bb=rectangle(c,10,10,30,50)
kx=5
ky=5
kr=3
for i in range(0,100000000,1):
  bb.update()
  bb.rotate(kr)
  sleep(0.01)
  bb.move(x=kx,y=ky)
  kr=1
  bb.update()
  x,y,x1,y1,x2,y2,x3,y3=bb.points(all=True)
  if x>=500 or x1>=500 or x2>=500 or x3>=500:
    kx=kx*-1
    kr*=-1
    
  if y>=300 or y1>=300 or y2>=300 or y3>=300:
    ky=ky*-1
    kr*=-1
  if x<=0 or x1<=0 or x2<=0 or x3<=0:
    kx=kx*-1
    kr*=-1
  if y<=0 and y1<=0 or y2<=0 and y3<=0:
    ky=ky*-1
    kr*=-1
a1.loop()