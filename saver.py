import json as j

data={}
def save(obj,filename='auto'):
  global data
  objects_tosave=obj._get()
  objects_data=obj._get_type()
  objinfo=str(obj)
  data=dict(info=dict(bg=objects_tosave[0],bginfo=objects_tosave[1],fullscreen=objects_tosave[2],icon=objects_tosave[3],istool=objects_tosave[4],title=objects_tosave[5],topmost=objects_tosave[6],transparency=objects_tosave[7],windowsize=objects_tosave[8]))
  data[objects_data]=data.pop('info')
  if filename=='auto':
    name=objinfo[len(objinfo)-13:len(objinfo)-1]
  else:
    name = filename
  with open(name +'.json','w') as dtsv:
    j.dump(data,dtsv)
def _load(app):
  with open(str(app)+'.json','r+') as f:
    return j.load(f)
