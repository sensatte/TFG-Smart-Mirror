# pylint: disable=no-member
import logging

from kivy.clock import Clock
from utils.ImgurWrapper import ImgurWrapper
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from customWidgets.utils.BehaviorUtil import GifConfig, ImageButton, Scrolling, ColoredLabelConfig, AsyncImageButton
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties

import db.dbWrapper as dbWrapper
import datetime

from functools import partial

#import kv
from kivy.lang import Builder
Builder.load_file('kv/gifsConfig.kv')


class GifsConfig(Screen):
    ind = 0

    text = Properties.StringProperty()

    imgurWrapper = ImgurWrapper()
    rvData = Properties.ListProperty()

    currentGifsData = Properties.ListProperty()

    waitUntilFinishesTypingEvent = Properties.ObjectProperty()

    activeInter = Properties.BooleanProperty(False)

    def __init__(self, **kwargs):
        super(GifsConfig, self).__init__(**kwargs)

        self.backg = [0, 0, 0, 0]
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        self.updateCurrentGifsData()

    def updateCurrentGifsData(self):
        gifsList = dbWrapper.getAllGifs()
        self.currentGifsData = [
            {
                "imagenId": gif._id,
                "source": gif.source,
                "pinned": gif.pinned,
                "anim_delay": gif.delay,
                "updateListFunction": self.updateCurrentGifsData
            } for gif in gifsList
        ]

    def saveConfig(self):
        print(self.activeInter)
        dbWrapper.saveGifState(self.activeInter)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

    def writeGif(self, source):
        dbWrapper.saveGif(source)

    def textChanged(self, text):

        try:
            self.waitUntilFinishesTypingEvent.cancel()
        except:
            logging.info('Gifs: No previous event')

        self.text = text
        self.waitUntilFinishesTypingEvent = Clock.schedule_once(
            self.updateData, 2)

    def updateData(self, dt):
        dataList = self.imgurWrapper.search(self.text)
        self.rvData = [
            {
                'source': x,
                "on_press": partial(self.pressedImage, x),
            } for x in dataList if x[-3:] != "mp4"]

    def pressedImage(self, pressedImage):
        self.writeGif(pressedImage)
        self.goToMenuScreen(None, None)
        self.updateCurrentGifsData()

    def on_rvData(self, instance, value):
        self.ids.imgurRV.data = value
