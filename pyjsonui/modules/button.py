from tkinter import*
from PIL import Image,ImageTk,ImageEnhance,ImageDraw
animations=['lighter']
buttons=[]
buttonsapply=[]
buttonssizes=[]
class button():
  def __init__(self,app,size='50x25',place=None,text='',image=None,function=None,withoutput=False,animation=None,switcher=None,autoresize=False,onreleasef=None,onreleasout=False,bg='#004DFF'):
    window=app._mw()
    self.window=window
    self.size=size
    x,y=size.split('x')
    if image==None:
      self.image=Image.new('RGB', (int(x),int(y)), color =bg)
    else:
      self.image=Image.open(image)
    self.drawer=ImageDraw.Draw(self.image)
    self.drawer.text((self.image.size[0]//4,self.image.size[1]//4),fill='black',text=text)
    self.tkim=ImageTk.PhotoImage(self.image,master=window)
    self.counterpr=0
    self.counterre=0
    self.enh = ImageEnhance.Brightness(self.image)
    sizex,sizey=size.split('x')
    self.sizex,self.sizey=int(sizex),int(sizey)
    self.obj=Canvas(window,height=self.sizey,width=self.sizex)
    self.obj.pack()
    self.bg=self.obj.create_image(self.image.size[0]//2,self.image.size[1]//2,image=self.tkim)
    buttonssizes.append((self.sizex,self.sizey))
    buttons.append(self.obj)
    self.function=function
    if autoresize==True:
      buttonsapply.append(self.obj)
    if place!=None:
      coordx,coordy=place.split('x')
      self.coordx,self.coordy=int(coordx),int(coordy)
      self.obj.place(x=self.coordx,y=self.coordy)
    def doing(e):
      self.counterpr+=1
      if animation==animations[0]:
        self.obj.delete(self.bg)
        self.image=self.enh.enhance(1.5)
        self.tkim=ImageTk.PhotoImage(self.image,master=window)
        self.bg=self.obj.create_image(self.image.size[0]//2,self.image.size[1]//2,image=self.tkim)
      if self.function!=None:
        if withoutput:
          identify=str(self)
          self.function(('pyuijson-Button'+identify[len(identify)-13:len(identify)-1]+'Press',self.counterpr))
        else:
          self.function()
    def realdoing(e):
      self.counterre+=1
      if animation==animations[0]:
        self.obj.delete(self.bg)
        self.image=self.enh.enhance(1)
        self.tkim=ImageTk.PhotoImage(self.image,master=window)
        self.bg=self.obj.create_image(self.image.size[0]//2,self.image.size[1]//2,image=self.tkim)
      if onreleasef!=None:
        if onreleasout:
          identify=str(self)
          onreleasef(('pyuijson-Button'+identify[len(identify)-13:len(identify)-1]+'Release',self.counterre))
          

        else:
          onreleasef()
    self.obj.bind('<Button-1>',doing)
    self.obj.bind('<ButtonRelease-1>',realdoing)
  def refunc(self,function):
    self.function=function
  def _kill(self):
    self.obj.destroy()
  def restyle(self,text='',image=None,bg='#FFFFFF'):
    if image==None:
      self.image=Image.new('RGB', (self.sizex,self.sizey), color =bg)
    else:
      self.image=Image.open(image)
    self.drawer=ImageDraw.Draw(self.image)
    self.drawer.text((self.image.size[0]//4,self.image.size[1]//4),fill='black',text=text)
    self.tkim=ImageTk.PhotoImage(self.image,master=self.window)
    self.counterpr=0
    self.counterre=0
    self.enh = ImageEnhance.Brightness(self.image)
    self.bg=self.obj.create_image(self.image.size[0]//2,self.image.size[1]//2,image=self.tkim)
    self.obj.update()