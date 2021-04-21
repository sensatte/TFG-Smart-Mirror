from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\saveScreen.kv')


class SaveScreen(Screen):

    

    def __init__(self, **kwargs):
        super(SaveScreen, self).__init__(**kwargs)

    def goToMenuScreen(self, widget):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "home"
