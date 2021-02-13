from kivy.uix.floatlayout import FloatLayout

from customWidgets.NewsWidget import NewsWidget
from customWidgets.InfoDayWidget import InfoDayWidget
from customWidgets.QuotesWidget import QuotesWidget
from customWidgets.NotesWidget import NotesWidget
from customWidgets.SpotifyWidget import SpotifyWidget
from customWidgets.ImageButton import ImageButton
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

        infoDay = InfoDayWidget(size_hint=(.3, .15), pos_hint={
            "x": 0, "top": 1})
        widgets.append(infoDay)

        # quotes = QuotesWidget()
        # widgets.append(quotes)

        # notes = NotesWidget()
        # widgets.append(notes)

        menuButton = self.ids.menuButton
        menuButton.on_press = self.goToConfigScreen

        for i in widgets:
            self.add_widget(i)

    def goToConfigScreen(self,):
        print("aceituna")
        self.parent.transition = RiseInTransition(duration=.75)
        self.parent.current = 'menu'
