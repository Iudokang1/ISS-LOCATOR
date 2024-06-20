from flask import Flask, render_template, request
from geopy import distance
import requests
from get_iss import iss_loc
from get_weather import get_weather
from get_address import address
from get_distance import dist
from get_country import country


#find the location of iss
#weather information 
#reverse geolocation (we lat and lon and the address or country name)
#distance between you and ISS
#rest countries api
#The Flag of the country

app = Flask('app')
@app.route('/')
   
def index():
  data =iss_loc()
  lat,lon=data[0],data[1]
  flag=""

  #Weather
  weather = get_weather(lat,lon)
    #print(weather)
  temp_c = round(weather["main"]["temp"]-273.15,2)
  description = weather["weather"][0]["description"]
  print(str(temp_c)+" C " + description)

    # address reverse gelocation
  add = address(lat,lon)
    # Print the Country Code
    #print("Country Code is : ",add["countryCode"])

    #distance from ISS
  distance = dist(lat,lon,43.7360765,-79.4856325)
  print(f"You are {distance} km from the ISS")


  if (add["countryCode"] == ""):
    #print("ISS is over water")
    countryname = 'ISS IS OVER WATER BODY'
    #flag = 'ISS IS OVER WATER BODY'
  
  else:
    location = add["countryCode"]
    countryname = "The ISS is currently in "  + add["countryName"]
    print("Country Code is : ", add["countryCode"])
    flag = country(location)[0]["flags"]["png"]
    #print(flag)
  
  return render_template(
    "index.html", lon=lon, lat=lat, distance=distance, temp_c=temp_c, flag=flag, countryname=countryname, iss_loc=iss_loc) 
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)


