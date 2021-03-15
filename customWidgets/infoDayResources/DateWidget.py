from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
import kivy.properties as Properties
from db.dbWrapper import getFecha

from datetime import datetime

class DateWidget(Image):
    #TODO qie se actualice al ser las 00:00
    text = Properties.StringProperty('')
    chosenColor = Properties.ListProperty()
    formato= Properties.StringProperty()
    def on_text(self, *_):
            # Just get large texture:
            l = Label(text=self.text)
            l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
            l.color=self.color
            l.texture_update()
            # Set it to image, it'll be scaled to image size automatically:
            self.texture = l.texture

    def __init__(self, **kwargs):
        super(DateWidget, self).__init__(**kwargs)
        currentFecha=getFecha()
        self.chosenColor=currentFecha.color
        self.formato=currentFecha.formato
        self.color = self.chosenColor
        self.text=datetime.now().strftime(self.update_Format()) 
        Clock.schedule_interval(self.update_time, 60)
        
    def update_time(self, *args):
        self.text = datetime.now().strftime(self.update_Format())
        self.color = self.chosenColor
        
    def update_Format(self):
        if (self.formato=="dd/mm"):
            return '%d/%m'
        elif (self.formato=="dd/mm/yyyy"):
            return '%d/%m/%y'
        elif (self.formato=="mm/dd"):
            return '%m/%d'
        else: return '%m/%d/%y'