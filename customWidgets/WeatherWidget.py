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
        self.pos_hint ={"x":0.05, "y":0.75}

        #Temperature
        #self.add_widget(Label(text=str(int(getWeatherReducedByCityId()['temp']))+"º"))

        #Weather
        #self.add_widget(Label(text=getWeatherReducedByCityId()['weather']))

        #self.add_widget(Image(source=switch_demo(getWeatherReducedByCityId()['weather']), 

        self.add_widget(Image(source="images/icons/weather_medmin/001-cloud.png",
                #allow_stretch=True, keep_ratio=False,
                #size_hint =(.1, .1),
                #pos_hint ={"x":0.3, "y":0.1}
                ))

        
def switch_demo(argument):
    path = "images/icons/"
    switcher = {
        "Clear": "01.png",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return path+switcher[argument]
        
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

test = getWeatherReducedByCityId()
print(test)