from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

import requests
import json

id_endpoint = "http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=%s"

class TempWidget(Label):
    
    def __init__(self, **kwargs):
        super(TempWidget, self).__init__(**kwargs)
        # self.anchor_x = 'left'
        # self.anchor_y = 'center'
        # self.size_hint =(.2, .2)
        # self.pos_hint ={"x":0.02, "y":0.75}

        #Temperature
        self.text=str(int(getWeatherReducedByCityId()['temp']))+"º"
        
def getWeatherReducedByCityId(city_id='6361046', units="metric"):
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