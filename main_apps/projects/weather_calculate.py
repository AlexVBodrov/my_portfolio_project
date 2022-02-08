import json
import os
from pyowm import OWM
from main_apps.settings import BASE_DIR
# change languages = ru
from pyowm.utils.config import get_default_config


config_dict = get_default_config()
config_dict['language'] = 'ru'


with open(
    os.path.join(BASE_DIR, "tmp", "secrets", "api_wh.json"), "r"
) as secrets_api:
    api_wh = json.load(secrets_api)


owm = OWM(api_wh["api_key"])
mgr = owm.weather_manager()


def get_weather_at_city(city):
    """Search for current weather in city and get details"""
    city = city
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    wind = w.wind()['speed']
    status = w.detailed_status
    return f"В городе {city} температура {temperature} °C и {status},скорость ветра {wind}"


if __name__ == '__main__':
    place = input("Укажите город: ")
    print(get_weather_at_city(place))
