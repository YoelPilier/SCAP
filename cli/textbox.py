import urwid

class TextBox(urwid.Edit):
    def __init__(self, caption, callback):
        super().__init__(caption)
        self.callback = callback
    def keypress(self, size, key):
        if key == 'enter':
            self.callback(self.get_edit_text())
            self.set_edit_text('')
        else:
            return super().keypress(size, key)