from kivy.uix.floatlayout import FloatLayout

from customWidgets.NewsWidget import NewsWidget
from customWidgets.InfoDayWidget import InfoDayWidget
from customWidgets.QuotesWidget import QuotesWidget
from customWidgets.NotesWidget import NotesWidget, deleteNotes
from customWidgets.SpotifyWidget import SpotifyWidget
from customWidgets.utils.BehaviorUtil import ImageButton
from customWidgets.SpotifyWidget2 import SpotifyWidget2
from customWidgets.GifsWidget import GifsWidget
from utils.volume import VolumeWid
from kivy.uix.screenmanager import FadeTransition, RiseInTransition, Screen

#import kv
from kivy.lang import Builder
Builder.load_file("kv/homeScreen.kv")


class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        widgets = []

        # spotifyWidget = SpotifyWidget()
        # widgets.append(spotifyWidget)

        # volumeWidget=VolumeWid()
        # widgets.append(volumeWidget)

        infoDay = InfoDayWidget()
        widgets.append(infoDay)

        quotes = QuotesWidget()
        widgets.append(quotes)

        notes = NotesWidget()
        widgets.append(notes)

        for i in widgets:
            self.add_widget(i)

        
    def refreshPage(self):
        #TODO echar cuenta a esto porque como se vaya del inicio de la lista veras
        self.remove_widget(self.children[__name__=="notas"])
        notes = NotesWidget()
        self.remove_widget(self.children[__name__=="infoDay"])
        infoday = InfoDayWidget()

        self.add_widget(notes)
        self.add_widget(infoday)

    def goToConfigScreen(self):
        self.parent.transition = FadeTransition(duration=.35)
        self.parent.current = 'menu'
