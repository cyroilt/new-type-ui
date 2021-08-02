from pyjsonui import *
a=app(windowsize='1000x1000',title='py_electro')
c=canvas(a,size='1000x1000')
els=[]
elsln=[]
for i in range(20):
  for j in range(20):
    elsln.append(rectangle(c,i*50,j*50,i*50+50,j*50+50,width=2))
  els.append(elsln)
  els[i][j].update()
print('ok')
a.loop()