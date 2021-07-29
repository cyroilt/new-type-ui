from tkinter import *
from PIL import Image,ImageTk
from functools import partial
from json import *
import time
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
  def __init__(self,windowsize='100x100',title='pyuijson',icon='ICO_OR_PNG_IMAGE',transparency=1,fullscreen=False,istool=False,topmost=False,bg='"COLOR" OR "IMAGE"',bginfo="white"):
        global names,paths,images
        window=Tk()
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
          mybackground=Canvas(bg=bginfo,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          mybackground.pack()
          mybackground.place(x=0,y=0)
        else:
          mybackground=Canvas(height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          mybackground.pack()
          mybackground.place(x=0,y=0)
          semiimages=Image.open(bginfo)
          x,y=windowsize.split('x')
          x,y=int(x),int(y)
          self.lx,self.ly=x,y
          semiimages=semiimages.resize((x,y),Image.NEAREST)
          images=ImageTk.PhotoImage(semiimages,master=mybackground)
          im=mybackground.create_image(semiimages.size[0]//2,semiimages.size[1]//2,image=images)
        self.window=window
        self.bg=bg
        self.mybackground=mybackground
        self.bginfo=bginfo
        self.im=im
        
        self.title,self.icon,self.transparency,self.fullscreen,self.istool,self.topmost,self.windowsize=title,icon,transparency,fullscreen,istool,topmost,windowsize
        self.mybackground.update()
        self.autocheck()
        
  def loop(self):
    self.window.mainloop()
  def autoresize(self,e):
    global images
    if e.widget==self.mybackground:
      return 0
    if self.bg=='"COLOR" OR "IMAGE"' or self.bg=='COLOR':
          self.mybackground.configure(width=e.width,height=e.height)
    else:
          self.mybackground.configure(width=e.width,height=e.height)
          semiimages=Image.open(self.bginfo)
          x,y=e.width,e.height
          semiimages=semiimages.resize((x,y),Image.NEAREST)
          images=ImageTk.PhotoImage(semiimages)
          self.mybackground.itemconfigure(self.im,image=images)
          self.mybackground.move(self.im,(x-self.lx)//2,(y-self.ly)//2)
          self.lx,self.ly=x,y
          self.mybackground.update()
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
          mybackground=Canvas(bg=bginfo,height=windowsize.split('x')[1],width=windowsize.split('x')[0])
          mybackground.pack()
          mybackground.place(x=0,y=0)
        else:
          mybackground=Canvas(height=windowsize.split('x')[1],width=windowsize.split('x')[0])
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
    print('hi')
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