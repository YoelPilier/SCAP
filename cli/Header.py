import urwid


class Header(urwid.Pile):
    def __init__(self, text="SCAP"):
        self.basetext = text
        self.text_widget = urwid.Text(text, align="center")
        super().__init__([
            self.text_widget,
            urwid.Divider("*")
        ])

    def set_text(self, text):
        self.text_widget.set_text(self.basetext+"|"+text)
    