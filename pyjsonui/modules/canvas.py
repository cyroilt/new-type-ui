from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from math import sin,cos
objects=[]
artefactsl=[]
rules={'M-Left':'<Button-1>',
'M-Right':'<Button-3>',
'M-Middle':'<Button-2>',
'M-Wheel':'<MouseWheel>',
'MM-Left':'<Double-Button-1>',
'MM-Middle':'<Double-Button-2>',
'MM-Right':'<Double-Button-3>',
'M-Motion':'<Motion>',
'M-Left-Motion':'<B1-Motion>',
'M-Middle-Motion':'<B2-Motion>',
'M-Right-Motion':'<B3-Motion>',
'Enter':'<Return>',
'In':'<Enter>',
'Out':'<Leave>'}
class canvas():

  def __init__(self,app,size='100x100',place=None,bg='white'):
    self.window=app._mw()
    wid,heig=size.split('x')
    self.c=Canvas(self.window,bg=bg,width=int(wid),height=int(heig))
    self.c.pack()
    if place!=None:
      x,y=place.split('x')
      self.c.place(x=int(x),y=int(y))
    self.holst=-464
    self.width=int(wid)
    self.height=int(heig)
    
  def get_win(self):
    return self.window
  def get_c(self):
    return self.c
  def bind(self,rule,todo,args=(),kwargs={},withoutput=True):
    global rules
    def doing(e):
      if withoutput:
        if args!= ():
            if kwargs != {}:
              todo(e,args,kwargs)
            else:
              todo(e,args)
        else:
          if kwargs != {}:
              todo(e,kwargs)
          else:
              todo(e)
      else:
        if args!= ():
            if kwargs != {}:
              todo(args,kwargs)
            else:
              todo(args)
        else:
          if kwargs != {}:
              todo(kwargs)
          else:
              todo()
    if rule in rules.keys():
      self.c.bind(rules[rule],doing)
    else:
      self.c.bind('<'+str(rule)+'>',doing)
class rectangle():
  def __init__(self,c,x,y,x1,y1,fill=None,line='black',width=2):
    self.c=c.get_c()
    self.ca=c
    self.artefactsl=[]
    self.w=self.ca.get_win()
    mx=max(x1-x,y1-y)
    self.imag=Image.new('RGBA',(x+mx*2,x+mx*2))
    self.draw = ImageDraw.Draw(self.imag)
    self.draw.rectangle([(x,y), (x1,y1)], fill=fill, outline=line,width=width)
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((x1-x)//2,(y1-y)//2,image=self.path)
    self.x=x
    self.y=y
    self.x1=x1
    self.y1=y1
    self.x0=x
    self.y0=y
    self.x01=x1
    self.y01=y1
    self.angle=0
    self.elements=[]
    self.scalex=1
    self.scaley=1
    self.grouped=[]
    self.c.update()
  def rotate(self,angle):
    self.rotated=self.imag.rotate(self.angle+angle)
    self.angle+=angle
    self.path=ImageTk.PhotoImage(self.rotated,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.rotate(angle)
  def scale(self,x=1,y=1):
    self.scalex*=x
    self.scaley*=y
    self.scaled=self.imag.resize(((self.x1-self.x)*x,(self.y1-self.y)*y),Image.NEAREST)
    self.path=ImageTk.PhotoImage(self.scaled,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.scale(x=x,y=y)
  def update(self):
    self.c.update()
  def move(self,x=0,y=0,artefacts=False):
    self.c.move(self.rec,x,y)
    self.x+=x
    self.y1+=y
    self.x1+=x
    self.y+=y
    if artefacts==True:
        self.artefactsl.append(rectangle(self.ca,self.x0,self.y0,self.x01,self.y01))
        self.artefactsl[-1].move_to(self.x,self.y)
    for i in self.grouped:
      i.move(x=x,y=y,artefacts=artefacts)
  def pos(self):
    return self.x,self.y,self.x1,self.y1
  def coords(self):
    return (self.x1-self.x)//2+self.x,(self.y1-self.y)//2+self.y
  def points(self,all=False):
    x,y,x1,y1=self.x,self.y,self.x1,self.y1
    xc,yc=self.coords()
    x2,y2,x3,y3=self.x,self.y,self.x1,self.y
    x2,y2,x3,y3=x2,y2+(yc-y)*2,x3+(xc-x)*2,y3
    angle=self.angle
    xs=((x-xc)*cos(angle))-((y-yc)*sin(angle))+xc
    ys=((x-xc)*sin(angle))+((y-yc)*cos(angle))+yc
    x1s=((x1-xc)*cos(angle))-((y1-yc)*sin(angle))+xc
    y1s=((x1-xc)*sin(angle))+((y1-yc)*cos(angle))+yc
    if all:
      xs2=((x2-xc)*cos(angle))-((y2-yc)*sin(angle))+xc
      ys2=((x2-xc)*sin(angle))+((y2-yc)*cos(angle))+yc
      x2s=((x3-xc)*cos(angle))-((y3-yc)*sin(angle))+xc
      y2s=((x3-xc)*sin(angle))+((y3-yc)*cos(angle))+yc
      return (round(xs),round(ys),round(x1s),round(y1s),round(xs2),round(ys2),round(x2s),round(y2s))
    else:
      return (round(xs),round(ys),round(x1s),round(y1s))  
  def move_to(self,x=0,y=0,artefacts=False):
    x1,y1=self.coords()
    self.move(int(x-x1),int(y-y1),artefacts=artefacts)
    for i in self.grouped:
      i.move_to(x=x,y=y,artefacts=artefacts)
  def hide(self):
    self.path=ImageTk.PhotoImage(Image.new("RGBA",(100,100)),master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.update()
    for i in self.grouped:
      i.hide()
  def show(self):
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.scale(x=self.scalex,y=self.scaley)
    self.rotate(self.angle)
    self.update()
    for i in self.grouped:
      i.show()
  def group(self,*obj):#you should call mother element
    for i in range(len(obj)):
      self.grouped.append(obj[i])
  def ungroup(self,*obj):
    self.grouped=[]
class oval():
  def __init__(self,c,x,y,x1,y1,fill=None,line='black',width=2):
    self.c=c.get_c()
    self.ca=c
    self.artefactsl=[]
    self.w=self.ca.get_win()
    mx=max(x1-x,y1-y)
    self.imag=Image.new('RGBA',(x+mx*2,x+mx*2))
    self.draw = ImageDraw.Draw(self.imag)
    self.draw.ellipse([(x,y), (x1,y1)], fill=fill, outline=line,width=width)
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((x1-x)//2,(y1-y)//2,image=self.path)
    self.x=x
    self.y=y
    self.x1=x1
    self.y1=y1
    self.x0=x
    self.y0=y
    self.x01=x1
    self.y01=y1
    self.angle=0
    self.elements=[]
    self.scalex=1
    self.scaley=1
    self.grouped=[]
    self.c.update()
  def rotate(self,angle):
    self.rotated=self.imag.rotate(self.angle+angle)
    self.angle+=angle
    self.path=ImageTk.PhotoImage(self.rotated,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.rotate(angle)
  def scale(self,x=1,y=1):
    self.scalex*=x
    self.scaley*=y
    self.scaled=self.imag.resize(((self.x1-self.x)*x,(self.y1-self.y)*y),Image.NEAREST)
    self.path=ImageTk.PhotoImage(self.scaled,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.scale(x=x,y=y)
  def update(self):
    self.c.update()
  def move(self,x=0,y=0,artefacts=False):
    self.c.move(self.rec,x,y)
    self.x+=x
    self.y1+=y
    self.x1+=x
    self.y+=y
    if artefacts==True:
        self.artefactsl.append(oval(self.ca,self.x0,self.y0,self.x01,self.y01))
        self.artefactsl[-1].move_to(self.x,self.y)
    for i in self.grouped:
      i.move(x=x,y=y,artefacts=artefacts)
  def pos(self):
    return self.x,self.y,self.x1,self.y1
  def coords(self):
    return (self.x1-self.x)//2+self.x,(self.y1-self.y)//2+self.y
  def points(self,all=False):
    x,y,x1,y1=self.x,self.y,self.x1,self.y1
    xc,yc=self.coords()
    x2,y2,x3,y3=self.x,self.y,self.x1,self.y
    x2,y2,x3,y3=x2,y2+(yc-y)*2,x3+(xc-x)*2,y3
    angle=self.angle
    xs=((x-xc)*cos(angle))-((y-yc)*sin(angle))+xc
    ys=((x-xc)*sin(angle))+((y-yc)*cos(angle))+yc
    x1s=((x1-xc)*cos(angle))-((y1-yc)*sin(angle))+xc
    y1s=((x1-xc)*sin(angle))+((y1-yc)*cos(angle))+yc
    if all:
      xs2=((x2-xc)*cos(angle))-((y2-yc)*sin(angle))+xc
      ys2=((x2-xc)*sin(angle))+((y2-yc)*cos(angle))+yc
      x2s=((x3-xc)*cos(angle))-((y3-yc)*sin(angle))+xc
      y2s=((x3-xc)*sin(angle))+((y3-yc)*cos(angle))+yc
      return (round(xs),round(ys),round(x1s),round(y1s),round(xs2),round(ys2),round(x2s),round(y2s))
    else:
      return (round(xs),round(ys),round(x1s),round(y1s))  
  def move_to(self,x=0,y=0,artefacts=False):
    x1,y1=self.coords()
    self.move(int(x-x1),int(y-y1),artefacts=artefacts)
    for i in self.grouped:
      i.move_to(x=x,y=y,artefacts=artefacts)
  def hide(self):
    self.path=ImageTk.PhotoImage(Image.new("RGBA",(100,100)),master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.update()
    for i in self.grouped:
      i.hide()
  def show(self):
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.scale(x=self.scalex,y=self.scaley)
    self.rotate(self.angle)
    self.update()
    for i in self.grouped:
      i.show()
  def group(self,*obj):#you should call mother element
    for i in range(len(obj)):
      self.grouped.append(obj[i])
  def ungroup(self,*obj):
    self.grouped=[]
class rounded_rectangle():
  def __init__(self,c,x,y,x1,y1,fill=None,line='black',width=2,radius=2):
    self.c=c.get_c()
    self.ca=c
    self.artefactsl=[]
    self.w=self.ca.get_win()
    mx=max(x1-x,y1-y)
    self.imag=Image.new('RGBA',(x+mx*2,x+mx*2))
    self.draw = ImageDraw.Draw(self.imag)
    self.draw.rounded_rectangle([(x,y), (x1,y1)], fill=fill, outline=line,width=width,radius=radius)
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((x1-x)//2,(y1-y)//2,image=self.path)
    self.x=x
    self.radius=radius
    self.y=y
    self.x1=x1
    self.y1=y1
    self.x0=x
    self.y0=y
    self.x01=x1
    self.y01=y1
    self.angle=0
    self.elements=[]
    self.scalex=1
    self.scaley=1
    self.grouped=[]
    self.c.update()
  def rotate(self,angle):
    self.rotated=self.imag.rotate(self.angle+angle)
    self.angle+=angle
    self.path=ImageTk.PhotoImage(self.rotated,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.rotate(angle)
  def scale(self,x=1,y=1):
    self.scalex*=x
    self.scaley*=y
    self.scaled=self.imag.resize(((self.x1-self.x)*x,(self.y1-self.y)*y),Image.NEAREST)
    self.path=ImageTk.PhotoImage(self.scaled,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.scale(x=x,y=y)
  def update(self):
    self.c.update()
  def move(self,x=0,y=0,artefacts=False):
    self.c.move(self.rec,x,y)
    self.x+=x
    self.y1+=y
    self.x1+=x
    self.y+=y
    if artefacts==True:
        self.artefactsl.append(rounded_rectangle(self.ca,self.x0,self.y0,self.x01,self.y01,radius=self.radius))
        self.artefactsl[-1].move_to(self.x,self.y)
    for i in self.grouped:
      i.move(x=x,y=y,artefacts=artefacts)
  def pos(self):
    return self.x,self.y,self.x1,self.y1
  def coords(self):
    return (self.x1-self.x)//2+self.x,(self.y1-self.y)//2+self.y
  def points(self,all=False):
    x,y,x1,y1=self.x,self.y,self.x1,self.y1
    xc,yc=self.coords()
    x2,y2,x3,y3=self.x,self.y,self.x1,self.y
    x2,y2,x3,y3=x2,y2+(yc-y)*2,x3+(xc-x)*2,y3
    angle=self.angle
    xs=((x-xc)*cos(angle))-((y-yc)*sin(angle))+xc
    ys=((x-xc)*sin(angle))+((y-yc)*cos(angle))+yc
    x1s=((x1-xc)*cos(angle))-((y1-yc)*sin(angle))+xc
    y1s=((x1-xc)*sin(angle))+((y1-yc)*cos(angle))+yc
    if all:
      xs2=((x2-xc)*cos(angle))-((y2-yc)*sin(angle))+xc
      ys2=((x2-xc)*sin(angle))+((y2-yc)*cos(angle))+yc
      x2s=((x3-xc)*cos(angle))-((y3-yc)*sin(angle))+xc
      y2s=((x3-xc)*sin(angle))+((y3-yc)*cos(angle))+yc
      return (round(xs),round(ys),round(x1s),round(y1s),round(xs2),round(ys2),round(x2s),round(y2s))
    else:
      return (round(xs),round(ys),round(x1s),round(y1s))  
  def move_to(self,x=0,y=0,artefacts=False):
    x1,y1=self.coords()
    self.move(int(x-x1),int(y-y1),artefacts=artefacts)
    for i in self.grouped:
      i.move_to(x=x,y=y,artefacts=artefacts)
  def hide(self):
    self.path=ImageTk.PhotoImage(Image.new("RGBA",(100,100)),master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.update()
    for i in self.grouped:
      i.hide()
  def show(self):
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.scale(x=self.scalex,y=self.scaley)
    self.rotate(self.angle)
    self.update()
    for i in self.grouped:
      i.show()
  def group(self,*obj):#you should call mother element
    for i in range(len(obj)):
      self.grouped.append(obj[i])
  def ungroup(self,*obj):
    self.grouped=[]
class arc():
  def __init__(self,c,x,y,x1,y1,start,end,fill=None,width=2):
    self.c=c.get_c()
    self.ca=c
    self.artefactsl=[]
    self.w=self.ca.get_win()
    mx=max(x1-x,y1-y)
    self.imag=Image.new('RGBA',(x+mx*2,x+mx*2))
    self.draw = ImageDraw.Draw(self.imag)
    self.draw.arc((x,y, x1,y1),start,end, fill=fill,width=width)
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((x1-x)//2,(y1-y)//2,image=self.path)
    self.x=x
    self.y=y
    self.x1=x1
    self.y1=y1
    self.x0=x
    self.y0=y
    self.x01=x1
    self.y01=y1
    self.angle=0
    self.elements=[]
    self.scalex=1
    self.scaley=1
    self.start=start
    self.end=end
    self.grouped=[]
    self.c.update()
  def rotate(self,angle):
    self.rotated=self.imag.rotate(self.angle+angle)
    self.angle+=angle
    self.path=ImageTk.PhotoImage(self.rotated,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.rotate(angle)
  def scale(self,x=1,y=1):
    self.scalex*=x
    self.scaley*=y
    self.scaled=self.imag.resize(((self.x1-self.x)*x,(self.y1-self.y)*y),Image.NEAREST)
    self.path=ImageTk.PhotoImage(self.scaled,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.scale(x=x,y=y)
  def update(self):
    self.c.update()
  def move(self,x=0,y=0,artefacts=False):
    self.c.move(self.rec,x,y)
    self.x+=x
    self.y1+=y
    self.x1+=x
    self.y+=y
    if artefacts==True:
        self.artefactsl.append(arc(self.ca,self.x0,self.y0,self.x01,self.y01,self.start,self.end))
        self.artefactsl[-1].move_to(self.x,self.y)
    for i in self.grouped:
      i.move(x=x,y=y,artefacts=artefacts)
  def pos(self):
    return self.x,self.y,self.x1,self.y1
  def coords(self):
    return (self.x1-self.x)//2+self.x,(self.y1-self.y)//2+self.y
  def points(self,all=False):
    x,y,x1,y1=self.x,self.y,self.x1,self.y1
    xc,yc=self.coords()
    x2,y2,x3,y3=self.x,self.y,self.x1,self.y
    x2,y2,x3,y3=x2,y2+(yc-y)*2,x3+(xc-x)*2,y3
    angle=self.angle
    xs=((x-xc)*cos(angle))-((y-yc)*sin(angle))+xc
    ys=((x-xc)*sin(angle))+((y-yc)*cos(angle))+yc
    x1s=((x1-xc)*cos(angle))-((y1-yc)*sin(angle))+xc
    y1s=((x1-xc)*sin(angle))+((y1-yc)*cos(angle))+yc
    if all:
      xs2=((x2-xc)*cos(angle))-((y2-yc)*sin(angle))+xc
      ys2=((x2-xc)*sin(angle))+((y2-yc)*cos(angle))+yc
      x2s=((x3-xc)*cos(angle))-((y3-yc)*sin(angle))+xc
      y2s=((x3-xc)*sin(angle))+((y3-yc)*cos(angle))+yc
      return (round(xs),round(ys),round(x1s),round(y1s),round(xs2),round(ys2),round(x2s),round(y2s))
    else:
      return (round(xs),round(ys),round(x1s),round(y1s))  
  def move_to(self,x=0,y=0,artefacts=False):
    x1,y1=self.coords()
    self.move(int(x-x1),int(y-y1),artefacts=artefacts)
    for i in self.grouped:
      i.move_to(x=x,y=y,artefacts=artefacts)
  def hide(self):
    self.path=ImageTk.PhotoImage(Image.new("RGBA",(100,100)),master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.update()
    for i in self.grouped:
      i.hide()
  def show(self):
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.scale(x=self.scalex,y=self.scaley)
    self.rotate(self.angle)
    self.update()
    for i in self.grouped:
      i.show()
  def group(self,*obj):#you should call mother element
    for i in range(len(obj)):
      self.grouped.append(obj[i])
  def ungroup(self,*obj):
    self.grouped=[]
class line():
  def __init__(self,c,x,y,x1,y1,fill=None,width=2):
    self.c=c.get_c()
    self.ca=c
    self.artefactsl=[]
    self.w=self.ca.get_win()
    mx=max(x1-x,y1-y)
    self.imag=Image.new('RGBA',(x+mx*2,x+mx*2))
    self.draw = ImageDraw.Draw(self.imag)
    self.draw.arc((x,y, x1,y1),start,end, fill=fill,width=width)
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((x1-x)//2,(y1-y)//2,image=self.path)
    self.x=x
    self.y=y
    self.x1=x1
    self.y1=y1
    self.x0=x
    self.y0=y
    self.x01=x1
    self.y01=y1
    self.angle=0
    self.elements=[]
    self.scalex=1
    self.scaley=1
    self.start=start
    self.end=end
    self.grouped=[]
    self.c.update()
  def rotate(self,angle):
    self.rotated=self.imag.rotate(self.angle+angle)
    self.angle+=angle
    self.path=ImageTk.PhotoImage(self.rotated,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.rotate(angle)
  def scale(self,x=1,y=1):
    self.scalex*=x
    self.scaley*=y
    self.scaled=self.imag.resize(((self.x1-self.x)*x,(self.y1-self.y)*y),Image.NEAREST)
    self.path=ImageTk.PhotoImage(self.scaled,master=self.c)
    self.c.itemconfigure(self.rec,image=self.path)
    for i in self.grouped:
      i.scale(x=x,y=y)
  def update(self):
    self.c.update()
  def move(self,x=0,y=0,artefacts=False):
    self.c.move(self.rec,x,y)
    self.x+=x
    self.y1+=y
    self.x1+=x
    self.y+=y
    if artefacts==True:
        self.artefactsl.append(line(self.ca,self.x0,self.y0,self.x01,self.y01,self.start,self.end))
        self.artefactsl[-1].move_to(self.x,self.y)
    for i in self.grouped:
      i.move(x=x,y=y,artefacts=artefacts)
  def pos(self):
    return self.x,self.y,self.x1,self.y1
  def coords(self):
    return (self.x1-self.x)//2+self.x,(self.y1-self.y)//2+self.y
  def points(self,all=False):
    x,y,x1,y1=self.x,self.y,self.x1,self.y1
    xc,yc=self.coords()
    x2,y2,x3,y3=self.x,self.y,self.x1,self.y
    x2,y2,x3,y3=x2,y2+(yc-y)*2,x3+(xc-x)*2,y3
    angle=self.angle
    xs=((x-xc)*cos(angle))-((y-yc)*sin(angle))+xc
    ys=((x-xc)*sin(angle))+((y-yc)*cos(angle))+yc
    x1s=((x1-xc)*cos(angle))-((y1-yc)*sin(angle))+xc
    y1s=((x1-xc)*sin(angle))+((y1-yc)*cos(angle))+yc
    if all:
      xs2=((x2-xc)*cos(angle))-((y2-yc)*sin(angle))+xc
      ys2=((x2-xc)*sin(angle))+((y2-yc)*cos(angle))+yc
      x2s=((x3-xc)*cos(angle))-((y3-yc)*sin(angle))+xc
      y2s=((x3-xc)*sin(angle))+((y3-yc)*cos(angle))+yc
      return (round(xs),round(ys),round(x1s),round(y1s),round(xs2),round(ys2),round(x2s),round(y2s))
    else:
      return (round(xs),round(ys),round(x1s),round(y1s))  
  def move_to(self,x=0,y=0,artefacts=False):
    x1,y1=self.coords()
    self.move(int(x-x1),int(y-y1),artefacts=artefacts)
    for i in self.grouped:
      i.move_to(x=x,y=y,artefacts=artefacts)
  def hide(self):
    self.path=ImageTk.PhotoImage(Image.new("RGBA",(100,100)),master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.update()
    for i in self.grouped:
      i.hide()
  def show(self):
    self.path=ImageTk.PhotoImage(self.imag,master=self.w)
    self.rec=self.c.create_image((self.x1-self.x)//2,(self.y1-self.y)//2,image=self.path)
    self.scale(x=self.scalex,y=self.scaley)
    self.rotate(self.angle)
    self.update()
    for i in self.grouped:
      i.show()
  def group(self,*obj):#you should call mother element
    for i in range(len(obj)):
      self.grouped.append(obj[i])
  def ungroup(self,*obj):
    self.grouped=[]
