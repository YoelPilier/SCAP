import urwid


class Header(urwid.Pile):
    def __init__(self,text="SCAP"):
        super().__init__([
            urwid.Text(text, align="center"),
            urwid.Divider("*")
        ])