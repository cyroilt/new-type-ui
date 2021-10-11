
!['PYUIJSON'](icon.png 'PYUIJSON')
# version 0.1 # 
- ##  added `app` module ##
- ## added ` main ` module ##
# version 0.2 #
- ## added `bind` function to `app` module
- ## added `button` module
# version 0.3
- ## added `autoresize` parameter to `button`
# version 0.4
- ## added gradient and gif support
- ## added `canvas` module   
- ## bug fixes
## * modules functions * 
- ## app(*windowsize*='100x100',*title*='pyuijson',*icon*='ICO_OR_PNG_IMAGE',*transparency*=1,*fullscreen*=False,*istool*=False,*topmost*=False,*bg*='"COLOR" OR "IMAGE"',*bginfo*="white",*looped*=True)
 #### v.0.1 
creates a window with parameters parameters 
- - `windowsize='XxY'` - set size of window (height=y,width=x) 
- - `title = 'title'` - set a window title 
- - `icon='icon.(png or ico or jpg)'` #### after v0.4 it can be animated ico
- - `transparency = 1` - set window transparency from 0.1 to 1.0 #### after v.0.4 from 1 to 100 
- - `fullscreen=False` - set window mode to fullscreen
- - `istool=False` - set window mode to tool window
- - `topmost=False` - set window mode to forward window
- - `bg="color" or bg = "image" or bg="gradient"` - set window's bg mode
- - `bginfo ="your_color" or bginfo ="your_image" or bginfo=('your color 1','your color 2') ` - set window's bg
- - `looped=True` -run window loop #### v0.4 
***
- - ## app.loop() - start a window loop #### from v0.1. after v0.4 doesn't required 
***
- - ## app.configure(param) - update window's parameters (watch `app`) 
***
- - ## app.bind(rule,todo,args=(),kwargs={},withoutput=True) - binds app events
## here is comparing app bindings with tk bindings
- `'M-Left'`:`'<Button-1>'`,
- `'M-Right'`:`'<Button-3>'`,
- `'M-Middle':'<Button-2>'`,
- `'M-Wheel'`:`'<MouseWheel>'`,
- `'MM-Left'`:`'<Double-Button-1>'`,
- `'MM-Middle'`:`'<Double-Button-2>'`,
- `'MM-Right'`:`'<Double-Button-3>'`,
- `'M-Motion'`:`'<Motion>'`,
- `'M-Left-Motion'`:`'<B1-Motion>'`,
- `'M-Middle-Motion'`:`'<B2-Motion>'`,
- `'M-Right-Motion'`:`'<B3-Motion>'`,
- `'Enter'`:`'<Return>'`,
- `'In'`:`'<Enter>'`,
- `'Out'`:`'<Leave>'`
- other buttons you can bind as like tk but without '<' and '>'
- ### params: `rule` watch higher , `todo` - any function
====
example: 

<br> `a= app()` <br /> 
<br> `a.bind('M-Left',print,args=('hi','sleep'),kwargs='sep')` <br />
<br> `a.loop() #after click on window prints 'event hi sleep'` <br /> 
*** 
- - ## app.kill()-destroys an app window
***
- ## button(app,size='50x25',place=None,text='',image=None,function=None,withoutput=False,animation=None,switcher=None,autoresize=False,onreleasef=None,onreleasout=False,bg='#004DFF') - creates a button on `app` window
- - at that moment released 'lighter' animation
- - ### refunc(function) 



