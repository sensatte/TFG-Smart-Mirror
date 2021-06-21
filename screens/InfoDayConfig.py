# pylint: disable=no-member

import time
from functools import partial
from time import strftime

import db.dbWrapper as dbWrapper
import kivy.properties as Properties
from customWidgets.infoDayResources.ClockWidget import ClockWidget
from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
#import kv
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import FadeTransition, Screen, ScreenManager

Builder.load_file('kv\\infoConfig.kv')

class InfoDayConfig(Screen):
    #TODO al abrirse se pone la config por defecto pero no funciona cambiar el state para que mire la db
    colorHora=Properties.ListProperty([1,1,1,1])
    formatoHora=Properties.ListProperty(["24h", False])

    colorFecha=Properties.ListProperty([1,1,1,1])
    formatoFecha=Properties.StringProperty("dd/mm")

    colorTemp=Properties.ListProperty([1,1,1,1])
    formatoTemp=Properties.StringProperty("metric")

    formatoClima=Properties.NumericProperty(2)

    c_id=Properties.StringProperty('6361046')
    activeInter = Properties.BooleanProperty(True)
    
    colorInter = Properties.ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(InfoDayConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}
        self.getAllInter()

    def saveConfig(self):
        #guardar las configs
        if self.ids.textinput.text=="":
            self.c_id=self.ids.textinput.hint_text
        else:
            self.c_id=self.ids.textinput.text
        dbWrapper.saveHora("hora", self.formatoHora, self.colorHora)
        dbWrapper.saveFecha("fecha", self.formatoFecha, self.colorFecha)
        dbWrapper.saveTemp("temp", self.formatoTemp, self.colorTemp, self.c_id)
        dbWrapper.saveClima("weather", self.formatoClima, self.c_id)
        dbWrapper.saveInfoState(self.activeInter)
        dbWrapper.saveInternationalConfig(
            "inter", self.colorInter)

        
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
