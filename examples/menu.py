from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<LoginScreen>:
    GridLayout:
        cols: 1
        padding: 15
        spacing: 50
        Button:
            size_hint_y: None
            height: '200sp'
        BoxLayout:
            size_hint_y: None
            height: 200
            orientation: 'horizontal'
            CheckBox:
                active: False
            CheckBox:
                active: True
<Scrolling>:
    do_scroll_x: False
    bar_margin: 0
    bar_width: 15
    bar_color: [.7,.7,.7,.9]
    bar_inactive_color: [.7,.7,.7,.9]
    scroll_type: ['bars','content']
""")

from kivy.app import App
from kivy.uix.screenmanager import (ScreenManager, Screen)
from kivy.uix.scrollview import ScrollView


class MainManager(ScreenManager):
    pass

class Scrolling(ScrollView):
    pass

class LoginScreen(Screen):
    pass

class QuestionApp(App):
    def build(self):
        AppSM = MainManager()
        AppSM.add_widget(LoginScreen(name='login'))
        return AppSM

if __name__ == '__main__':
    QuestionApp().run()