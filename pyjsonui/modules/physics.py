from math import sin,cos,sqrt
materials=['platinum', 'silver', 'iron', 'copper', 'aluminum','gold']
materials_ro=[0.107,0.015,0.09,0.017,0.026,0.023]
class gravitation():
  def __init__(self,g=9.8,k=0.5):
    self.g=g
    self.k=k
    self.t=0
    self.y=0
    self.x=0
  def set_speed(self,v=0,angle=0):
    self.vx=abs(v*cos(angle))
    self.vy=abs(v*sin(angle))
  def set_height(self,h=1):
    self.h=h
    self.t=sqrt(self.h/self.g)+self.vy/self.g
    self.s=self.vx*self.t-(self.g*self.t**2)/2
    self.vyk=self.g*self.t-self.vy
  def setfloor(self,y,start=200):
    self.floor=y+start
  def get_result(self):
    return {'time':self.t,'distance':self.s,'last speed ':self.vyk}
  def get_moment(self,t=1,part=0.1,timepart=1):
    if self.h>0:
      self.x=self.vx*timepart*t
      self.vy+=self.g*timepart*t
      self.h-=self.vy
    else:
      self.vy=-1*self.vy*self.k
      self.h-=self.vy
    return {'distance':self.x,'falling speed':self.vy,'height':self.h}
class electricy():
  def __init__(self,input_U,material='copper'):
    self.Ustart=input_U
    self.ro_cable=materials_ro[materials.index(material)]
  def get_ro(self):
    return self.ro_cable
  def change_wire(self,material='copper'):
    self.ro_cable=materials_ro[materials.index(material)]
    