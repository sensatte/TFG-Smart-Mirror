# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
import kivy.properties as Properties
from kivy.uix.behaviors import ButtonBehavior  
from kivy.uix.image import Image 
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition

from customWidgets.infoDayResources.DateWidget import DateWidget
from customWidgets.infoDayResources.WeatherWidget import WeatherWidget
from customWidgets.infoDayResources.TempWidget import TempWidget
from customWidgets.infoDayResources.ClockWidget import ClockWidget

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\configs.kv')

class InfoDayConfig(Screen):
    #TODO hacer el kv que se pueda usar pa mas gente
    #TODO color picker
    #TODO la fecha tarda mucho en actualizarse
    #TODO poder poner la id de ciudad para temp y weather
    #TODO que las anim las coja de otro archivo
    
    def __init__(self, **kwargs):
        super(InfoDayConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}


    def secondsClock(self, checkboxInstance):
        if checkboxInstance.text=="Sí":
            ClockWidget.seconds=True
            print("Segundos activados")
        elif checkboxInstance.text=="No":
            ClockWidget.seconds=False
            print("Segundos desactivados")

    def colorClock(self, checkboxInstance):
        ClockWidget.chosenColor = checkboxInstance.color
        print("Color cambiado a ", checkboxInstance.color)

    def formatClock(self, checkboxInstance):
        ClockWidget.formato=checkboxInstance.text
        print("Formato hora: ", checkboxInstance.text)


    def formatDate(self, checkboxInstance):
        DateWidget.formato=checkboxInstance.text
        print("Formato fecha: ", checkboxInstance.text)

    def colorDate(self, checkboxInstance):
        DateWidget.chosenColor = checkboxInstance.color
        # DateWidget.update_time(DateWidget)
        print("Color cambiado a ", checkboxInstance.color)


    def unitsTemp(self, checkboxInstance):
        if checkboxInstance.text=="Celcius":
            TempWidget.unit="metric"
        elif checkboxInstance.text=="Fahrenheit":
            TempWidget.unit="imperial"
        print("Unidades temperatura: ", checkboxInstance.text)

    def colorTemp(self, checkboxInstance):
        TempWidget.chosenColor = Properties.ListProperty(checkboxInstance.color)
        # TempWidget.update_time(TempWidget)
        print("Color cambiado a ", checkboxInstance.color)

    def themeWeather(self, checkboxInstance):
        WeatherWidget.theme = checkboxInstance
        print("Cambiado a tema: ", checkboxInstance)

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"

class ImageButton(ButtonBehavior, Image):  
    pass


class Scrolling(ScrollView):
    pass