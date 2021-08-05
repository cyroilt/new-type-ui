from pyjsonui import app,canvas,rectangle,gravitation
from time import sleep
a=app(windowsize='1000x1000',bg='GRADIENT',bginfo=('blue','red'))
c=canvas(a,size='1000x1000')
aa=rectangle(c,90,10,109,29)
gr=gravitation(k=0.91)
gr.set_speed(v=20000)
gr.set_height(h=400)
gr.set_floor(800)
for i in range(100000):
  exe=gr.get_moment(t=i,part=0.1,timepart=0.0001)
  x,y=exe['distance'],exe['height']
  aa.move_to(x=x,y=1000-y,artefacts=True)
  aa.update()
  sleep(0.01)
a.loop()