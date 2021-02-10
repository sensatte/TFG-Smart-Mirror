from customWidgets.SpotifyWidget import SpotifyWidget
from utils.volume import VolumeWid
from menu.Screens import Screens
import kivy
kivy.require('1.11.1')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

Window.size = (540,960)

from customWidgets.NewsWidget import NewsWidget
from customWidgets.RootLayout import RootLayout
from customWidgets.InfoDayWidget import InfoDayWidget
from customWidgets.QuotesWidget import QuotesWidget
from customWidgets.NotesWidget import NotesWidget

class SmartMirrorApp(App):

    def build(self):

        widgets = []

        spotifyWidget = SpotifyWidget()
        widgets.append(spotifyWidget)

        volumeWidget=VolumeWid()
        widgets.append(volumeWidget)

        
        infoDay = InfoDay(size_hint=(.3, .15), pos_hint={
                          "x": 0, "top": 1})
        widgets.append(infoDay)

        # quotes = QuotesWidget()  
        # widgets.append(quotes)

        # notes = NotesWidget()  
        # widgets.append(notes)

        test = Screens()
        widgets.append(test)
        
        root_layout = RootLayout()

        for widget in widgets:
            root_layout.add_widget(widget)

        return root_layout


if __name__ == '__main__':

    #GPIO to Keyboard Translate
    # gpio_translate_thread = threading.Thread(target=gpio_translate, name='GPIO Translation')
    # gpio_translate_thread.daemon = True
    # gpio_translate_thread.start()
    
    SmartMirrorApp().run()
