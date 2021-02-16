from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import FallOutTransition, Screen
from customWidgets.ImageButton import ImageButton
from kivy.uix.gridlayout import GridLayout

#import kv
Builder.load_file("kv/menuScreen.kv")


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        pass

    def goToHomeScreen(self,):
        print("caramelizada")
        self.parent.transition = FallOutTransition(duration=.75)
        self.parent.current = 'home'
