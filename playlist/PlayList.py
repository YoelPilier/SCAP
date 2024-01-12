﻿import os
import random
import time
import playlist.Metadata as Metadata
from playlist.Util import To_Minutes
from concurrent.futures import ThreadPoolExecutor

class PlayList:
    def __init__(self, valid_ext):
        self.valid_ext = valid_ext
        random.seed(time.time()) 
        self.files = []
        self.metadata = []  
        self.queue = [] 
        self.playlist = []
        self.current = -1 
        self.shuffle = True
        self.focused = -1
        self.first = True    
        # Obtener el directorio home del usuario actual
        home_dir = os.path.expanduser("~")

        # Cambiar el directorio de trabajo actual al directorio home
        os.chdir(home_dir)
    def __len__(self):
        return len(self.files)
    
    def add(self, file_path):
        
        if os.path.isfile(file_path):
            self.__addsingle(file_path)
        elif os.path.isdir(file_path):
            routes=self.__getRoutes(file_path)
            with ThreadPoolExecutor() as executor:
                executor.map(self.__addsingle, routes) 
    
    def __getRoutes(self, file_path):
         
        routes=[]
        for dirpath, _, filenames in os.walk(file_path):
            for filename in filenames:
                routes.append(os.path.join(dirpath, filename))
        return routes
    
    def __addsingle(self, file_path):
        _, ext = os.path.splitext(file_path)
        if ext.lower() in self.valid_ext:
            meta=Metadata.get_song_info(file_path, ext)
            self.files.append(file_path)             
            meta[Metadata.INDEX]=len(self.files)-1                         
            self.metadata.append(meta)
            self.playlist.append((f"{meta[Metadata.INDEX]+1} - {meta[Metadata.TITLE]} - {meta[Metadata.ARTIST]} - {meta[Metadata.ALBUM]} - {To_Minutes(meta[Metadata.DURATION])}",meta[Metadata.INDEX]))
                                               
    def remove(self, index):
        if index < len(self.files):
            self.files.pop(index)
            
    def clear(self):
        self.files.clear()
        self.playlist.clear()
        
 
        
    def Next(self):
        if  self.shuffle:
            self.current=random.choice(range(len(self.files)))
            file=self.files[self.current]
            data=self.metadata[self.current]
            self.queue.append(self.current)
            return file, data
        
        if self.current < len(self.files):
            self.current += 1
            self.focused = self.current
            file=self.files[self.current]
            data=self.metadata[self.current]
            self.queue.append(self.current)
            return file, data 
        else:
            return None
        
    def Prev(self):
        if len(self.queue)>1:
            index=self.queue.index(self.current)
            if index==0:
                return None
            self.current=self.queue[index-1]
            self.focused = self.current
            self.queue.append(self.current)
            return self.files[self.current], self.metadata[self.current]
        
        else:
            return None         
        
    def Jump(self, index):
        if index < len(self.files):
            if self.first:
                if self.shuffle:
                    self.current=random.choice(range(len(self.files)))
                else:
                                    
                    self.current=index if index >=0 else 0
                self.first=False
            else:
                self.current=index
            self.focused = self.current
            self.queue.append(self.current)
            return self.files[self.current], self.metadata[self.current]
        else:
            return None
        
    def Move_up(self):
        if self.focused > 0:
            self.focused -= 1
        return self.focused
        
    def Move_down(self):
        if self.focused < len(self.files):
            self.focused += 1
        return self.focused
        
    def Get_focused(self):
        return  self.files[self.focused], self.metadata[self.focused]
    
    def Set_focused(self, index):
        self.focused = index
    
    def Get_current(self):
        return self.files[self.current], self.metadata[self.current]
    
    def search(self, text):
        result=[] 
        for i in range(len(self.files)):
            if text.lower() in self.files[i].lower() or text.lower() in self.playlist[i][0].lower():
                result.append(i) 
        return result  
        
    def Get_Playlist(self ):
        return self.playlist
 
        
