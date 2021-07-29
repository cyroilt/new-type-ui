from tkinter import*
animations={}
class button():
  def __init__(self,wp,size='50x50',place=None,text=None,image=None,function=None,withoutput=False,animation=None,switcher=None):
    window=wp
    sizex,sizey=size.split('x')
    self.sizex,self.sizey=int(sizex),int(sizey)
    obj=Canvas(window,height=self.sizey,width=self)
    obj.pack()
    if place!=None:
      coordx,coordy=place.split('x')
      self.coordx,self.coordy=int(coordx),int(coordy)
      obj.place(x=self.coordx,y=self.coordy)