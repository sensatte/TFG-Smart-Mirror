from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import kivy.properties as Properties
from kivy.clock import Clock
from kivy.event import EventDispatcher
from db.dbWrapper import getTemp

import requests
import json

id_endpoint = "http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=%s"

class TempWidget(Image, EventDispatcher):
    text = Properties.StringProperty('')
    unit = Properties.StringProperty()
    c_id=Properties.StringProperty()
    chosenColor = Properties.ListProperty()

    def on_text(self, *_):
            # Just get large texture:
            l = Label(text=self.text)
            l.font_size = '1000dp'  # something that'll give texture bigger than phone's screen size
            l.color = self.color
            l.texture_update()
            # Set it to image, it'll be scaled to image size automatically:
            self.texture = l.texture

    
    def __init__(self, **kwargs):
        super(TempWidget, self).__init__(**kwargs)

        
        currentTemp=getTemp()
        self.chosenColor=currentTemp.color
        self.unit=currentTemp.formato
        self.c_id=currentTemp.c_id
        self.color = self.chosenColor
        self.bind(chosenColor=self.update_temp)
        #Temperature
        self.text=str(int(getWeatherReducedByCityId(self.c_id, self.unit)['temp']))+"º"
        Clock.schedule_interval(self.update_temp, 200)
        
    def update_temp(self, *args):
        self.text = str(int(getWeatherReducedByCityId(self.c_id, self.unit)['temp']))+"º"
        self.color = self.chosenColor
        
def getWeatherReducedByCityId(city_id, units):
    """
    Returns a dictionary with entries for weather following one of the next values:  and current temperature

    Keyword arguments:

    city_id -- the numeric id of the city (default 6361046)

    units -- the unit system (default 'metric')
    """
    res = {}

    request = requests.get(id_endpoint % (city_id, "14ceb9ab023628e4d3304e9a8c46f4ba", units))

    if request.status_code != 200:
        pass

    else:
        result = json.loads(request.text)

        res['weather'] = result['weather'][0]['main']
        res['temp'] = result['main']['temp']

    return res