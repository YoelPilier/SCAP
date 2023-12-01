import asyncio
import urwid
from cli.playlist import PlayListWidget
from cli.cliSets import palette
from cli.Header import Header
from playlist.PlayList import PlayList
from player.Player import MusicPlayer


musicplayer = MusicPlayer()

pl=PlayList(musicplayer.valid_ext)
pl.add("testmusic")

def Play(idx):
    song,data= pl.Jump(idx)
    musicplayer.load_file(song)
    musicplayer.play()

def Pause():
    musicplayer.pause()


def Play_Focused():
    song,data= pl.Get_focused()
    musicplayer.load_file(song)
    musicplayer.play()

def Next():
    song,data= pl.Next()
    musicplayer.load_file(song)
    musicplayer.play()

def Prev():
    song,data= pl.Prev()
    musicplayer.load_file(song)
    musicplayer.play()
    
def Shuffle():
    pl.shuffle = not pl.shuffle
    
def Clear():
    pl.clear()
    musicplayer.stop()
    
def Add(ruta):
    pl.add(ruta)


 

def play_onclick_callback(button, idx):
    Play(idx)
    
    
def focus_callback(button, idx):
    pl.Set_focused(idx)
    pass





plw=PlayListWidget(play_callback=play_onclick_callback, focus_callback=focus_callback)


plw.UpdateList(pl.Get_Playlist())


header=urwid.AttrMap(Header("SCAP"), 'normal')
frame=urwid.AttrMap( urwid.Frame(header=header,body=plw) , 'normal')






evl=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl )

loop.run()
