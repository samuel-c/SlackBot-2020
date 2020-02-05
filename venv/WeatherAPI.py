import os
import pyowm
from JsonParse import get_code_from_country

api_key = os.environ['WEATHER_API_KEY']
owm = pyowm.OWM(api_key)

def get_data(city, region):
    region = region[1:]
    region = get_code_from_country(region) if len(region) > 2 else region
    location = "{},{}".format(city, region)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    response = (u'You requested the weather in ' + city + ", " +region.upper() +":\n"
                u'Temperature : ' + str(w.get_temperature('celsius')['temp']) + u"\u00b0C \n"
                u'Status : ' + w.get_detailed_status() + u" \n"
                u'Clouds: ' + str(w.get_clouds()) + u"% \n"
                u'Wind speed: ' + str(w.get_wind()['speed']) + u" km/h \n"
                u'Air pressure: ' + str(w.get_pressure()['press']) + u" hPa\n")
    return response




