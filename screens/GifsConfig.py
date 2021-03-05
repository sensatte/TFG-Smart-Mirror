# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import GifConfig, ImageButton, Scrolling, ColoredLabelConfig
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\gifsConfig.kv')


class GifsConfig(Screen):
    # TODO hacer el kv que se pueda usar pa mas gente
    # TODO color picker
    # TODO que las anim las coja de otro archivo
    # TODO poner pestaña para crear nota
    # TODO quje no puedas enviar nota vacia

    def __init__(self, **kwargs):
        super(GifsConfig, self).__init__(**kwargs)
        self.backg = [0, 0, 0, 0]
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        gifsList = dbWrapper.getAllGifs()
        self.showGifs(gifsList)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def showGifs(self, gifsList):
        for gif in gifsList:
            self.ids.showGifs.add_widget(
                GifConfig(imagenId=gif._id, source=gif.source, pinned=gif.pinned, anim_delay=gif.delay))

    def writeGif(self, source, size):
        dbWrapper.saveGif(source, size)
