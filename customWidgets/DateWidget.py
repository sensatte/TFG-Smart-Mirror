from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime

class DateWidget(AnchorLayout):
    
    def __init__(self, **kwargs):
        super(DateWidget, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.size_hint =(.2, .2)
        self.pos_hint ={"x":0.15, "y":0.75}
        
        self.time_label = Label (text=datetime.now().strftime("%d/%m/%y"),
                            font_size=15
                            )
        
        self.add_widget(self.time_label)
        
        Clock.schedule_interval(self.update_time, 60)
        
        
    def update_time(self, *args):
        self.time_label.text = datetime.now().strftime("%d/%m/%y")
        