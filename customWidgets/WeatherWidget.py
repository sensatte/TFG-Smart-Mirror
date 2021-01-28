from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image

import requests
import json

id_endpoint = "http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=%s"

class WeatherWidget (AnchorLayout):
    
    def __init__(self, **kwargs):
        super(WeatherWidget, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'
        self.size_hint =(.2, .2)
        self.pos_hint ={"x":0.075, "y":0.75}

        #Weather
        self.add_widget(Image(source=switch_demo(getWeatherReducedByCityId()['weather'],2), 
                allow_stretch=True, keep_ratio=False,
                size_hint =(.2, .2)
                ))

        
def switch_demo(argument, theme):
    path = "images/icons/"
    switcher = {
        "Clear": "01.png",
        "Clouds": "02.png",
        "Drizzle": "03.png",
        "Rain": "04.png",
        "Mist": "08.png",
        "Smoke": "08.png",
        "Haze": "08.png",
        "Dust": "08.png",
        "Fog": "08.png",
        "Sand": "08.png",
        "Ash": "08.png",
        "Squall": "08.png",
        "Tornado": "08.png",
        "Snow": "06.png",
        "Thunderstorm": "05.png"
    }
    themes = {
        1: "weather_min/",
        2: "weather_medmin/",
        3: "weather_supper/"
    }
    return path+themes[theme]+switcher[argument]
        
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
