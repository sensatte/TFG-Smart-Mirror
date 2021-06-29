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
from kivy.clock import Clock

import db.dbWrapper as dbWrapper
import datetime

#import kv
from kivy.lang import Builder
Builder.load_file('kv/settingsScreen.kv')

class SettingsScreen(Screen):

    image=Properties.StringProperty(dbWrapper.getSaveScreen().image)
    showNotes=Properties.ObjectProperty(None)
    refreshImagesSchedule = Properties.ObjectProperty(None)

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}    
        self.showNotes.bind(minimum_height=self.showNotes.setter('height'))
        self.showSaveScreenFunc()
        Clock.schedule_interval(self.showSaveScreenFunc, 20)

    def showSaveScreenFunc(self, *args):
        imagenes = dbWrapper.getAllSaveScreen()

        try:
            children = self.showNotes.children.copy()
            for child in children:
                self.showNotes.remove_widget(child)
        except:
            pass

        for imagen in imagenes:
            selected = imagen.image == self.image
            fondo = Fondo(imagen=imagen.image, state="down" if selected else "normal")
            self.ids.showNotes.add_widget(fondo)

    def refreshImageList(self):
        imageName = dbWrapper.getSaveScreen().image
        self.fondo="images/saveScreen/"+imageName

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):        
        #self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"


class Fondo(ToggleButtonBehavior, Image):
    imagen=Properties.StringProperty("")
    def __init__(self, imagen, **kwargs):
        super(Fondo, self).__init__(**kwargs)
        self.imagen=imagen
        self.source="images/saveScreen/"+imagen

    def on_state(self, widget, value):
        if value == 'down' and self.imagen != "":
            dbWrapper.saveSaveScreen(self.imagen)
