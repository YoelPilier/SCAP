import urwid

class Body(urwid.Frame):
    def __init__(self, header, body, footer):
        super().__init__(header=header,  body=body, footer=footer)
        self.set_focus('body')
        
    
    
    def keypress(self, size, key):
        if key == 'tab':
            
       
            if self.focus_part == 'body':
                self.set_focus('footer')
            elif self.focus_part == 'footer':
                self.set_focus('body')
        else:
            return super().keypress(size, key)

 

 