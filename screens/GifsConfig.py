# pylint: disable=no-member
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from customWidgets.utils.BehaviorUtil import GifConfig, ImageButton, Scrolling, ColoredLabelConfig
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\gifsConfig.kv')


class GifsConfig(Screen):
    ind = 0

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
            self.ids.showGifs.add_widget(self.showGif(gif, self.ind))
            self.ind += 1

        # for gif in gifsList:
        #     self.ids.showGifs.add_widget(
        #         GifConfig(
        #             imagenId=gif._id,
        #             source=gif.source,
        #             pinned=gif.pinned,
        #             anim_delay=gif.delay
        #         ))

    def showGif(self, gif, idwidget):
        layout = GridLayout(cols=1, spacing=[0, 7])
        layout.id = idwidget

        layout.add_widget(
            GifConfig(
                imagenId=gif._id,
                source=gif.source,
                pinned=gif.pinned,
                anim_delay=gif.delay
            )
        )
        botones = BoxLayout(orientation='horizontal')
        botones.add_widget(self.createButton(gif._id, idwidget, "trash"))

        layout.add_widget(botones)
        return layout

    def createButton(self, gifid, idwidget, image):
        button = ImageButton(gif=gifid, idwidget=idwidget, source="images/menu/" +
                             image+".png", size_hint_y=None, size_hint=(.8, .8))
        button.bind(on_press=self.deleteGif)
        return button

    def deleteGif(self, button):
        dbWrapper.deleteGifById(button.gif)
        for child in self.ids.showGifs.children:
            if child.id == button.idwidget:
                borrar = child
                break

        self.ids.showGifs.remove_widget(borrar)

    def writeGif(self, source):
        dbWrapper.saveGif(source)
