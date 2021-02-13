from kivy.uix.button import Button
from kivy.uix.screenmanager import FallOutTransition, Screen
from customWidgets.ImageButton import ImageButton
from kivy.uix.gridlayout import GridLayout

#import kv
from kivy.lang import Builder
Builder.load_file("kv/menuScreen.kv")


class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        widgets = []

        homeButton = self.ids.homeButton
        homeButton.on_press = self.goToHomeScreen

        optionsGrid = GridLayout(
            cols=3,
            rows=3,
            pos_hint={"center_x": .5, "center_y": .5},
            size_hint=(.7, .7)
        )

        optionsGrid.add_widget(Button(text='Hello 1'))
        optionsGrid.add_widget(Button(text='World 1'))
        optionsGrid.add_widget(Button(text='Hello 2'))
        optionsGrid.add_widget(Button(text='World 2'))

        widgets.append(optionsGrid)

        for i in widgets:
            self.add_widget(i)

    def goToHomeScreen(self,):
        print("caramelizada")
        self.parent.transition = FallOutTransition(duration=.75)
        self.parent.current = 'home'
