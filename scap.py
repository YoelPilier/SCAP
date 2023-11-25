from Player import MusicPlayer

player = MusicPlayer()
player.load_file('test.m4a')
player.play()  # Reproducir la música
player.set_volume(0.1)  # Establecer volumen a 50%

input('Presiona enter para detener la música')
player.stop()  # Detener la música

input('Presiona enter para reproducir la música')

player.play()  # Reproducir la música
 
    
input('Presiona enter para pausar la música')

player.load_file('test.flac')

player.play()  # Reproducir la música

input('Presiona enter para detener la música')

 