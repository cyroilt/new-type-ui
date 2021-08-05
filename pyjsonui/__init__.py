from .modules import app  as _app
from .modules import button  as _bt
from .modules import canvas  as _canv
from .modules import physics as _ph
from .modules import saver  as _save
from .modules import console as _cmd
from time import sleep
class console():
  def colorize(*w,**kw):
    return _cmd.format(*w,**kw)
  def color_line(*w,**kw):
    return _cmd.format_line(*w,**kw)
  def clear_all():
    _cmd.clear_all()
  def clear_line():
    _cmd.clear_line()
  class progressbar():
    def __init__(self,*w,**kw):
      self.pro=_cmd.progressbar(*w,**kw)
    def update(self,percent):
      self.pro.update(percent)
  def load_image(img,descent=(1,1)):
    _cmd.image_opener(img,descent=(1,1))
class app():
  def __init__(self,**dt):
    self._app=_app.app(**dt)
  def loop(self):
    self._app.loop()
  def kill(self):
    self._app.kill()
  def configure(self,**dt):
    self._app.configure(**dt)
  def bind(self,*dt,**dt2):
    self._app.bind(*dt,**dt2)
  def _get(self):
    return self._app._get()
  def _get_type(self):
    return self._app._get_type()
  def _mw(self):
    return self._app._mw() 
def save(self,filename='auto'):
    return _save.save(self,filename=filename)
def load(filename):
    dt=_save._load(filename)
    for i in dt.keys():
      if i=='app'+str(filename):
        a1=dt[i]
        return app(bg=a1['bg'],bginfo=a1['bginfo'],fullscreen=a1['fullscreen'],icon=a1['icon'],istool=a1['istool'],title=a1['title'],topmost=a1['topmost'],transparency=a1['transparency'],windowsize=a1['windowsize'])
def update(filename):
  _save._upd(filename)
class button():
  def __init__(self,*kw,**dt):
    self._bt=_bt.button(*kw,**dt)
  def kill(self):
    self._bt._kill()
  def refunc(self,func):
    self._bt.refunc(func)
  def restyle(self,**nn):
    self._bt.restyle(**nn)
class canvas():
  def __init__(self,*ar,**kw):
    self._canv=_canv.canvas(*ar,**kw)
  def get_win(self):
    return self._canv.get_win()
  def get_c(self):
    return self._canv.get_c()
  def bind(self,*dt,**dt2):
    self._canv.bind(*dt,**dt2)
class rectangle():
  def __init__(self,*ar,**kw):
    self._rec=_canv.rectangle(*ar,**kw)
  def rotate(self,degree):
    self._rec.rotate(degree)
  def scale(self,x,y):
    self._rec.scale(x,y)
  def update(self):
    self._rec.update()
  def move(self,*ar,**kw):
    self._rec.move(*ar,**kw)
  def pos(self):
    return self._rec.pos()
  def coords(self):
    return self._rec.coords()
  def points(self,all=False):
    return self._rec.points(all=all)
  def move_to(self,*args,**kw):
    self._rec.move_to(*args,**kw)
  def hide(self):
    self._rec.hide()
  def show(self):
    self._rec.show()
  def group(self,*el):
    self._rec.group(*el)
  def ungroup(self):
    self._rec.group()
  def colorize(self,*d,**dd):
    self._rec.colorize(*d,**dd)
class oval():
  def __init__(self,*ar,**kw):
    self._ov=_canv.oval(*ar,**kw)
  def rotate(self,degree):
    self._ov.rotate(degree)
  def scale(self,x,y):
    self._ov.scale(x,y)
  def update(self):
    self._ov.update()
  def move(self,*ar,**kw):
    self._ov.move(*ar,**kw)
  def pos(self):
    return self._ov.pos()
  def coords(self):
    return self._ov.coords()
  def points(self,all=False):
    return self._ov.points(all=all)
  def move_to(self,*args,**kw):
    self._ov.move_to(*args,**kw)
  def hide(self):
    self._ov.hide()
  def show(self):
    self._ov.show()
  def group(self,*el):
    self._ov.group(*el)
  def ungroup(self):
    self._ov.group()
class rounded_rectangle():
  def __init__(self,*ar,**kw):
    self._rr=_canv.rounded_rectangle(*ar,**kw)
  def rotate(self,degree):
    self._rr.rotate(degree)
  def scale(self,x,y):
    self._rr.scale(x,y)
  def update(self):
    self._rr.update()
  def move(self,*ar,**kw):
    self._rr.move(*ar,**kw)
  def pos(self):
    return self._rr.pos()
  def coords(self):
    return self._rr.coords()
  def points(self,all=False):
    return self._rr.points(all=all)
  def move_to(self,*args,**kw):
    self._rr.move_to(*args,**kw)
  def hide(self):
    self._rr.hide()
  def show(self):
    self._rr.show()
  def group(self,*el):
    self._rr.group(*el)
  def ungroup(self):
    self._rr.group()
class arc():
  def __init__(self,*ar,**kw):
    self._ar=_canv.arc(*ar,**kw)
  def rotate(self,degree):
    self._ar.rotate(degree)
  def scale(self,x,y):
    self._ar.scale(x,y)
  def update(self):
    self._ar.update()
  def move(self,*ar,**kw):
    self._ar.move(*ar,**kw)
  def pos(self):
    return self._ar.pos()
  def coords(self):
    return self._ar.coords()
  def points(self,all=False):
    return self._ar.points(all=all)
  def move_to(self,*args,**kw):
    self._ar.move_to(*args,**kw)
  def hide(self):
    self._ar.hide()
  def show(self):
    self._ar.show()
  def group(self,*el):
    self._ar.group(*el)
  def ungroup(self):
    self._ar.group()
class gravitation():
  def __init__(self,**kw):
    self.gr=_ph.gravitation(**kw)
  def set_speed(self,**kw):
    self.gr.set_speed(**kw)
  def set_height(self,**kw):
    self.gr.set_height(**kw)
  def get_result(self):
    return self.gr.get_result()
  def get_moment(self,**kw):
    return self.gr.get_moment(**kw)
  def set_floor(self,y):
    self.gr.setfloor(y)
class line():
  def __init__(self,*ar,**kw):
    self._ln=_canv.line(*ar,**kw)
  def rotate(self,degree):
    self._ln.rotate(degree)
  def scale(self,x,y):
    self._ln.scale(x,y)
  def update(self):
    self._ln.update()
  def move(self,*ar,**kw):
    self._ln.move(*ar,**kw)
  def pos(self):
    return self._ln.pos()
  def coords(self):
    return self._ln.coords()
  def points(self,all=False):
    return self._ln.points(all=all)
  def move_to(self,*args,**kw):
    self._ln.move_to(*args,**kw)
  def hide(self):
    self._ln.hide()
  def show(self):
    self._ln.show()
  def group(self,*el):
    self._ln.group(*el)
  def ungroup(self):
    self._ln.group()
class electricy():
  def __init__(self,*info,**subinfo):
    self._electr=_ph.electricy(*info,**subinfo)
  def get_ro(self):
    return self._electr.get_ro()
  def change_wire(self,**mmm):
    self._electr.change_wire(**mmm)