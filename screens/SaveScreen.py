from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
import kivy.properties as Properties
import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv/saveScreen.kv')


class SaveScreen(Screen):
    fondo=Properties.StringProperty()    

    def __init__(self, **kwargs):
        super(SaveScreen, self).__init__(**kwargs)
        self.fondo=dbWrapper.getSaveScreen().image
        print(self.fondo)

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
        
       

    def goToHomeScreen(self, widget):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "home"
