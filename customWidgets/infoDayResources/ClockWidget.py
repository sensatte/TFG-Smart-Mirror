from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime

class ClockWidget(Label):
    
    def __init__(self, **kwargs):
        super(ClockWidget, self).__init__(**kwargs)
        
        self.text = datetime.now().strftime('%H:%M')
        
        Clock.schedule_interval(self.update_time, 1)
        
        
    def update_time(self, *args):
        self.text = datetime.now().strftime('%H:%M')
        
        
