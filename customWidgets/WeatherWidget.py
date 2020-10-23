from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

class WeatherWidget (AnchorLayout):
    
    def __init__(self, **kwargs):
        super(WeatherWidget, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.size_hint =(.2, .2)
        self.pos_hint ={"x":0.8, "y":0.5}