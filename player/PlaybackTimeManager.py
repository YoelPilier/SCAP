import time


class PlaybackTimeManager:
    def __init__(self):
        self.__start_time = None
        self.__pause_time = 0
        self.jump_time = 0
        self.__paused = False
        self.max_time = 0
        
    def start(self ):
        self.jump_time = 0 
        self.__start_time = time.time()-self.__pause_time-self.jump_time
        self.__paused = False
        
    def pause(self):
        self.__pause_time = time.time() - self.__start_time
        self.__paused = True
        
    def resume(self):
        self.__start_time = time.time()-self.__pause_time
        self.__paused = False
        
    def stop(self):
        self.__start_time = None
        self.__pause_time = 0
        self.jump_time = 0
        self.__paused = False
        
    def get_time(self):
        if self.__start_time:
            if self.__paused:
                return self.__pause_time
            else:
                return time.time() - self.__start_time
        else:
            return 0
        
    def set_time(self, new_time):
        self.jump_time = new_time
        val = abs(time.time() - self.__pause_time - self.jump_time)
        
        self.__start_time = val 