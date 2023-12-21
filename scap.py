import asyncio
import urwid
from cli.playlist import PlayListWidget
from cli.cliSets import palette
from cli.Header import Header
from cli.Buttons import Buttons
from cli.Body import Body
from cli.MediaKeys import MediaKeysController
from cli.SongProgress import SongProgressBar
from cli.textbox import TextBox
from playlist.PlayList import PlayList
from playlist import Metadata
from player.Player import MusicPlayer
from player.States import PlayerState

 
musicplayer = MusicPlayer()
pl=PlayList(musicplayer.valid_ext)

header=Header("SCAP")
progres=SongProgressBar('pg_normal', 'pg_complete', 0, 100, 'pg_smooth',musicplayer.jump_to )


def set_taskbar_title(song_name):
    print(f'\033]0;{song_name}\007', end='', flush=True)


plw=PlayListWidget()

 
def Play(idx):
    try:
        song, data = pl.Jump(idx)
        if  pl.current != -1:
            plw.set_focus(pl.current)
            plw.set_focus_valign('middle')  
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}", data[Metadata.DURATION])
        musicplayer.load_file(song, data[Metadata.DURATION])
        header.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        set_taskbar_title(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        musicplayer.play()
    
        loop.set_alarm_in(3, clear )  
    except Exception as e:
        pass

def Pause():
    try:
        musicplayer.pause()
    except Exception as e:
        pass


def Play_Focused(Button=None):
    try:
        state=musicplayer.get_state()
        if state== PlayerState.DETENIDO:
            Play(pl.focused)
            if  pl.current != -1:
                plw.set_focus(pl.current)
                plw.set_focus_valign('middle') 
        elif state == PlayerState.EN_PAUSA:
            musicplayer.play()
        if state == PlayerState.REPRODUCIENDO:
            musicplayer.pause()
        loop.set_alarm_in(3, clear )  
    except Exception as e:
        clear()
    
        

def Next(Button=None):
    try:
        song, data = pl.Next()
        if  pl.current != -1:
            plw.set_focus(pl.current)
            plw.set_focus_valign('middle')  
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}", data[Metadata.DURATION])
        musicplayer.load_file(song, data[Metadata.DURATION])
        header.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        set_taskbar_title(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        musicplayer.play()
        loop.set_alarm_in(3, clear )  
    except Exception as e:
        clear()

def Prev(Button=None):
    try:
        song, data = pl.Prev()
        if  pl.current != -1:
            plw.set_focus(pl.current)
            plw.set_focus_valign('middle') 
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}", data[Metadata.DURATION])
        musicplayer.load_file(song, data[Metadata.DURATION])
        header.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        set_taskbar_title(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]}")
        musicplayer.play()
        loop.set_alarm_in(3, clear )  
    except Exception as e:
        clear()
    

    
def Stop(Button=None):
    try: 
        musicplayer.stop()
    except Exception as e:
        pass
    
def Add(ruta):
    try:
        pl.add(ruta)
        plw.UpdateList(pl.Get_Playlist())
    except Exception as e:
        pass
 


def play_onclick_callback( Button=None, idx=-1):
    try:
        if pl.current != idx:
            Play(idx)
    except Exception as e:
        pass
    
    
def focus_callback(Button=None, idx=-1):
    try:
        pl.Set_focused(idx)
    except Exception as e:
        pass
    

 

def playing(loop=None, user_data=None):
    if musicplayer.get_state() == PlayerState.REPRODUCIENDO:
        if not  musicplayer.isPlaying():
            Next()
            progres.set_prog(0)
    
    
    loop.set_alarm_in(1, playing )  
    

def Updatebar(loop=None, user_data=None):
    progres.set_prog(musicplayer.get_Progress())
    progres.set_time(musicplayer.track_playback_time())
    progres.update_progress_bar()
    loop.set_alarm_in(1, Updatebar )         
  

MediaKeysController(Play_Focused, Next, Prev ).start_listening()



plw.Set_Callbacks(focus_callback=focus_callback, play_callback=play_onclick_callback)


def clear(l=None, u=None ):
    loop.screen.clear() 



def Handle_Command(text):
    if text.startswith('>'):
        text=text[1:].strip() 
         
        
        Add(text)
    elif text.startswith('#'):
        text=text[1:].strip()
        if len(text)==0:
             
        
            plw.ResetFilter()
            if pl.focused >-1:
                plw.set_focus(pl.focused)
                plw.set_focus_valign('middle')
            return "D:"
            
        else:
            if text.startswith('#'):
                text=text[1:].strip()
            filter=pl.search(text)
            plw.SetFilter(filter)
            return "D:#"
    elif text == 'exit':
        raise urwid.ExitMainLoop()
    elif text == 'play':
        Play_Focused()
    elif text == 'pause':
        Pause()
    elif text == 'stop':
        Stop()
    elif text == 'next':
        Next()
    elif text == 'prev':
        Prev()
    elif text == 'random':
        pl.shuffle = not pl.shuffle
    return None        
        
 
command_prompt = TextBox("D:", Handle_Command)
 
 
 


botones=Buttons(play=Play_Focused, stop=Stop, next=Next, prev=Prev  ) 
footer_stack = urwid.Pile([urwid.Divider("*"),progres, urwid.Divider("*"),   botones,urwid.Divider("*"),command_prompt,urwid.Divider("*")])
#footer_stack = urwid.Pile([urwid.Divider("*"),progres, urwid.Divider("*"),    command_prompt,urwid.Divider("*")])

frame=urwid.AttrMap( Body(header=header,body=plw,footer=footer_stack) , 'normal')

loop = asyncio.get_event_loop()
 
 
 
 

evl=urwid.AsyncioEventLoop(loop=loop)

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl )




loop.set_alarm_in(1, playing ) 
loop.set_alarm_in(1, Updatebar )


 


loop.run()
