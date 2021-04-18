# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.uix.image import Image 
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling

from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget

import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\infoConfig.kv')

class InfoDayConfig(Screen):
    #TODO buscador ue te traduzca de ciudad a id
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

    def __init__(self, **kwargs):
        super(InfoDayConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}        

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
        

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):        
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
