from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

#import kv
from kivy.lang import Builder
Builder.load_file('kv\\configs.kv')

class InfoDayConfig(BoxLayout):
    #TODO hacer el kv que se pueda usar pa mas gente
    def __init__(self, **kwargs):
        super(InfoDayConfig, self).__init__(**kwargs)
        self.pos_hint={'center_y': 0.5, 'center_x': 0.5}
        self.add_widget(Label(text="Reloj/Fecha"))

        checkbox = CheckBox()
        checkbox.bind(active=on_checkbox_active)

def on_checkbox_active(self, checkbox, value):
    if value:
        print('The checkbox', checkbox, 'is active')
    else:
        print('The checkbox', checkbox, 'is inactive')