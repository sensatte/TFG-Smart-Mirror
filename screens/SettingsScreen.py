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
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.image import Image

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv/settingsScreen.kv')

class SettingsScreen(Screen):
    colorHora=Properties.ListProperty([1,1,1,1])
    formatoHora=Properties.ListProperty(["24h", False])

    colorTemp=Properties.ListProperty([1,1,1,1])
    formatoTemp=Properties.StringProperty("metric")

    formatoClima=Properties.NumericProperty(2)

    image=Properties.StringProperty('wolf')
    showNotes=Properties.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}    
        self.showNotes.bind(minimum_height=self.showNotes.setter('height'))
        self.showSaveScreenFunc()  


    def showSaveScreenFunc(self):
        imagenes = dbWrapper.getAllSaveScreen()
        for imagen in imagenes:
            self.ids.showNotes.add_widget(Fondo(imagen=imagen.image))

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


class Fondo(ToggleButtonBehavior, Image):
    imagen=Properties.StringProperty("")
    def __init__(self, imagen, **kwargs):
        super(Fondo, self).__init__(**kwargs)
        self.imagen=imagen
        self.source="images/saveScreen/"+imagen

    def saveSaveScreen(self):
        dbWrapper.saveSaveScreen(self.imagen)

    def on_state(self, widget, value):
        if value == 'down':
            self.saveSaveScreen()