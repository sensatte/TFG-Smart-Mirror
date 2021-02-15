from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
import kivy.properties as Properties

from datetime import datetime

class DateWidget(Image):
    text = Properties.StringProperty('')

    def on_text(self, *_):
            # Just get large texture:
            l = Label(text=self.text)
            l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
            l.texture_update()
            # Set it to image, it'll be scaled to image size automatically:
            self.texture = l.texture

    def __init__(self, **kwargs):
        super(DateWidget, self).__init__(**kwargs)

        self.text=datetime.now().strftime("%d/%m")       
        
        Clock.schedule_interval(self.update_time, 60)
        
    def update_time(self, *args):
        self.text = datetime.now().strftime("%d/%m")
        