import os
import pygame
import io
from pydub import AudioSegment

from enum import Enum

class PlayerState(Enum):
    REPRODUCIENDO = 1
    EN_PAUSA = 2
    DETENIDO = 3

Formatos_Permitidos = ['.ogg', '.wav', '.mp3', '.flac', '.m4a']


class MusicPlayer:
    def __init__(self):
        # Inicializar mixer con canales estéreo
        pygame.mixer.init(channels=2)
        self.audio_file = None
        self.prev_audio_file = None
        self.state = PlayerState.DETENIDO 
        self.ext = None     

    def load_file(self, file_path):
        # Obtener la extensión del archivo
        _,  ext = os.path.splitext(file_path)
        if ext.lower()  in Formatos_Permitidos:
            self.ext = ext
            if self.audio_file == None:
                self.audio_file = file_path
                self.prev_audio_file = file_path
                return
            else: 
                self.audio_file = file_path
                return
            
        else:
            print(f'Unsupported file format: {ext}')
            return

    def get_state(self):
        return self.state
    
    def __LoadM4A(self, file_path):
        audio = AudioSegment.from_file(file_path, "m4a")
        byteIO = io.BytesIO()
        audio.export(byteIO, format="wav")
        byteIO.seek(0)
        return byteIO
    
    
    def play(self):     
        match self.state:
            case PlayerState.REPRODUCIENDO:
                if self.audio_file != self.prev_audio_file:
                    self.stop()
                    self.state = PlayerState.DETENIDO
                    self.prev_audio_file = self.audio_file
                    self.play()
                else:
                    pygame.mixer.music.pause()
                    self.state = PlayerState.EN_PAUSA
                 
            case PlayerState.EN_PAUSA:
                pygame.mixer.music.unpause()
                self.state = PlayerState.REPRODUCIENDO
                
            case PlayerState.DETENIDO:
                
                if self.ext == '.m4a':
                    byteIO = self.__LoadM4A(self.audio_file)
                    pygame.mixer.music.load(byteIO)
                else:
                    pygame.mixer.music.load(self.audio_file)
                pygame.mixer.music.play()
                self.state = PlayerState.REPRODUCIENDO
        return
     
   
    def stop(self):
        if self.state == PlayerState.REPRODUCIENDO:
            pygame.mixer.music.stop()
            self.state = PlayerState.DETENIDO
            return
        
        
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()
 
 
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
