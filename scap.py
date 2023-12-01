import asyncio
import urwid


palette = [ 
    ('altered', 'black', 'light red'),   
    ('normal', 'light red', 'black'),
    ('pg_normal', 'light red', 'black'),
    ('pg_complete', 'black', 'light red'),
  
    ('selected', 'black', 'light red'),
]

 

 
 


frame=urwid.AttrMap( urwid.Frame(body=filler) , 'normal')






evl=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl )

loop.run()