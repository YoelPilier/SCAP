﻿import asyncio
import urwid
from cli.playlist import PlayListWidget
from cli.cliSets import palette
from cli.Header import Header
from cli.Buttons import Buttons
from cli.Body import Body
from cli.MediaKeys import MediaKeysController
from cli.SongProgress import SongProgressBar
from playlist.PlayList import PlayList
from playlist import Metadata
from player.Player import MusicPlayer
from player.States import PlayerState

 
musicplayer = MusicPlayer()
pl=PlayList(musicplayer.valid_ext)
progres=SongProgressBar('pg_normal', 'pg_complete', 0, 100 )
 
pl.add("testmusic")



 
def Play(idx):
    try:
        song, data = pl.Jump(idx)
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]} - {data[Metadata.ALBUM]}")
        musicplayer.load_file(song, data[Metadata.DURATION])
        musicplayer.play()
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
        elif state == PlayerState.EN_PAUSA:
            musicplayer.play()
        if state == PlayerState.REPRODUCIENDO:
            musicplayer.pause()
        
    except Exception as e:
        pass
    
        

def Next(Button=None):
    try:
        song, data = pl.Next()
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]} - {data[Metadata.ALBUM]}")
        musicplayer.load_file(song, data[Metadata.DURATION])
        musicplayer.play()
    except Exception as e:
        pass

def Prev(Button=None):
    try:
        song, data = pl.Prev()
        progres.set_text(f"{data[Metadata.TITLE]} - {data[Metadata.ARTIST]} - {data[Metadata.ALBUM]}")
        musicplayer.load_file(song, data[Metadata.DURATION])
        musicplayer.play()
    except Exception as e:
        pass
    
 
    
def Stop(Button=None):
    try: 
        musicplayer.stop()
    except Exception as e:
        pass
    
def Add(ruta):
    try:
        pl.add(ruta)
    except Exception as e:
        pass



def play_onclick_callback( Button=None, idx=-1):
    try:
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
    progres.update_progress_bar()
    loop.set_alarm_in(1, Updatebar )         
  

MediaKeysController(Play_Focused, Next, Prev).start_listening()


plw=PlayListWidget(play_callback=play_onclick_callback, focus_callback=focus_callback)


plw.UpdateList(pl.Get_Playlist())

botones=Buttons(play=Play_Focused, stop=Stop, next=Next, prev=Prev  ) 
footer_stack = urwid.Pile([urwid.Divider("*"), botones, urwid.Divider("*"), progres, urwid.Divider("*")])

frame=urwid.AttrMap( Body(header=Header(),body=plw,footer=footer_stack) , 'normal')

loop = asyncio.get_event_loop()
 

evl=urwid.AsyncioEventLoop(loop=loop)

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl )
loop.set_alarm_in(1, playing ) 
loop.set_alarm_in(1, Updatebar )
 

loop.run()
