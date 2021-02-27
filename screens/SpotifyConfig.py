# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.uix.image import Image
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling

#import kv
from kivy.lang import Builder
Builder.load_file('kv/spotifyConfig.kv')


class SpotifyConfig(Screen):

    def __init__(self, **kwargs):
        super(SpotifyConfig, self).__init__(**kwargs)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
