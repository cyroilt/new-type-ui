from tkinter import *
from PIL import Image,ImageTk,ImageSequence
from functools import partial
from json import *
from . import button
import time
from threading import Thread
names=[]
paths=[]
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
images=0
class app():
  def generate_gradient(self,c1='', c2='', w=0, h=0):
    width=w
    height=h
    colour1=c1
    colour2=c2
    """Generate a vertical gradient."""
    base = Image.new('RGBA', (width, height), colour1)
    top = Image.new('RGBA', (width, height), colour2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base
  def gificoplayer(self,file=None):
    im = Image.open(file)
    while True:
      for frame in ImageSequence.Iterator(im):
        self.window.iconphoto(False,ImageTk.PhotoImage(frame,master=self.window))
        time.sleep(0.01)
        
  def gifbgplayer(self,file=None,im=0,mybg=0):
    im2 = Image.open(file)
    self.frame=None
    x1,y1=self.windowsize.split('x')
    x1,y1=int(x1),int(y1)
    while True:
      mybg.update()
      for frame in ImageSequence.Iterator(im2):
        x,y=self.windowsize.split('x')
        xf=int(x)
        kf=int(y)/y1
        x,y=int(x1*kf),int(y)
        self.frame=frame.resize((x,y),Image.NEAREST)
        self.image=ImageTk.PhotoImage(self.frame,master=mybg)
        mybg.create_image(self.frame.size[0]//2+(int(xf)-self.frame.size[0])//2,self.frame.size[1]//2,image=self.image)
        time.sleep(0.01)
        mybg.update()
      for i in mybg.find_all():
        mybg.delete(i)
  def __init__(self,windowsize='100x100',title='pyuijson',icon='ICO_OR_PNG_IMAGE',transparency=1,fullscreen=False,istool=False,topmost=False,bg='"COLOR" OR "IMAGE" OR "GRADIENT"',bginfo="white",onclosefunc=None):
        global names,paths,images
        self.window=Tk()
        self.looped=onclosefunc
        def on_closing():
          if self.looped!=None:
            self.looped()
          self.window.destroy()
        self.window.protocol("WM_DELETE_WINDOW", on_closing)
        if 'icon.png' in paths:
              pass
        else:
              paths.append('icon.png')
              names.append(PhotoImage(file='icon.png'))
        if icon!='ICO_OR_PNG_IMAGE':
          if icon.find('.gif')==-1:
            if icon in paths:
              myicon=names[paths.index(icon)]
            else:
              paths.append(icon)
              names.append(PhotoImage(file=icon))
              myicon=names[paths.index(icon)]
            try:
              self.window.call('wm', 'iconphoto', window._w, myicon)
            except:
              self.window.iconphoto(False,PhotoImage(file=icon,master=self.window))
          else:
            self.gifpl=Thread(target=self.gificoplayer,kwargs={'file':icon})
            self.gifpl.start()
        else:
            imgpyuijson=names[0]
            try:
              self.window.call('wm', 'iconphoto', window._w, imgpyjson)
            except:
              self.window.iconphoto(False,PhotoImage(file='icon.png',master=self.window))
        self.window.title(title)
        x,y=windowsize.split('x')
        x,y=int(x),int(y)
        self.lx,self.ly=x,y
        self.window.geometry(windowsize)
        try:
          self.window.call("wm", "attributes", ".", "-alpha", str(transparency/100))
        except:
          print("your system doesn't support transparency method")
        try:
          self.window.call("wm", "attributes", ".", "-fullscreen", fullscreen)
        except:
          print("your system doesn't support fullscreen method")
        try:
          self.window.call("wm", "attributes", ".", "-toolwindow", istool)
        except:
          print("your system doesn't support tool window method")
        try:
          self.window.call("wm", "attributes", ".", "-topmost", topmost)
        except:
          print("your system doesn't support topmost method")
        bg=bg.upper()
        im=0
        if bg=='"COLOR" OR "IMAGE" OR "GRADIENT"' or bg=='COLOR':
          self.mybackground=Canvas(self.window,bg=bginfo,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          self.mybackground.pack()
          self.mybackground.place(x=0,y=0)
        elif bg=='GRADIENT':
          self.mybackground=Canvas(self.window,height=windowsize.split('x')[1]*3,width=windowsize.split('x')[0])
          self.mybackground.pack()
          self.mybackground.place(x=0,y=0)
          gradientfr=bginfo[0]
          gradientto=bginfo[1]
          x,y=windowsize.split('x')
          x,y=int(x),int(y)
          self.lx,self.ly=x,y
          semiimages=self.generate_gradient(c1=gradientfr,c2=gradientto,w=x,h=y)
          images=ImageTk.PhotoImage(semiimages,master=self.mybackground)
          im=self.mybackground.create_image(semiimages.size[0]//2,semiimages.size[1]//2,image=images)
        else:

          self.mybackground=Canvas(self.window,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          self.mybackground.pack()
          self.mybackground.place(x=0,y=0)
          semiimages=Image.open(bginfo)
          x,y=windowsize.split('x')
          x,y=int(x),int(y)
          self.lx,self.ly=x,y
          semiimages=semiimages.resize((x,y),Image.NEAREST)
          images=ImageTk.PhotoImage(semiimages,master=self.mybackground)
          im=self.mybackground.create_image(semiimages.size[0]//2,semiimages.size[1]//2,image=images)
        self.bg=bg
        self.bginfo=bginfo
        self.im=im
        self.title,self.icon,self.transparency,self.fullscreen,self.istool,self.topmost,self.windowsize=title,icon,transparency,fullscreen,istool,topmost,windowsize
        try:
          if self.bginfo.find('.gif')!=-1:
            self.gifpl2=Thread(target=self.gifbgplayer,kwargs={'file':self.bginfo,'im':self.im,'mybg':self.mybackground})
            self.gifpl2.start()
        except:
          pass
        
        
        
        self.mybackground.update()
        self.autocheck()
        
  def loop(self):
    self.window.mainloop()
  def autoresize(self,e):
    global images
    if e.widget!=self.window or e.widget in button.buttons:
      return 0
    if self.bg=='"COLOR" OR "IMAGE" OR "GRADIENT"' or self.bg=='COLOR':
          self.mybackground.configure(width=e.width,height=e.height)
    elif self.bg=='GRADIENT':
          self.mybackground.configure(width=e.width,height=e.height)
          gradientfr=self.bginfo[0]
          gradientto=self.bginfo[1]
          x,y=e.width,e.height
          x,y=int(x),int(y)
          semiimages=self.generate_gradient(c1=gradientfr,c2=gradientto,w=x,h=y)
          images=ImageTk.PhotoImage(semiimages,master=self.mybackground)
          self.mybackground.itemconfigure(self.im,image=images)
          self.mybackground.move(self.im,(x-self.lx)//2,(y-self.ly)//2)
          self.lx,self.ly=x,y
          
          
          
    else:
          self.mybackground.configure(width=e.width,height=e.height)
          semiimages=Image.open(self.bginfo)
          x,y=e.width,e.height
          semiimages=semiimages.resize((x,y),Image.NEAREST)
          images=ImageTk.PhotoImage(semiimages)
          self.mybackground.itemconfigure(self.im,image=images)
          self.mybackground.move(self.im,(x-self.lx)//2,(y-self.ly)//2)
          self.lx,self.ly=x,y
          self.windowsize=str(x)+'x'+str(y)
          self.mybackground.update()
    for i in button.buttonsapply:
      sizea1,sizea2=self.windowsize.split('x')
      sizea1,sizea2=int(sizea1),int(sizea2)
      k1=sizea1/e.width
      k2=sizea2/e.height
      if k1>k2 and k2!=0:
        k1=k2
      elif k1!=0 and k2>k1:
        k2=k1
      k1=k1*2
      i['width']=button.buttonssizes[button.buttonsapply.index(i)][0]*(k1)
      i['height']=button.buttonssizes[button.buttonsapply.index(i)][1]*(k1)
      print(i['height'],i['width'],k1)
  def autocheck(self):
    self.window.bind('<Configure>',self.autoresize)
  def configure(self,**k):

        
        window=self.window
        if 'topmost' in k.keys():
          topmost=k['topmost']
        else:
          topmost=self.topmost
        if 'windowsize' in k.keys():
          windowsize=k['windowsize']
        else:
          windowsize=self.windowsize
        if 'bg' in k.keys():
          bg=k['bg']
        else:
          bg=self.bg
        if 'bginfo' in k.keys():
          bginfo=k['bginfo']
        else:
          bginfo=self.bginfo
        if 'title' in k.keys():
          title=k['title']
        else:
          title=self.title
        if 'icon' in k.keys():
          icon=k['icon']
        else:
          icon=self.icon
        if 'transparency' in k.keys():
          transparency=k['transparency']
        else:
          transparency=self.transparency
        if 'fullscreen' in k.keys():
          fullscreen=k['fullscreen']
        else:
          fullscreen=self.fullscreen
        if 'istool' in k.keys():
          istool=k['istool']
        else:
          istool=self.istool
        if 'icon.png' in paths:
              pass
        else:
              paths.append('icon.png')
              names.append(PhotoImage(file='icon.png'))
        if icon!='ICO_OR_PNG_IMAGE':
            if icon in paths:
              myicon=names[paths.index(icon)]
            else:
              paths.append(icon)
              names.append(PhotoImage(file=icon))
              myicon=names[paths.index(icon)]
            window.call('wm', 'iconphoto', window._w, myicon)
        else:
            imgpyuijson=names[0]
            window.call('wm', 'iconphoto', window._w, imgpyuijson)
        window.title(title)
        window.geometry(windowsize)
        try:
          window.call("wm", "attributes", ".", "-alpha", str(transparency))
        except:
          print("your system doesn't support transparency method")
        try:
          window.call("wm", "attributes", ".", "-fullscreen", fullscreen)
        except:
          print("your system doesn't support fullscreen method")
        try:
          window.call("wm", "attributes", ".", "-toolwindow", istool)
        except:
          print("your system doesn't support tool window method")
        try:
          window.call("wm", "attributes", ".", "-topmost", topmost)
        except:
          print("your system doesn't support topmost method")
        bg=bg.upper()
        im=0
        if bg=='"COLOR" OR "IMAGE"' or bg=='COLOR':
          mybackground=Canvas(window,bg=bginfo,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          mybackground.pack()
          mybackground.place(x=0,y=0)
        else:
          mybackground=Canvas(window,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          mybackground.pack()
          mybackground.place(x=0,y=0)
          semiimages=Image.open(bginfo)
          x,y=windowsize.split('x')
          x,y=int(x),int(y)
          self.lx,self.ly=x,y
          semiimages=semiimages.resize((x,y),Image.NEAREST)
          images=ImageTk.PhotoImage(semiimages,master=mybackground)
          im=mybackground.create_image(semiimages.size[0]//2,semiimages.size[1]//2,image=images)
          mybackground.update()
        self.bg=bg
        self.mybackground=mybackground
        self.bginfo=bginfo
        self.im=im
        
        self.title,self.icon,self.transparency,self.fullscreen,self.istool,self.topmost,self.windowsize=title,icon,transparency,fullscreen,istool,topmost,windowsize
  def kill(self,afterdeathfunc=None):
    self.window.destroy()
    print('window destroyed')
    if afterdeathfunc!=None:
      afterdeathfunc()

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
      self.window.bind(rules[rule],doing)
    else:
      self.window.bind('<'+str(rule)+'>',doing)
  def _get(self):
    return self.bg,self.bginfo,self.fullscreen,self.icon,self.istool,self.title,self.topmost,self.transparency,self.windowsize
  def _get_type(self):
    return 'app'
  def _mw(self):
    return self.window