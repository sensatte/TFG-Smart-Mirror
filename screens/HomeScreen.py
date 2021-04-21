import db.dbWrapper as dbWrapper
from kivy.uix.floatlayout import FloatLayout

from customWidgets.NewsWidget import NewsWidget
from customWidgets.TwitterWidget import TwitterWidget
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
        # volumeWidget=VolumeWid()
        # widgets.append(volumeWidget)

    def refreshPage(self):
        state = dbWrapper.getQuote().state
        stateTwitter = dbWrapper.getTwitter().state
        stateSpotify = dbWrapper.getSpotify().state
        stateNotes = dbWrapper.getNoteState().state
        stateInfo = dbWrapper.getInfoState().state
        stateGifs = dbWrapper.getGifState().state

        print("Before deleting", self.children)

        i = 0
        while len(self.children) > 1:
            print("Trying to delete ", self.children[i])
            if not isinstance(self.children[i], ImageButton):
                self.remove_widget(self.children[i])
            else:
                i = 1

        print("Before adding", self.children)

        if state == True:
            quote = QuotesWidget()
            self.add_widget(quote)

        if stateTwitter == True:
            twitter = TwitterWidget()
            self.add_widget(twitter)

        if stateSpotify == True:
            spotify = SpotifyWidget2()
            self.add_widget(spotify)

        if stateNotes == True:
            notes = NotesWidget()
            self.add_widget(notes)

        if stateInfo == True:
            info = InfoDayWidget()
            self.add_widget(info)

        if stateGifs == True:
            gifs = GifsWidget()
            self.add_widget(gifs)

        print("After adding", self.children)

    def goToConfigScreen(self):
        self.parent.transition = FadeTransition(duration=.35)
        self.parent.current = 'menu'
