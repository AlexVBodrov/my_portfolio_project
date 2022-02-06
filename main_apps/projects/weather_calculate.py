import pyowm
from pyowm import OWM
# change languages = ru
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('b3e3f2a737d2967e2851a9892592d8c7')
mgr = owm.weather_manager()


def get_weather_at_city(city):
    """Search for current weather in city and get details"""
    city = city
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    status = w.detailed_status
    return f"В городе {city} температура = {temperature} градусов по Цельсию и статус {status}"


if __name__ == '__main__':
    place = input("Укажите город: ")
    print(get_weather_at_city(place))

