# pylint: disable=no-member
from customWidgets.utils.BehaviorUtil import ColoredLabelConfig, ImageButton, Scrolling
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\settingsScreen.kv')

class SettingsScreen(Screen):
    colorHora=Properties.ListProperty([1,1,1,1])
    formatoHora=Properties.ListProperty(["24h", False])

    colorFecha=Properties.ListProperty([1,1,1,1])
    formatoFecha=Properties.StringProperty("dd/mm")

    colorTemp=Properties.ListProperty([1,1,1,1])
    formatoTemp=Properties.StringProperty("metric")

    formatoClima=Properties.NumericProperty(2)

    c_id=Properties.StringProperty('6361046')
    activeInter = Properties.BooleanProperty(True)
    image=Properties.StringProperty('wolf')

    currentGifsData = Properties.ListProperty()

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}        

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
        dbWrapper.saveSaveScreen(self.image)        

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):        
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
