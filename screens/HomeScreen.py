import db.dbWrapper as dbWrapper
from kivy.uix.floatlayout import FloatLayout

from customWidgets.NewsWidget import NewsWidget
from customWidgets.TwitterWidget import TwitterWidget
from customWidgets.InfoDayWidget import InfoDayWidget
from customWidgets.QuotesWidget import QuotesWidget
from customWidgets.NotesWidget import NotesWidget, deleteNotes
from customWidgets.utils.BehaviorUtil import ImageButton
from customWidgets.SpotifyWidget import SpotifyWidget
from customWidgets.GifsWidget import GifsWidget

from kivy.uix.screenmanager import FadeTransition, RiseInTransition, Screen
from kivy.clock import Clock
from kivy.app import App

from kivy.core.window import Window

from kivy.properties import BooleanProperty

#import kv
from kivy.lang import Builder
Builder.load_file("kv/homeScreen.kv")


class HomeScreen(Screen):

    firstLoad = BooleanProperty(True)

    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, window, pos):
        if App.get_running_app().root.current != "save":
            try:
                Clock.unschedule(self.saveScreen)
            except:
                pass

        Clock.schedule_once(self.saveScreen, 100)

    def saveScreen(self, a):
        #Clock.unschedule(self.saveScreen)
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "save"

    def refreshPage(self):
        #Clock.schedule_once(self.saveScreen, 100)
        state = dbWrapper.getQuote().state
        stateTwitter = dbWrapper.getTwitter().state
        stateSpotify = dbWrapper.getSpotify().state
        stateNotes = dbWrapper.getNoteState().state
        stateInfo = dbWrapper.getInfoState().state
        stateGifs = dbWrapper.getGifState().state

        copiedList = self.children.copy()

        # for child in copiedList:
        #     if not isinstance(child, ImageButton) and not isinstance(child, SpotifyWidget):
        #         self.remove_widget(child)

        for child in copiedList:
            if isinstance(child, InfoDayWidget):
                self.remove_widget(child)

        if stateInfo == True:
            info = InfoDayWidget()
            self.add_widget(info)

        if self.firstLoad:

            if state == True:
                quote = QuotesWidget()
                self.add_widget(quote)

            if stateTwitter == True:
                twitter = TwitterWidget()
                self.add_widget(twitter)

            if stateSpotify == True:
                spotify = SpotifyWidget()
                self.add_widget(spotify)

            if stateNotes == True:
                notes = NotesWidget()
                self.add_widget(notes)

            if stateGifs == True:
                gifs = GifsWidget()
                self.add_widget(gifs)

            self.firstLoad = False

    def goToConfigScreen(self):
        self.parent.transition = FadeTransition(duration=.35)
        self.parent.current = 'menu'
