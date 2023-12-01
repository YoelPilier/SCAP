import urwid


class Buttons(urwid.GridFlow):
    def __init__(self, play=None , stop=None, next=None, prev=None ):
        buttons = [
            urwid.Button("play",on_press=play),
            urwid.Button("stop",on_press=stop),
            urwid.Button("next",on_press=next),
            urwid.Button("prev",on_press=prev) 
        ]
         
        super().__init__(buttons, 8, 2, 0, 'center')
 