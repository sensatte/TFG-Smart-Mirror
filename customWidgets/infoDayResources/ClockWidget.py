from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.image import Image
import kivy.properties as Properties
from datetime import datetime
from db.dbWrapper import getHora

class ClockWidget(Image):
    text = Properties.StringProperty('')    
    chosenColor = Properties.ListProperty()
    segundos = Properties.BooleanProperty()
    horas = Properties.StringProperty()

    def on_text(self, *_):
            # Just get large texture:z
            l = Label(text=self.text)
            l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
            l.color = self.color
            l.texture_update()
            # Set it to image, it'll be scaled to image size automatically:
            self.texture = l.texture
    
    def __init__(self, **kwargs):
        super(ClockWidget, self).__init__(**kwargs)
        currentHora=getHora()
        self.chosenColor=currentHora.color
        self.segundos=currentHora.formato[1]
        self.horas=currentHora.formato[0]
        self.color = self.chosenColor
        self.text = datetime.now().strftime(self.update_secondsAndFormat(self.segundos, self.horas))
        Clock.schedule_interval(self.update_time, 1)
        
        
    def update_time(self, *args):
        self.text = datetime.now().strftime(self.update_secondsAndFormat(self.segundos, self.horas))
        self.color = self.chosenColor

    def update_secondsAndFormat(self, seconds, formato):
        if (seconds==True and formato=="24h"):
            return '%H:%M:%S'
        elif (seconds==True and formato=="12h"):
            return '%I:%M:%S %p'
        elif (seconds==False and formato=="24h"):
            return '%H:%M'
        else: return '%I:%M %p'
    

