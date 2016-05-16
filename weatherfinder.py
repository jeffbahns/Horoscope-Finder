# weatherfind

import requests, re, os
from bs4 import BeautifulSoup
from json import load
s='1868967083e9'
s2='ca9a'
url = "http://api.wunderground.com/api/{}/conditions/q/{}/{}.json"
apiKey = "xxxxxxxxxxxx"

def weatherfind(city, state):
	city = re.sub("[^a-zA-Z]", "_", city)
	r = requests.get(url.format(apiKey, state,city))
	data = r.json()
	co = data['current_observation']
    
    # grabs all info from json file and formats it onto screen
	print ("____________________________________________________")
	print (co['local_time_rfc822'])
	print ("Forecast for " + co['display_location']['full'])
	print ("---------------------------------------------")
	print ("Weather : " + co['weather'])
	print ("Current Temperature : " + str(co['temp_f']) + "F")
	print ("Feels like : " + str(co['feelslike_f']) + "F")
	print ("Wind : " + str(co['wind_mph']) + "MPH")
	print ("____________________________________________________|")


os.system('clear')
testcity = input("Enter a city name:\n>>  ")
teststate = input("Enter a state:\n>>  ")
(weatherfind(testcity, teststate))
