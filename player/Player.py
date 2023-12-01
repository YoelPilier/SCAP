import os
import pygame
import io
from pydub import AudioSegment
from player.States import PlayerState


class MusicPlayer:
    def __init__(self):
        # Inicializar mixer con canales estéreo
        pygame.mixer.init(channels=2)
        self.audio_file = None
        self.prev_audio_file = None
        self.state = PlayerState.DETENIDO 
        self.ext = None     
        self.valid_ext = ['.ogg', '.wav', '.mp3', '.flac', '.m4a']
        self.fadeout=0
        
    def setFadeout(self, time):
        self.fadeout = time   
        
    def load_file(self, file_path):
        # Obtener la extensión del archivo
        _,  ext = os.path.splitext(file_path)
        if ext.lower()  in self.valid_ext:
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
    
    def isPlaying(self):
        return pygame.mixer.music.get_busy()
    
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
                    if self.fadeout > 0:
                        pygame.mixer.music.fadeout(self.fadeout)
                    else:
                        pygame.mixer.music.stop()
                    self.state = PlayerState.DETENIDO
                    self.prev_audio_file = self.audio_file
                    self.play()
       
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
    
    def pause(self):
        if self.state == PlayerState.REPRODUCIENDO:
            pygame.mixer.music.pause()
            self.state = PlayerState.EN_PAUSA
            return
     
   
    def stop(self):
        if self.state == PlayerState.REPRODUCIENDO:
            pygame.mixer.music.stop()
            self.state = PlayerState.DETENIDO
            return
        
        
    def set_volume(self, volume):
        volume = max(0, min(volume, 1))
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()
  
      
    def track_playback_time(self):
       return pygame.mixer.music.get_pos() / 1000
    
    def jump_to(self, time):
        pygame.mixer.music.set_pos(time)
         
         

 
 