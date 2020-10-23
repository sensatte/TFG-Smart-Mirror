from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime

class ClockWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(ClockWidget, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.size_hint =(.2, .2)
        self.pos_hint ={"x":0.1, "y":0.8}
        
        self.time_label = Label (text=datetime.now().strftime('%H:%M:%S'),
                            font_size=40 #Default 15
                            )
        
        self.add_widget(self.time_label)
        
        Clock.schedule_interval(self.update_time, 1)
        
        
    def update_time(self, *args):
        self.time_label.text = datetime.now().strftime('%H:%M:%S')
        
        
