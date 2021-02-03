from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from datetime import datetime

class DateWidget(Label):
    
    def __init__(self, **kwargs):
        super(DateWidget, self).__init__(**kwargs)

        self.text=datetime.now().strftime("%d/%m/%y")       
        
        Clock.schedule_interval(self.update_time, 60)
        
    def update_time(self, *args):
        self.text = datetime.now().strftime("%d/%m/%y")
        