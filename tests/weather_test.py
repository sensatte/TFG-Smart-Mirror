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
    id1 = '819838'
    id2 = '3523670'

    result1 = getWeatherReducedByCityId(city_id = id1)
    result2 = getWeatherReducedByCityId(city_id = id2)

    temperature1 = result1['temp']
    weather1 = result1['weather']

    temperature2 = result2['temp']
    weather2 = result2['weather']

    assert temperature1 != temperature2 or weather1 != weather2
