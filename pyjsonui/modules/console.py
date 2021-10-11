import os
import sys 
import difflib
from curses import *
from threading import Thread
bindings={}
def divide(input, n=2):
    size=n
    input_size = len(input)
    slice_size = input_size // size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(next(iterator))
        if remain:
            result[i].append(next(iterator))
            remain -= 1
    return result
  
styles={'classic':'1','dark':'2','italic':'3','underline':'4','switchbg':'7','hiddentext':'8'}
tkcolors={'snow': '#fffdfd', 'ghost white': '#fcfcff', 'white smoke': '#fafafa', 'gainsboro': '#ededed', 'floral white': '#fffdf8', 'old lace': '#fefaf3', 'linen': '#fdf8f3', 'antique white': '#fdf5eb', 'papaya whip': '#fff7e9', 'blanched almond': '#fff5e5', 'bisque': '#fff2e0', 'peach puff': '#ffecda', 'navajo white': '#ffeed2', 'lemon chiffon': '#fffde5', 'mint cream': '#fafffd', 'azure': '#f8ffff', 'alice blue': '#f8fcff', 'lavender': '#f3f3fd', 'lavender blush': '#fff8fa', 'misty rose': '#fff2f0', 'dark slate gray': '#6d8e8e', 'dim gray': '#a4a4a4', 'slate gray': '#a9b5c0', 'light slate gray': '#aebac6', 'gray': '#b5b5b5', 'light grey': '#e8e8e8', 'midnight blue': '#5050a9', 'navy': '#0000b5', 'cornflower blue': '#a0c3f6', 'dark slate blue': '#887dbd', 'slate blue': '#a598e5', 'medium slate blue': '#b1a3f7', 'light slate blue': '#b8a9ff', 'medium blue': '#0000e5', 'royal blue': '#81a4f0', 'blue': '#0000ff', 'dodger blue': '#57c0ff', 'deep sky blue': '#00ddff', 'sky blue': '#bae6f5', 'light sky blue': '#bae6fd', 'steel blue': '#86b6d7', 'light steel blue': '#d4e0ee', 'light blue': '#d2ebf3', 'powder blue': '#d4eff3', 'pale turquoise': '#d4f7f7', 'dark turquoise': '#00e6e7', 'medium turquoise': '#88e7e4', 'turquoise': '#80efe7', 'cyan': '#00ffff', 'light cyan': '#efffff', 'cadet blue': '#9cc9ca', 'medium aquamarine': '#a1e5d1', 'aquamarine': '#b4ffe9', 'dark green': '#00a000', 'dark olive green': '#93a56d', 'dark sea green': '#bfdbbf', 'sea green': '#6cbd95', 'medium sea green': '#7cd6aa', 'light sea green': '#5ad5d1', 'pale green': '#c5fdc5', 'spring green': '#00ffb4', 'lawn green': '#b2fe00', 'medium spring green': '#00fdc6', 'green yellow': '#d2ff6d', 'lime green': '#71e571', 'yellow green': '#c6e571', 'forest green': '#5dbd5d', 'olive drab': '#a5bf5e', 'dark khaki': '#dcd8a5', 'khaki': '#f8f3bd', 'pale goldenrod': '#f7f4d1', 'light goldenrod yellow': '#fdfde8', 'light yellow': '#ffffef', 'yellow': '#ffff00', 'gold': '#ffeb00', 'light goldenrod': '#f7eeb6', 'goldenrod': '#eccd5a', 'dark goldenrod': '#d9b935', 'rosy brown': '#dbbfbf', 'indian red': '#e59999', 'saddle brown': '#bd8545', 'sandy brown': '#facd9d', 'dark salmon': '#f4c4b1', 'salmon': '#fdb5ab', 'light salmon': '#ffcab1', 'orange': '#ffcd00', 'dark orange': '#ffbd00', 'coral': '#ffb48f', 'light coral': '#f8b5b5', 'tomato': '#ff9f87', 'orange red': '#ff8500', 'red': '#ff0000', 'hot pink': '#ffa4d7', 'deep pink': '#ff47c2', 'pink': '#ffdee4', 'light pink': '#ffd8de', 'pale violet red': '#eda9c2', 'maroon': '#b50000', 'medium violet red': '#e249b8', 'violet red': '#e75ac0', 'medium orchid': '#da93e8', 'dark orchid': '#c671e4', 'dark violet': '#c300e8', 'blue violet': '#bc69f1', 'purple': '#b500b5', 'medium purple': '#c2a9ed', 'thistle': '#ebddeb', 'snow2': '#f7f4f4', 'snow3': '#e5e3e3', 'snow4': '#bdbbbb', 'seashell2': '#f7f2ee', 'seashell3': '#e5e1dd', 'seashell4': '#bdb9b6', 'AntiqueWhite1': '#fff7ed', 'AntiqueWhite2': '#f7efe4', 'AntiqueWhite3': '#e5ded4', 'AntiqueWhite4': '#bdb7af', 'bisque2': '#f7e9d8', 'bisque3': '#e5d8c9', 'bisque4': '#bdb3a5', 'PeachPuff2': '#f7e4d2', 'PeachPuff3': '#e5d4c3', 'PeachPuff4': '#bdaea1', 'NavajoWhite2': '#f7e6cb', 'NavajoWhite3': '#e5d6bd', 'NavajoWhite4': '#bdb09b', 'LemonChiffon2': '#f7f4dd', 'LemonChiffon3': '#e5e3cd', 'LemonChiffon4': '#bdbba9', 'cornsilk2': '#f7f4e5', 'cornsilk3': '#e5e2d5', 'cornsilk4': '#bdbaaf', 'ivory2': '#f7f7ef', 'ivory3': '#e5e5de', 'ivory4': '#bdbdb7', 'honeydew2': '#eff7ef', 'honeydew3': '#dee5de', 'honeydew4': '#b7bdb7', 'LavenderBlush2': '#f7eff2', 'LavenderBlush3': '#e5dee1', 'LavenderBlush4': '#bdb7b9', 'MistyRose2': '#f7e9e8', 'MistyRose3': '#e5d8d7', 'MistyRose4': '#bdb3b1', 'azure2': '#eff7f7', 'azure3': '#dee5e5', 'azure4': '#b7bdbd', 'SlateBlue1': '#b7a8ff', 'SlateBlue2': '#b1a2f7', 'SlateBlue3': '#a497e5', 'SlateBlue4': '#877cbd', 'RoyalBlue1': '#88aeff', 'RoyalBlue2': '#83a8f7', 'RoyalBlue3': '#7a9ce5', 'RoyalBlue4': '#6480bd', 'blue2': '#0000f7', 'blue4': '#0000bd', 'DodgerBlue2': '#54b9f7', 'DodgerBlue3': '#4eace5', 'DodgerBlue4': '#408dbd', 'SteelBlue1': '#9fd9ff', 'SteelBlue2': '#99d2f7', 'SteelBlue3': '#8ec3e5', 'SteelBlue4': '#75a0bd', 'DeepSkyBlue2': '#00d5f7', 'DeepSkyBlue3': '#00c6e5', 'DeepSkyBlue4': '#00a3bd', 'SkyBlue1': '#bae6ff', 'SkyBlue2': '#b3def7', 'SkyBlue3': '#a6cee5', 'SkyBlue4': '#89a9bd', 'LightSkyBlue1': '#d4f1ff', 'LightSkyBlue2': '#cde8f7', 'LightSkyBlue3': '#bed8e5', 'LightSkyBlue4': '#9db1bd', 'SlateGray1': '#e1f1ff', 'SlateGray2': '#dae8f7', 'SlateGray3': '#cad8e5', 'SlateGray4': '#a6b1bd', 'LightSteelBlue1': '#e3f0ff', 'LightSteelBlue2': '#dbe8f7', 'LightSteelBlue3': '#ccd7e5', 'LightSteelBlue4': '#a8b1bd', 'LightBlue1': '#ddf7ff', 'LightBlue2': '#d5eff7', 'LightBlue3': '#c6dee5', 'LightBlue4': '#a3b7bd', 'LightCyan2': '#e7f7f7', 'LightCyan3': '#d7e5e5', 'LightCyan4': '#b1bdbd', 'PaleTurquoise1': '#dbffff', 'PaleTurquoise2': '#d3f7f7', 'PaleTurquoise3': '#c4e5e5', 'PaleTurquoise4': '#a1bdbd', 'CadetBlue1': '#c5faff', 'CadetBlue2': '#bff2f7', 'CadetBlue3': '#b1e1e5', 'CadetBlue4': '#92b9bd', 'turquoise1': '#00faff', 'turquoise2': '#00f2f7', 'turquoise3': '#00e1e5', 'turquoise4': '#00b9bd', 'cyan2': '#00f7f7', 'cyan3': '#00e5e5', 'cyan4': '#00bdbd', 'DarkSlateGray1': '#c4ffff', 'DarkSlateGray2': '#bef7f7', 'DarkSlateGray3': '#b0e5e5', 'DarkSlateGray4': '#91bdbd', 'aquamarine2': '#aef7e1', 'aquamarine4': '#85bdac', 'DarkSeaGreen1': '#deffde', 'DarkSeaGreen2': '#d7f7d7', 'DarkSeaGreen3': '#c7e5c7', 'DarkSeaGreen4': '#a4bda4', 'SeaGreen1': '#92ffca', 'SeaGreen2': '#8df7c3', 'SeaGreen3': '#83e5b5', 'PaleGreen1': '#c6ffc6', 'PaleGreen2': '#c0f7c0', 'PaleGreen3': '#b2e5b2', 'PaleGreen4': '#92bd92', 'SpringGreen2': '#00f7ae', 'SpringGreen3': '#00e5a1', 'SpringGreen4': '#00bd85', 'green2': '#00f700', 'green3': '#00e500', 'green4': '#00bd00', 'chartreuse2': '#aef700', 'chartreuse3': '#a1e500', 'chartreuse4': '#85bd00', 'OliveDrab1': '#deff7e', 'OliveDrab2': '#d6f77a', 'OliveDrab4': '#a4bd5d', 'DarkOliveGreen1': '#e3ffa9', 'DarkOliveGreen2': '#dbf7a3', 'DarkOliveGreen3': '#cce598', 'DarkOliveGreen4': '#a8bd7d', 'khaki1': '#fffbbf', 'khaki2': '#f7f3b8', 'khaki3': '#e5e1ab', 'khaki4': '#bdb98d', 'LightGoldenrod1': '#fff6bd', 'LightGoldenrod2': '#f7edb6', 'LightGoldenrod3': '#e5dca9', 'LightGoldenrod4': '#bdb68b', 'LightYellow2': '#f7f7e7', 'LightYellow3': '#e5e5d7', 'LightYellow4': '#bdbdb1', 'yellow2': '#f7f700', 'yellow3': '#e5e500', 'yellow4': '#bdbd00', 'gold2': '#f7e300', 'gold3': '#e5d200', 'gold4': '#bdad00', 'goldenrod1': '#ffde61', 'goldenrod2': '#f7d75d', 'goldenrod3': '#e5c756', 'goldenrod4': '#bda447', 'DarkGoldenrod1': '#ffda3e', 'DarkGoldenrod2': '#f7d23b', 'DarkGoldenrod3': '#e5c337', 'DarkGoldenrod4': '#bda12d', 'RosyBrown1': '#ffdede', 'RosyBrown2': '#f7d7d7', 'RosyBrown3': '#e5c7c7', 'RosyBrown4': '#bda4a4', 'IndianRed1': '#ffa5a5', 'IndianRed2': '#f79f9f', 'IndianRed3': '#e59393', 'IndianRed4': '#bd7a7a', 'sienna1': '#ffb687', 'sienna2': '#f7b082', 'sienna3': '#e5a379', 'sienna4': '#bd8762', 'burlywood1': '#ffe8c7', 'burlywood2': '#f7e1c1', 'burlywood3': '#e5d1b3', 'burlywood4': '#bdab93', 'wheat1': '#fff3da', 'wheat2': '#f7ebd3', 'wheat3': '#e5dac4', 'wheat4': '#bdb3a1', 'tan1': '#ffcd8e', 'tan2': '#f7c688', 'tan4': '#bd9869', 'chocolate1': '#ffb460', 'chocolate2': '#f7ae5c', 'chocolate3': '#e5a156', 'firebrick1': '#ff6f6f', 'firebrick2': '#f76a6a', 'firebrick3': '#e56262', 'firebrick4': '#bd5151', 'brown1': '#ff8080', 'brown2': '#f77b7b', 'brown3': '#e57272', 'brown4': '#bd5e5e', 'salmon1': '#ffbda4', 'salmon2': '#f7b69e', 'salmon3': '#e5a992', 'salmon4': '#bd8b79', 'LightSalmon2': '#f7c3ab', 'LightSalmon3': '#e5b69e', 'LightSalmon4': '#bd9582', 'orange2': '#f7c600', 'orange3': '#e5b800', 'orange4': '#bd9800', 'DarkOrange1': '#ffb400', 'DarkOrange2': '#f7ae00', 'DarkOrange3': '#e5a100', 'DarkOrange4': '#bd8500', 'coral1': '#ffab94', 'coral2': '#f7a58f', 'coral3': '#e59885', 'coral4': '#bd7e6d', 'tomato2': '#f79982', 'tomato3': '#e58e79', 'tomato4': '#bd7562', 'OrangeRed2': '#f78000', 'OrangeRed3': '#e57600', 'OrangeRed4': '#bd6100', 'red2': '#f70000', 'red3': '#e50000', 'red4': '#bd0000', 'DeepPink2': '#f744bb', 'DeepPink3': '#e540ae', 'DeepPink4': '#bd328f', 'HotPink1': '#ffa8d7', 'HotPink2': '#f7a5cf', 'HotPink3': '#e59dc0', 'HotPink4': '#bd7a9e', 'pink1': '#ffd7e1', 'pink2': '#f7d0d9', 'pink3': '#e5c1c9', 'pink4': '#bd9fa6', 'LightPink1': '#ffd3da', 'LightPink2': '#f7ccd2', 'LightPink3': '#e5bdc3', 'LightPink4': '#bd9ca1', 'PaleVioletRed1': '#ffb6d1', 'PaleVioletRed2': '#f7b0ca', 'PaleVioletRed3': '#e5a3bb', 'PaleVioletRed4': '#bd879a', 'maroon1': '#ff73d6', 'maroon2': '#f76fcf', 'maroon3': '#e566c0', 'maroon4': '#bd549e', 'VioletRed1': '#ff7ec4', 'VioletRed2': '#f77abd', 'VioletRed3': '#e571af', 'VioletRed4': '#bd5d91', 'magenta2': '#f700f7', 'magenta3': '#e500e5', 'magenta4': '#bd00bd', 'orchid1': '#ffb7fd', 'orchid2': '#f7b1f4', 'orchid3': '#e5a4e3', 'orchid4': '#bd87bb', 'plum1': '#ffdbff', 'plum2': '#f7d3f7', 'plum3': '#e5c4e5', 'plum4': '#bda1bd', 'MediumOrchid1': '#efa1ff', 'MediumOrchid2': '#e79cf7', 'MediumOrchid3': '#d791e5', 'MediumOrchid4': '#b176bd', 'DarkOrchid1': '#dd7eff', 'DarkOrchid2': '#d57af7', 'DarkOrchid3': '#c671e5', 'DarkOrchid4': '#a35dbd', 'purple1': '#c76fff', 'purple2': '#c16af7', 'purple3': '#b362e5', 'purple4': '#9351bd', 'MediumPurple1': '#d1b6ff', 'MediumPurple2': '#cab0f7', 'MediumPurple3': '#bba3e5', 'MediumPurple4': '#9a87bd', 'thistle1': '#fff0ff', 'thistle2': '#f7e8f7', 'thistle3': '#e5d7e5', 'thistle4': '#bdb1bd', 'gray1': '#1b1b1b', 'gray2': '#232323', 'gray3': '#2d2d2d', 'gray4': '#323232', 'gray5': '#393939', 'gray6': '#3e3e3e', 'gray7': '#444444', 'gray8': '#474747', 'gray9': '#4c4c4c', 'gray10': '#515151', 'gray11': '#545454', 'gray12': '#595959', 'gray13': '#5c5c5c', 'gray14': '#606060', 'gray15': '#626262', 'gray16': '#666666', 'gray17': '#696969', 'gray18': '#6c6c6c', 'gray19': '#6f6f6f', 'gray20': '#727272', 'gray21': '#757575', 'gray22': '#777777', 'gray23': '#7b7b7b', 'gray24': '#7d7d7d', 'gray25': '#808080', 'gray26': '#828282', 'gray27': '#858585', 'gray28': '#878787', 'gray29': '#898989', 'gray30': '#8c8c8c', 'gray31': '#8e8e8e', 'gray32': '#919191', 'gray33': '#929292', 'gray34': '#959595', 'gray35': '#979797', 'gray36': '#999999', 'gray37': '#9b9b9b', 'gray38': '#9d9d9d', 'gray39': '#9f9f9f', 'gray40': '#a1a1a1', 'gray42': '#a5a5a5', 'gray43': '#a8a8a8', 'gray44': '#a9a9a9', 'gray45': '#ababab', 'gray46': '#adadad', 'gray47': '#afafaf', 'gray48': '#b1b1b1', 'gray49': '#b3b3b3', 'gray50': '#b4b4b4', 'gray51': '#b6b6b6', 'gray52': '#b8b8b8', 'gray53': '#bababa', 'gray54': '#bcbcbc', 'gray55': '#bdbdbd', 'gray56': '#bfbfbf', 'gray57': '#c1c1c1', 'gray58': '#c3c3c3', 'gray59': '#c4c4c4', 'gray60': '#c6c6c6', 'gray61': '#c8c8c8', 'gray62': '#c9c9c9', 'gray63': '#cbcbcb', 'gray64': '#cccccc', 'gray65': '#cecece', 'gray66': '#cfcfcf', 'gray67': '#d1d1d1', 'gray68': '#d2d2d2', 'gray69': '#d4d4d4', 'gray70': '#d6d6d6', 'gray71': '#d7d7d7', 'gray72': '#d9d9d9', 'gray73': '#dadada', 'gray74': '#dcdcdc', 'gray75': '#dddddd', 'gray76': '#dfdfdf', 'gray77': '#e0e0e0', 'gray78': '#e2e2e2', 'gray79': '#e3e3e3', 'gray80': '#e4e4e4', 'gray81': '#e6e6e6', 'gray82': '#e7e7e7', 'gray83': '#e9e9e9', 'gray84': '#eaeaea', 'gray85': '#ececec', 'gray86': '#ededed', 'gray87': '#eeeeee', 'gray88': '#efefef', 'gray89': '#f1f1f1', 'gray90': '#f2f2f2', 'gray91': '#f4f4f4', 'gray92': '#f5f5f5', 'gray93': '#f6f6f6', 'gray94': '#f8f8f8', 'gray95': '#f9f9f9', 'gray97': '#fbfbfb', 'gray98': '#fdfdfd', 'gray99': '#fefefe','green':'#00FF00'}
styles={'classic':'1','dark':'2','italic':'3','underline':'4','switchbg':'7','hiddentext':'8'}
def format(text,color='#FFFFFF',bg="#000000",style='classic',category=None,infocategory=None):
  def transform(rgb='#AAA'):
    r,g,b=0,0,0
    if rgb.find('#')!=-1:
     if len(rgb)==4:
        r=(int(rgb[1]+rgb[1],base=16))
        g=(int(rgb[2]+rgb[2],base=16))
        b=(int(rgb[3]+rgb[3],base=16))
    
     elif len(rgb)==7:
       r=int(rgb[1]+rgb[2],base=16)
       g=int(rgb[3]+rgb[4],base=16)
       b=int(rgb[5]+rgb[6],base=16)
    else:
      try:
        rgb=tkcolors[rgb]
        r,g,b=transform(rgb)
      except:
        
        print(format('No such color '+rgb,category='Error'))
    return r,g,b
  def toformat(r,g,b,format='fg',style='classic'):
   if format=='fg':
     try:
        return "\x1b[38;2;" + str(r) + ";" + str(g) + ";" + str(b) +';'+styles[style]+ "m"
     except:
       print(format('No such style '+str(style),category='Error'))
   else:
     return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"
  if infocategory==None:
      infocategory=category
  if category=='Error':
    r1,g1,b1=transform(tkcolors['red'])
    r2,g2,b2=transform('#000')
    ri,gi,bi=transform(tkcolors['orange'])
    style='italic'
    style2='underline'
    if infocategory==None:
      infocategory='Error'
    return toformat(ri,gi,bi,format='fg',style=style)+'['+infocategory+'] '+"\x1b[0m"+' '+toformat(r1,g1,b1,format='fg',style=style2)+toformat(r2,g2,b2,format='bg')+text+"\x1b[0m"
  elif category=='Warning':
    r1,g1,b1=transform(tkcolors['orange'])
    r2,g2,b2=transform('#000')
    ri,gi,bi=transform(tkcolors['yellow'])
    style='italic'
    style2='underline'
    return toformat(ri,gi,bi,format='fg',style=style)+'['+infocategory+'] '+"\x1b[0m"+' '+toformat(r1,g1,b1,format='fg',style=style2)+toformat(r2,g2,b2,format='bg')+text+"\x1b[0m"
  elif category=='Tip':
    r1,g1,b1=transform(tkcolors['light blue'])
    r2,g2,b2=transform('#000')
    ri,gi,bi=transform(tkcolors['blue'])
    style='italic'
    style2='underline'
    return toformat(ri,gi,bi,format='fg',style=style)+'['+infocategory+'] '+"\x1b[0m"+' '+toformat(r1,g1,b1,format='fg',style=style2)+toformat(r2,g2,b2,format='bg')+text+"\x1b[0m"
  elif category=='Info':
    r1,g1,b1=transform(tkcolors['light sea green'])
    r2,g2,b2=transform('#000')
    ri,gi,bi=transform(tkcolors['green'])
    style='italic'
    style2='underline'
    return toformat(ri,gi,bi,format='fg',style=style)+'['+infocategory+'] '+"\x1b[0m"+' '+toformat(r1,g1,b1,format='fg',style=style2)+toformat(r2,g2,b2,format='bg')+text+"\x1b[0m"
  else:
    r1,g1,b1=transform(color)
    r2,g2,b2=transform(bg)
    return toformat(r1,g1,b1,format='fg',style=style)+toformat(r2,g2,b2,format='bg')+text+"\x1b[0m"
def format_line(data,style=('classic',),color=('white',),bg=('black',)): 
  result=''
  info=[]
  for i in data:
    info.append(i)
  
  q1=divide(info,n=len(style))
  info=[]
  for i in q1:
    for j in i:
      info.append(j+'@CyRoIl'+style[q1.index(i)])
  q2=divide(info,n=len(color))
  info=[]
  for i in q2:
    for j in i:
      info.append(j+'@CyRoIl'+color[q2.index(i)])
  q3=divide(info,n=len(bg))
  info=[]
  for i in q3:
    for j in i:
      info.append(j+'@CyRoIl'+bg[q3.index(i)])
  text=''
  for i in info:
    dt=i.split('@CyRoIl')
    text+=format(dt[0],style=dt[1],color=dt[2],bg=dt[3])
  return text
def clear_all():
  if os.name == 'posix':
        os.system('clear')

  elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
def clear_line():
    sys.stdout.write("\033[F") #back to previous line 
    sys.stdout.write("\033[K") #clear line 
class progressbar():
  def __init__(self,percent,color='green',withpercents=True,width=1,wheel=True,startwheelpos=0,types=1):
    self.symbols={10:'█',5:'▍',-1:' ░',-2:'▒',-3:'▓',-4:' '}
    self.wheelpos=[" \ ",' | ',' / ',' — ']
    self.wheelposn=startwheelpos
    self.wheel=wheel
    self.width=width
    self.percent=percent
    self.color=color
    self.type=types
    self.wheelwid=''
    self.withpercents=withpercents
    if wheel==True:
      self.wheelwid=self.wheelpos[self.wheelposn]
    if (percent*width)%10>=5:
      self.text=(int(percent)*width)//10*self.symbols[10]+self.symbols[5]+(100*width-(int(percent)*width))//10*self.symbols[-1*types]
    else:
      self.text=(int(percent)*width)//10*self.symbols[10]+(100*width-(int(percent)*width))//10*self.symbols[-1*types]
    if withpercents==False:
     print(format(self.text+self.wheelwid+' ',color=color))
    else:
      print(format(self.text+self.wheelwid+' ',color=color)+format(str(round(percent,1))+'%',color=color,style='italic'))
  def update(self,percent):
     clear_line()
     if self.wheelposn<3:
      self.wheelposn+=1
     else:
       self.wheelposn=0
     progressbar(percent,color=self.color,withpercents=self.withpercents,width=self.width,wheel=self.wheel,startwheelpos=self.wheelposn,types=self.type)

def similar(arr):
    s = difflib.SequenceMatcher()
    full = []
    for i in arr:
        s.set_seq2(i)
        for n in (arr):
            if n == i:
                continue
            s.set_seq1(n)
            full.append((s.ratio()))
            full.sort(reverse=True)
    return full[0]
def meant(image):
  data=[]
  for i in os.listdir(os.getcwd()):
      data.append(i)
  result=difflib.get_close_matches(image, data)
  return result[0]
def image_opener(image,descend=(1,1)):
  from PIL import Image,ImageOps
  try:
    im = Image.open(image)
    def transform(obj):
   
          return '#%02x%02x%02x' % obj
    rgb_im = im.convert('RGB')
    rgb_im= rgb_im.resize((rgb_im.size[0]//descend[0],rgb_im.size[1]//descend[1]),Image.NEAREST)
    for i in range(1,rgb_im.size[1]):
      for j in range(1,rgb_im.size[0],1):
      
        print(format('.',bg=transform(rgb_im.getpixel((j, i))),color=transform(rgb_im.getpixel((j, i)))),end='')
      print('')
  except:
    print(format("Can't open the image "+image+'. Did you meant '+meant(image)+' ?',category='Error'))
    image_opener(meant(image),descend=descend)
def screen_size():  
  import curses #number of rows and columns

  screen = curses.initscr()
  rows, cols = screen.getmaxyx()
  curses.endwin()
  return rows,cols
def bind(button,function=None,nooutput=True):
  global bindings
  def curser(button,function,nooutput):
    stdscr = initscr()
    if nooutput==True:
      noecho() 
    else:
      pass
    while True:
      c = stdscr.getch()
      if c == ord(button):
         if function!=None:
           function()
  process=Thread(target=curser,args=(button,function,nooutput))
  process.start()
  bindings[button]=(function,process,nooutput) 