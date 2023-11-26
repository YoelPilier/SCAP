"""


player = MusicPlayer()
player.load_file('test.m4a')
player.play()  # Reproducir la música
player.set_volume(0.1)  # Establecer volumen a 50%
player.get_song_info()  # Obtener información de la canción
input('Presiona enter para detener la música')
player.stop()  # Detener la música

input('Presiona enter para reproducir la música')

player.play()  # Reproducir la música
 
input('Presiona enter para pausar la música')

player.load_file('test.flac')

player.play()  # Reproducir la música

player.get_song_info()  # Obtener información de la canción    
input('Presiona enter para detener la música') 
player.load_file('test.mp3')
print(player.track_playback_time())
input('Presiona enter para reproducir la música')
player.play()  # Reproducir la música
player.get_song_info()  # Obtener información de la canción
input('Presiona enter para detener la música')
player.track_playback_time()  # Obtener el tiempo de reproducción

"""
from Player import MusicPlayer
import PlayList as pl
import time

player = MusicPlayer()

playlist = pl.PlayList(player.valid_ext)


playlist.add("/home/yoel/externo/Musica/")

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