import asyncio
import urwid


palette = [
    ('pg_normal', 'white', 'black'),
    ('pg_complete', 'black', 'white'),
  
    ('selected', 'black', 'white'),
]




def KeyboardEvents():
    pass 




filler = urwid.Filler(urwid.Text("Hola mundo"), 'top')


frame=urwid.Frame(body=filler)





evl=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl, unhandled_input=KeyboardEvents)

loop.run()