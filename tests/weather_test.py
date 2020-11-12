import pytest
import logging
from customWidgets.WeatherWidget import getWeatherReducedByCityId

def test_get_result ():

    result = getWeatherReducedByCityId()

    temperature = result['temp']
    weather = result['weather']

    assert isinstance(temperature, float)
    assert isinstance(weather, str)

def test_get_different_results ():
    id1 = ''
    id2 = ''

    result1 = getWeatherReducedByCityId(id = id1)
    result2 = getWeatherReducedByCityId(id = id2)

    temperature1 = result1['temp']
    weather1 = result1['weather']

    temperature2 = result2['temp']
    weather2 = result2['weather']

    assert temperature1 != temperature2 and weather1 != weather2
