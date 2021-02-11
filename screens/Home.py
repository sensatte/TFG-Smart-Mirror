from kivy.uix.floatlayout import FloatLayout

from customWidgets.NewsWidget import NewsWidget
from customWidgets.InfoDayWidget import InfoDayWidget
from customWidgets.QuotesWidget import QuotesWidget
from customWidgets.NotesWidget import NotesWidget
from customWidgets.SpotifyWidget import SpotifyWidget
from utils.volume import VolumeWid

class Home(FloatLayout):

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        widgets = []

        # spotifyWidget = SpotifyWidget()
        # widgets.append(spotifyWidget)

        # volumeWidget=VolumeWid()
        # widgets.append(volumeWidget)
        
        infoDay = InfoDayWidget(size_hint=(.3, .15), pos_hint={
                          "x": 0, "top": 1})
        widgets.append(infoDay)

        # quotes = QuotesWidget()  
        # widgets.append(quotes)

        # notes = NotesWidget()  
        # widgets.append(notes)

        for i in widgets:
            self.add_widget(i)