import urwid
import asyncio
class SongProgressBar(urwid.ProgressBar):
    def __init__(self, normal, complete, current=0, done=100, satt=None):
        super().__init__(normal, complete, current, done, satt)
        self.song = "" 
        self.val=0
    
    def get_text(self):
        return self.song
    
    def set_text(self, text):
        self.song = text
        
    def set_prog(self,value):
        self.val=value
        
    def update_progress_bar(self,a=None,b=None):
         
        self.set_text(self.song )
        self.set_completion(self.val) 

 