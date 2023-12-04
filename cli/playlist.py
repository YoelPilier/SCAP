import urwid
from cli.ClickableText import ClickableText



class PlayListWidget(urwid.ListBox):
    def __init__(self,  ):
      
        self.listwalker = urwid.SimpleFocusListWalker([])
        self.filterlist=[]
        self.actualfilteritem=0
        super().__init__(self.listwalker)

    def Set_Callbacks(self, focus_callback=None, play_callback=None):
        self.focus_callback = focus_callback
        self.play_callback = play_callback
        
    def UpdateList(self, items):
        self.listwalker.clear()
        for item in items:
            self.listwalker.append(urwid.AttrMap(ClickableText(item[0], focus_callback=self.UpdateFocus, play_callback=self.play_callback, CallbackArgs=item[1], ),None,focus_map='selected') )
    
    def UpdateFocus(self, button,index):
        self.set_focus(index)
        if self.focus_callback:
            self.focus_callback(button,index)
        self.set_focus_valign('middle')
               
    def Play(self, button,index):
        if self.play_callback:
            self.play_callback(button,index)
            self.UpdateFocus(button,index)
    
    def SetFilter(self, filter):
        self.filterlist=filter
        self.actualfilteritem=0
        if self.filterlist:  # Comprobar si la lista no está vacía
            self.UpdateFocus(None,self.filterlist[self.actualfilteritem])
       
        
    
    def ResetFilter(self):
        self.filterlist=[]
        self.actualfilteritem=0       
    
    def keypress(self, size, key):
        if len(self.listwalker) == 0:
            return super().keypress(size, key)
        if key == 'down':
            try:
                if len(self.filterlist)>0:
                    if self.actualfilteritem==len(self.filterlist)-1:
                        pass
                    else:
                        self.actualfilteritem+=1
                    
                    self.UpdateFocus(None,index=self.filterlist[self.actualfilteritem])
                else:
                    self.UpdateFocus(None,index=self.focus_position + 1)
            except IndexError:
                pass  # ya en el último elemento
        elif key == 'up':
            if self.focus_position > 0:
                if len(self.filterlist)>0:
                    if self.actualfilteritem==0:
                        pass
                    else:
                        self.actualfilteritem-=1
                    self.UpdateFocus(None,index=self.filterlist[self.actualfilteritem])
                else:
                    self.UpdateFocus(None,index=self.focus_position - 1)
                
        elif key == 'enter':
            self.Play(None,index=self.focus_position)  
                 
                
        else:
            return super().keypress(size, key)
     
    def mouse_event(self, size, event, button, col, row, focus):
        if button == 4:
            self.keypress(size, 'up')
        elif button == 5:
            self.keypress(size, 'down')
         
        else:
            return super().mouse_event(size, event, button, col, row, focus)