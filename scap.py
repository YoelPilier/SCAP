"""
 
"""
from Player import MusicPlayer
import PlayList as pl
import time

player = MusicPlayer()

playlist = pl.PlayList(player.valid_ext)


playlist.add("testmusic")

playlist.shuffle = True

while True:
    song = playlist.Next()
    if song == None:
        break
    song, data = song
    player.load_file(song)
    player.play()
    print(data)
    while player.isPlaying():
        pass
        time.sleep(1)
print("Fin de la lista de reproduccion")