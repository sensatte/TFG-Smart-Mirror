from kivy.uix.button import Button
from kivy.uix.screenmanager import FallOutTransition, Screen
from customWidgets.ImageButton import ImageButton
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import CardTransition
from kivy.app import App
from functools import partial

#import kv
from kivy.lang import Builder
Builder.load_file("kv/menuScreen.kv")


class MenuScreen(Screen):
    #TODO arreglar las animaciones
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        widgetList=['schedule', "news", "settings", "at", "clock", "schedule", "settings", "settings", "settings"]
        self.insertIcons(widgetList)
        pass

    def insertIcons(self, widgetList):
        for i in range(len(widgetList)):
            if (i <= 9):
                boton=ImageButton(keep_ratio= True, allow_stretch= True, 
                    source= "images/menu/" + widgetList[i] + ".png")
                boton.on_press = partial(self.pressedOption, boton, widgetList[i])
                self.ids.optionsGridone.add_widget(boton)
            else:
                pass

    def goToHomeScreen(self):
        self.parent.transition = FallOutTransition(duration=.75)
        self.parent.current = 'home'


    def pressedOption(self, widget, selected):
        anim = Animation(size_hint=(0.2,0.2), duration=.1)
        anim += Animation(opacity=0,size_hint=(0.3,0.3), duration=.2)
        
        # anim.bind(on_complete=partial(self.openSelected, selected))
        anim += Animation(opacity=1, duration=.2)
        anim.start(widget)

    def openSelected(self, selected, *args):
        # #llama al método de la animación con el widget de selected item        
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = selected

