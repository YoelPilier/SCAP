"""
from Player import MusicPlayer
import PlayList as pl
import time

player = MusicPlayer()

playlist = pl.PlayList(player.valid_ext)


playlist.add("testmusic")

playlist.shuffle = True

while True:
    song = playlist.Next()
    if song == None:
        break
    song, data = song
    player.load_file(song)
    player.play()
    print(data)
    while player.isPlaying():
        pass
        time.sleep(1)
print("Fin de la lista de reproduccion") 
""" 
import asyncio
import urwid
from player.Player import MusicPlayer
import playlist.PlayList as pl

palette = [
    ('pg_normal', 'white', 'black'),
    ('pg_complete', 'black', 'white'),
  
    ('selected', 'black', 'white'),
]

player = MusicPlayer()

playlist = pl.PlayList(player.valid_ext)

playlist.add("testmusic")

asyncio.get_event_loop().run_until_complete(player.play())


class CustomProgressBar(urwid.ProgressBar):
    def set_text(self, text: str) -> None:
        self.customtext=text
        
    def get_text(self) -> str:
        return self.customtext
     


 
 #logica de botones
 
def on_play_pause_button_click(button):
    pass

def on_stop_button_click(button):
    # Código para detener la música
    pass

def on_previous_button_click(button):
    # Código para ir a la canción anterior
    pass

def on_next_button_click(button):
    # Código para ir a la canción siguiente
    pass


 
 
 
 
 
 
 
 
# Creación de un widget de texto para el título, alineado en la parte superior
 
lista = urwid.SimpleFocusListWalker([]  )

 
 
 
 
for i in range(200):
    lista.append(urwid.AttrMap( urwid.Text(f"Item {i}"),None,focus_map='selected') )
 




# Creación de una lista de canciones
 
class CustomListBox(urwid.ListBox):
    def keypress(self, size, key):
        if key == 'down':
            try:
                self.set_focus(self.focus_position + 1)
            except IndexError:
                pass  # ya en el último elemento
        elif key == 'up':
            if self.focus_position > 0:
                self.set_focus(self.focus_position - 1)
        else:
            return super().keypress(size, key)
     
    def mouse_event(self, size, event, button, col, row, focus):
        if button == 4:
            self.keypress(size, 'up')
        elif button == 5:
            self.keypress(size, 'down')
         
        else:
            return super().mouse_event(size, event, button, col, row, focus)
        
#plisbx = urwid.ListBox(lista)

plisbx = CustomListBox(lista)

playlist = urwid.LineBox(plisbx, title="Lista de reproducción")

# Creación de un widget de edición para los comandos, alineado en la parte inferior
prompt =  urwid.LineBox(urwid.Edit(multiline=False), title="Comandos") 

progress_bar = CustomProgressBar('pg_normal', 'pg_complete', current=0, done=100 ) 

play_pause_button = urwid.Button('play ', on_press=on_play_pause_button_click)
stop_button = urwid.Button('stop', on_press=on_stop_button_click)
previous_button = urwid.Button('prev', on_press=on_previous_button_click)
next_button = urwid.Button('next', on_press=on_next_button_click)

buttons = urwid.GridFlow([previous_button, play_pause_button, stop_button, next_button], 8, 2, 0, 'center')


footer_stack = urwid.Pile([buttons, progress_bar, prompt])
frame = urwid.Frame(playlist, footer=footer_stack)
 
progress_bar.set_text("Cargando...")
progress_bar.set_completion(50)

# Creación del bucle principal con la pila y la paleta de colores
loop = urwid.MainLoop(frame, palette=palette )
 
# Ejecución del bucle principal
loop.run()



"""
        
handle input 



def handle_input(input):
    if input == 'media play':
        song = playlist.Next()
        if song is not None:
            song, data = song
            asyncio.create_task(play_song(song))
    elif input == 'media stop':
        stop_song()
    elif input == 'media next':
        song = playlist.Next()
        if song is not None:
            song, data = song
            asyncio.create_task(play_song(song))
    elif input == 'media prev':
        song = playlist.Prev()
        if song is not None:
            song, data = song
            asyncio.create_task(play_song(song))

urwid.MainLoop(widget, palette, event_loop=loop, unhandled_input=handle_input).run()        
        
"""