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
Builder.load_file('kv\\gifsConfig.kv')


class GifsConfig(Screen):
    ind = 0

    text = Properties.StringProperty()

    imgurWrapper = ImgurWrapper()
    rvData = Properties.ListProperty()

    currentGifsData = Properties.ListProperty()

    waitUntilFinishesTypingEvent = Properties.ObjectProperty()

    activeInter = Properties.BooleanProperty(True)

    def __init__(self, **kwargs):
        super(GifsConfig, self).__init__(**kwargs)

        self.backg = [0, 0, 0, 0]
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        # self.showGifs(gifsList)
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
        #guardar las configs
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

    # def showGifs(self, gifsList):

    #     for child in self.ids.showGifs.children:
    #         self.ids.showGifs.remove_widget(child)

    #     for gif in gifsList:
    #         self.ids.showGifs.add_widget(self.showGif(gif, self.ind))
    #         self.ind += 1

    # def showGif(self, gif, idwidget):
    #     layout = GridLayout(cols=1, spacing=[0, 7])
    #     layout.id = idwidget

    #     layout.add_widget(
    #         GifConfig(
    #             imagenId=gif._id,
    #             source=gif.source,
    #             pinned=gif.pinned,
    #             anim_delay=gif.delay
    #         )
    #     )
    #     botones = BoxLayout(orientation='horizontal')
    #     botones.add_widget(self.createButton(gif._id, idwidget, "trash"))

    #     layout.add_widget(botones)
    #     return layout

    # def createButton(self, gifid, idwidget, image):
    #     button = ImageButton(gif=gifid, idwidget=idwidget, source="images/menu/" +
    #                          image+".png", size_hint_y=None, size_hint=(.8, .8))
    #     button.bind(on_press=self.deleteGif)
    #     return button

    # def deleteGif(self, button):
    #     dbWrapper.deleteGifById(button.gif)
    #     for child in self.ids.showGifs.children:
    #         if child.id == button.idwidget:
    #             borrar = child
    #             break

    #     self.ids.showGifs.remove_widget(borrar)

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
