import os
import pyowm

api_key = os.environ['WEATHER_API_KEY']
owm = pyowm.OWM(api_key)

def get_data(city, region):
    location = "{}{}".format(city, region)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    response = u'You requested the weather in ' + city +" "+region + ':\n'
    response += u'Temperature : ' + str(w.get_temperature('celsius')['temp']) + u"\u00b0C \n"
    response += u'Status : ' + w.get_detailed_status() + u" \n"
    response += u'Clouds: ' + str(w.get_clouds()) + u"% \n"
    response += u'Wind speed: ' + str(w.get_wind()['speed']) + u" km/h \n"
    response += u'Air pressure: ' + str(w.get_pressure()['press']) + u" hPa\n"
    return response

print(get_data('Brampton,', 'CA'))



