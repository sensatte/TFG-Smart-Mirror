# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.app import App
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from kivy.animation import Animation

#import kv
from kivy.lang import Builder

Builder.load_file('kv/twitterConfig.kv')

import db.dbWrapper as dbWrapper


class TwitterConfig(Screen):
    #TODO no hay hueco en el menu

    colorInter = Properties.ListProperty([1, 1, 1, 1])
    activeInter = Properties.BooleanProperty(True)
    halign = Properties.StringProperty('left')

    def __init__(self, **kwargs):
        super(TwitterConfig, self).__init__(**kwargs)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}

    def changeHalign(self, halign):
        self.halign = halign

    def saveConfig(self):
        #guardar las configs
        print(self.activeInter)
        dbWrapper.saveTwitter(self.activeInter, self.colorInter, self.halign)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
