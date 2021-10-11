from pyjsonui import *
from threading import Thread
from functools import partial
from random import randint 
catcher()
console.clear_all()
a=app(windowsize='500x350',title='py_electro')
aa=app(windowsize='500x350',title='loading please wait',bg='color',topmost=True,bginfo='red')
c=canvas(a,size='400x300',place='0x0')
print(console.colorize('loading an pyelectro',category='Info'))
print(console.colorize('wait please a few moments',category='Tip'))
progr=console.progressbar(0,width=4,types=1)
colors={1:'#B87333',1.5:'#848789',2:'#c0c0c0',2.5:'#a19d94',3:'#FFD700',3.5:'#e5e4e2',4:'red',4.5:'blue'}
texts={1:'copper wire',1.5: 'aluminum wire',2:'silver wire',2.5 : 'iron wire',3:'gold wire',3.5: 'platinum wire',4:'+ input',4.5:'- output'}
current=button(a,size='140x50',place='100x300')
el=electricy(220)
'''
1-copper wire
1.5 - alluminum wire
2 - silver wire
2.5 - iron wire 
3-golden wire 
3.5- platinum wire
'''
lastper=0
els=[]
elsln=[]
objlist=[]
objline=[]
color=0.5
k=0
for i in range(40):
  for j in range(30):
    objline.append(0)
  objlist.append(objline)
  objline=[]
def analyze_nearest(list,listofelements):
  pass
def colorline(n):
  global els,lastper
  elsln=[]
  for j in range(30):
    elsln.append(rectangle(c,0,0,10,10,width=1,line='#F3F3F3'))
    elsln[-1].move(x=n*10,y=j*10)
    progr.update((n*30+j)/12)
  els.append(elsln)
  elsln=[]
  r=hex(int(255/(n+1))+randint(0,255-int(255/(n+1))))[2:]
  g=hex(int(255/(n+1))+randint(0,255-int(255/(n+1))))[2:]
  b=hex(int(255/(n+1))+randint(0,255-int(255/(n+1))))[2:]
  r=r*(2-len(r))+r
  g=g*(2-len(g))+g
  b=b*(2-len(b))+b
  aa.configure(bg='color',bginfo='#'+r+g+b,title='loading please wait '+str(int(n/40*100))+'%')
  
  lastper=int(n/40*100)

for i in range(40):
  colorline(i)
def colori(e):
  global color,colors
  x,y=e.x,e.y
  file=open('hi.txt','w')
  file.write(' '*1200*2)
  file.close()
  file=open('hi.txt','w+')
  objlist[x//10][y//10]=color
  els[x//10][y//10].colorize(color=colors[color],line='white')
  for i in objlist:
    for j in i:
      file.write(str(j)+' ')
    file.write('\n')
  file.close()
progr.update(100)
def uncolori(e):
  global color,colors
  x,y=e.x,e.y
  file=open('hi.txt','w')
  file.write(' '*1200*2)
  file.close()
  file=open('hi.txt','w+')
  objlist[x//10][y//10]=0
  els[x//10][y//10].colorize(color=None,line='#F3F3F3',width=1)
  for i in objlist:
    for j in i:
      file.write(str(j)+' ')
    file.write('\n')
  file.close()
def change():
  global k,color,colors,current
  if color<=4:
    k+=1
    color+=0.5
  else:
    color=1
  if color!=4 or color !=4.5:
    el.change_wire(material=texts[color].split()[0])
    current.restyle(text=texts[color]+'\n'+'ro='+str(el.get_ro())+' ohm*m',bg=colors[color])
  else:
    current.restyle(text=texts[color]+'\n'+'U='+' 220 V',bg=colors[color])
def setc(n):
  global color,texts,colors
  color=n
  el.change_wire(material=texts[color].split()[0])
  current.restyle(text=texts[color]+'\n'+'ro='+str(el.get_ro())+' ohm*m',bg=colors[color])
change()
def settings(e):
  setwindow=app(windowsize='200x100',title='settings',bg='color',transparency=80,bginfo='blue')
c.bind('M-Left',colori,withoutput=True)
a.bind('Escape',a.kill,withoutput=False)
b=button(a,text='change color',animation='lighter',function=change,place='225x300')
for i in colors.keys():
  button(a,size='100x40',place=str(400)+'x'+str(int(i*70-50)),bg=colors[i],text=texts[i],function=partial(setc,i))
c.bind('M-Right',uncolori)
c.bind('MM-Left',settings)
aa.kill()
try:
  save((a,c,current,b),filename='1')
except:
  pass
a.loop()