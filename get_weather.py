import urllib.request
import json



def get_weather(lat,lon):
  #"Get the weather using lat and long from get_iss"
  key='feb31a2038bc60d5e9be408a03af389b'
  url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
