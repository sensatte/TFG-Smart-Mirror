from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import FadeTransition, Screen
from customWidgets.utils.BehaviorUtil import ImageButton
from customWidgets.utils.Animations import fadeIn, fadeOut
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.app import App
from functools import partial

from customWidgets.utils import Animations

#import kv
Builder.load_file("kv/menuScreen.kv")


class MenuScreen(Screen):

    # TODO que las animacines se cojan de un archivo distinto
    # TODO poner botones que lleven a la otra pagina?)
    # TODO poner bolitasw que indiquen en que pagina estas

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        widgetList = ['gym', "international", "clock", "drawing",
                      "quotes", "notes", "spotify", "gifs", "settings"]
        self.maxCols = 3
        self.maxRows = 3
        self.itemMatrix = {}
        ind = 0
        for i in range(self.maxCols):
            for j in range(self.maxRows):
                self.itemMatrix[ind] = (i, j)
                ind += 1

        self.insertIcons(widgetList)

    def insertIcons(self, widgetList):
        c = 1/self.maxCols
        r = 1/self.maxRows
        for i in range(len(widgetList)):
            if (i <= 9):
                boton = ImageButton(keep_ratio=True, allow_stretch=True,
                                    source="images/menu/" + widgetList[i] + ".png")
                boton.pos_hint = {
                    'center_x': c * (self.itemMatrix[i][0])+c/2, 'center_y': r * (self.itemMatrix[i][1])+r/2}
                boton.on_press = partial(
                    self.pressedOption, boton, widgetList[i])
                boton.size_hint = .25, .25
                self.ids.optionsGridone.add_widget(boton)
            else:
                pass

    def goToHomeScreen(self, widget, selected):
        self.parent.transition = FadeTransition(duration=.25)
        self.parent.current = 'home'

    def pressedOption(self, widget, selected):
        anim = Animation(size_hint=(0.2, 0.2), duration=.1)
        anim += Animation(opacity=0, size_hint=(0.3, 0.3), duration=.2)

        anim.bind(on_complete=partial(self.openSelected, selected))
        anim += Animation(opacity=1, size_hint=(0.25, 0.25), duration=.2)
        anim.start(widget)

    def openSelected(self, selected, *args):
        # #llama al método de la animación con el widget de selected item
        App.get_running_app().root.transition = FadeTransition(duration=.3)
        App.get_running_app().root.current = selected

    def pressedBack(self, widget):
        anim = Animation(pos_hint={"center_x": .5, "y": -.03}, duration=.1)
        anim += Animation(pos_hint={"center_x": .5, "y": 0}, duration=.1)
        anim.bind(on_complete=partial(self.fadeOut))
        anim.start(widget)

    def fadeIn(self):
        anim = Animation(
            pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=.5)
        anim &= Animation(size_hint=(.5, .4), duration=.5)
        anim.start(self.ids.caja)

    def fadeOut(self, widget, selected):
        anim = Animation(
            pos_hint={'center_x': 0.5, 'center_y': -.5}, duration=.5)
        anim &= Animation(size_hint=(.4, .3), duration=.5)
        anim.bind(on_complete=partial(self.goToHomeScreen))
        anim.start(self.ids.caja)
