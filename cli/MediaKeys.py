from pynput import keyboard 
import threading

class MediaKeysController:
    def __init__(self, playcallback, nextcallback, previouscallback):
        self.playcallback = playcallback
        self.nextcallback = nextcallback
        self.previouscallback = previouscallback

    def on_press(self, key):
        if key == keyboard.Key.media_play_pause:
            threading.Thread(target=self.playcallback).start()
        elif key == keyboard.Key.media_next:
            threading.Thread(target=self.nextcallback).start()
        elif key == keyboard.Key.media_previous:
            threading.Thread(target=self.previouscallback).start()

    def start_listening(self):
        listener = keyboard.Listener(on_press=self.on_press)
        thread = threading.Thread(target=listener.start)
        thread.start()