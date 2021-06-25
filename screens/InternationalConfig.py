# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.uix.image import Image
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from time import strftime

from customWidgets.infoDayResources.InternationalWidget import InternationalWidget

import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv/internationalConfig.kv')


class InternationalConfig(Screen):
    colorInter = Properties.ListProperty([1, 1, 1, 1])
    activeInter = Properties.BooleanProperty(True)

    def __init__(self, **kwargs):
        super(InternationalConfig, self).__init__(**kwargs)
        self.pos_hint = {'center_y': 0.5, 'center_x': 0.5}
        self.getAllInter()

    def printt(self, switch):
        print(switch.active)

    def saveConfig(self):
        # guardar las configs
        dbWrapper.saveInternationalConfig(
            "inter", self.colorInter if self.activeInter == False else [1, 1, 1, 0])

    def getAllInter(self):
        datos = dbWrapper.getAllInterByMonth(str(strftime('%m')))

        for j in datos:
            layout = BoxLayout(
                orientation='horizontal', size_hint_y=None, height=20, padding=[-40, 0, 0, 0])
            layout.add_widget(Texto(text=str(j.dia)))
            layout.add_widget(
                Texto(text=str(j.info if len(j.info) < 25 else '...'+j.info[10:35]+'...')))
            self.ids.todos.add_widget(layout)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"


class Texto(Label):
    font_size = 10
