#!/usr/bin/python2.7

import sys,requests,os,json,datetime

APPID = "25f70abd3ad9ca892070b7d4c647bc42"

def data_collect(location):
	url = "http://api.openweathermap.org/data/2.5/forecast/daily?q="+location+"&APPID="+APPID+"&units=metric&cnt=5"

	forecast = requests.get(url)
	forecast.raise_for_status()

	weatherData = json.loads(forecast.text)
	
	print '{0:24}    {1:5}   {2:5}\t{3}'.format(weatherData["city"]["name"]+","+weatherData["city"]["country"],"Max","Min","Description")
	for x in range(5):
		print '{0:24} -> {1:2.2f}   {2:2.2f}\t{3}'.format(\
			datetime.datetime.fromtimestamp(weatherData['list'][x]['dt']).ctime(),\
			weatherData['list'][x]['temp']['max'],\
			weatherData['list'][x]['temp']['min'],\
			weatherData['list'][x]['weather'][0]['description'])

if __name__=="__main__":
	if not len(sys.argv) > 1:
		print "Usage - python weather.py <city-name>"
		sys.exit()
	else:
		location = ' '.join(sys.argv[1:])
	data_collect(location)