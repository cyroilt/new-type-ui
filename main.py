import app as _app
import saver as _save
import button as _bt
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
def save(self,filename='auto'):
    return _save.save(self,filename=filename)
def load(filename):
    dt=_save._load(filename)
    for i in dt.keys():
      if i=='app':
        a1=dt[i]
        return app(bg=a1['bg'],bginfo=a1['bginfo'],fullscreen=a1['fullscreen'],icon=a1['icon'],istool=a1['istool'],title=a1['title'],topmost=a1['topmost'],transparency=a1['transparency'],windowsize=a1['windowsize'])
def _mw(self):
  return _app._mw() 
class button():
  def __init__(self,*kw,**dt):
    self._bt=_bt.button(*kw,**dt)
a=load('1')
b=button(a._mw())
a.loop()