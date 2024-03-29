import urwid


class Buttons(urwid.GridFlow):
    def __init__(self, play=None , stop=None, next=None, prev=None,on_check_change=None ):
        buttons = [
            urwid.Button("stop",on_press=stop),
            urwid.Button("prev",on_press=prev), 
            urwid.Button("play",on_press=play),            
            urwid.Button("next",on_press=next),
            urwid.CheckBox("rnd", state=True, on_state_change=on_check_change),
        ]
         
        super().__init__(buttons, 8, 2, 0, 'center')
 