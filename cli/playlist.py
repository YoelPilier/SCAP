import urwid
import cli.ClickableText as ClickableText



class PlayListWidget():
    def __init__(self,focus_callback=None,play_callback=None ):
        self.focus_callback = focus_callback
        self.Play_callback = play_callback
        self.listwalker = urwid.SimpleFocusListWalker([])
        self.listbox = urwid.ListBox(self.listwalker)
        
    def UpdateList(self, items):
        self.listwalker.clear()
        for item in items:
            self.listwalker.append(ClickableText.ClickableText(item[0], focus_callback=self.focus_callback, play_callback=self.Play_callback,CallbackArgs=item[1]))

    def SetFocus(self, index):
        self.focus_callback(self.listwalker[index],self.listwalker[index].CallbackArgs)
        self.listwalker.set_focus(index)
        