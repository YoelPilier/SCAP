import urwid
from cli.ClickableText import ClickableText



class PlayListWidget(urwid.ListBox):
    def __init__(self, focus_callback=None, play_callback=None):
        self.focus_callback = focus_callback
        self.play_callback = play_callback
        self.listwalker = urwid.SimpleFocusListWalker([])
        super().__init__(self.listwalker)

    def UpdateList(self, items):
        self.listwalker.clear()
        for item in items:
            self.listwalker.append(urwid.AttrMap(ClickableText(item[0], focus_callback=self.UpdateFocus, play_callback=self.play_callback, CallbackArgs=item[1]),None,focus_map='selected') )
    
    def UpdateFocus(self, button,index):
        self.set_focus(index)
        self.focus_callback(button,index)
               
    def Play(self, button,index):
        if self.focus_position != index:
            self.play_callback(button,index)
            self.UpdateFocus(button,index)
      
    
    def keypress(self, size, key):
        if key == 'down':
            try:
                self.UpdateFocus(None,index=self.focus_position + 1)
            except IndexError:
                pass  # ya en el último elemento
        elif key == 'up':
            if self.focus_position > 0:
                self.UpdateFocus(None,index=self.focus_position - 1)
        else:
            return super().keypress(size, key)
     
    def mouse_event(self, size, event, button, col, row, focus):
        if button == 4:
            self.keypress(size, 'up')
        elif button == 5:
            self.keypress(size, 'down')
         
        else:
            return super().mouse_event(size, event, button, col, row, focus)