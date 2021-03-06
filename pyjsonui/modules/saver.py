import json as j
keys=['bg','bginfo','fullscreen','icon','istool','title','topmost','transparency','windowsize','looped']
bout=['100x100','pyuijson','ICO_OR_PNG_IMAGE',1,False,False,False,'"COLOR" OR "IMAGE"',"white",True]
data={}
to_write=[]
def save(*obj,filename='auto'):
  global data,towrite
  for i in obj:
    objects_tosave=i._get()
    print(i,obj)
    objects_data=i._get_type()
    objinfo=str(i)
    if objects_data=='app':
      data=dict(info=dict(bg=objects_tosave[0],bginfo=objects_tosave[1],fullscreen=objects_tosave[2],icon=objects_tosave[3],istool=objects_tosave[4],title=objects_tosave[5],topmost=objects_tosave[6],transparency=objects_tosave[7],windowsize=objects_tosave[8]))
    elif objects_data=='button':
      data=dict(info=dict(bg=objects_tosave[0],size=objects_tosave[1],place=objects_tosave[2],text=objects_tosave[3],image=objects_tosave[4],animation=objects_tosave[5]))
    if filename=='auto':
        name=objinfo[len(objinfo)-13:len(objinfo)-1]
    else:
      name = filename
      data[objects_data+str(name)]=data.pop('info')
      with open(name +'.json','w') as dtsv:
       j.dump(data,dtsv)
def _load(app):
  with open(str(app)+'.json','r+') as f:
    return j.load(f)
def _upd(app):
  dicta=_load(app)
  for i in keys:
    if not (i in dicta['app'+str(app)].keys()):
      dicta['app'+str(app)][i]=bout[keys.index(i)]
  with open(app +'.json','w') as dtsv:
      j.dump(dicta,dtsv)
