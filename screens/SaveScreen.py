from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties
import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv/saveScreen.kv')


class SaveScreen(Screen):
    fondo=Properties.StringProperty()    

    def __init__(self, **kwargs):
        super(SaveScreen, self).__init__(**kwargs)
        imageName = dbWrapper.getSaveScreen().image
        self.fondo="images/saveScreen/"+imageName

    def refreshImage(self):
        imageName = dbWrapper.getSaveScreen().image
        self.fondo="images/saveScreen/"+imageName

    def goToHomeScreen(self, widget):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "home"
