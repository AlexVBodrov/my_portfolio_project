import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('b3e3f2a737d2967e2851a9892592d8c7')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
city = 'Москва'
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
status = w.detailed_status
print(f"В городе {city}  температура = {temperature} по Цельсию и статус {status}")

