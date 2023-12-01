import asyncio
import urwid
from cli.playlist import PlayListWidget
from playlist.PlayList import PlayList
from player.Player import MusicPlayer
from cli.cliSets import palette

musicplayer = MusicPlayer()


pl=PlayList(musicplayer.valid_ext)
pl.add("testmusic")

 

def play_callback(button, idx):
    song,data= pl.Jump(idx)
    musicplayer.load_file(song)
    musicplayer.play()
    
    
def focus_callback(button, data):
    pl
    pass





plw=PlayListWidget(play_callback=play_callback, focus_callback=focus_callback)


plw.UpdateList(pl.Get_Playlist())

 

frame=urwid.AttrMap( urwid.Frame(body=plw) , 'normal')






evl=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop())

loop=urwid.MainLoop(frame, palette=palette, event_loop=evl )

loop.run()
