import urwid
from playlist import Util

class SongProgressBar(urwid.ProgressBar):
    def __init__(self, normal, complete, current=0, done=100, satt=None,jumpcallback=None  ):
        super().__init__(normal, complete, current, done, satt)
        self.song = "" 
        self.duration=""
        self.val=0
        self.jumpcallback=jumpcallback
        self.time="0" 
    def set_time(self, seconds):
        self.time=Util.To_Minutes(seconds) 
    
    def get_text(self):
        return self.song+" "+self.time+"/"+Util.To_Minutes(self.duration)
    
    def set_text(self, text,duracion):
        self.song = text
        self.duration=duracion
        
    def set_prog(self,value):
        self.val=value
        
    def update_progress_bar(self,a=None,b=None):
         
        self.set_text(self.song,self.duration)
        self.set_completion(self.val) 

    def mouse_event(self, size, event, button, col, row, focus):
        if event == 'mouse press':
            if button == 1:
                relative_position = col / size[0]
                song_progress_point = relative_position * self.done
                if self.jumpcallback:
                    self.jumpcallback(relative_position)
                self.set_prog(song_progress_point)
                self.update_progress_bar()
                return True
 