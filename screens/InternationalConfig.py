# pylint: disable=no-member

from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as Properties
from kivy.uix.image import Image 
from kivy.app import App
from kivy.animation import Animation
from functools import partial
from kivy.uix.screenmanager import FadeTransition
from customWidgets.utils.BehaviorUtil import ImageButton, Scrolling

from customWidgets.infoDayResources.InternationalWidget import InternationalWidget

import db.dbWrapper as dbWrapper

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\internationalConfig.kv')

class InternationalConfig(Screen):
    #TODO color picker
    #TODO al abrirse se pone la config por defecto pero no funciona cambiar el state para que mire la db
    colorInter=Properties.ListProperty([1,1,1,1])
    activeInter=Properties.BooleanProperty(True)

    def __init__(self, **kwargs):
        super(InternationalConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}    

    def printt(self, switch):
        print(switch.active)    

    def saveConfig(self):
        #guardar las configs
        print(self.activeInter)
        dbWrapper.saveInternationalConfig("inter", self.colorInter if self.activeInter == False else [1,1,1,0])        

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.goToMenuScreen))
        anim.start(widget)

    def goToMenuScreen(self, widget, selected):        
        self.saveConfig()
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = "menu"
