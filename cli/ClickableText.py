import time
import urwid    

class ClickableText(urwid.Text):
    def __init__(self, markup, focus_callback=None, play_callback=None,CallbackArgs=None,wrap="clip"):
        super().__init__(markup,wrap=wrap)
        self.focus_callback = focus_callback
        self.play_callback = play_callback
        self.CallbackArgs = CallbackArgs
        self.last_click = 0

    def mouse_event(self, size, event, button, col, row, focus):
        if event == 'mouse press':
            if button == 1:
                current_time = time.time()
                if current_time - self.last_click < 0.5:  # 0.5 segundos de umbral
                    if self.play_callback:
                        self.play_callback(self,self.CallbackArgs)
                else:
                    if self.focus_callback:
                        self.focus_callback(self,self.CallbackArgs)
                self.last_click = current_time