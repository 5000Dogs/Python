import WweatherUE, Wutilities

print('--------------  PACPAC  HELPER  ---------------')
print('   MADE BY 5000 DOGS DATA FROM WEATHER CHINA')
print('-----------------VERSION 0.1.2-----------------')

Destination = input("where's your Destination sir? ")

while True:
	yes_no = input("the place your going is {}, is it correct? ".format(Destination))
	if yes_no == 'yes' or yes_no == 'Y':
		break
	else:
		Destination = input("where's your destination then, sir?")
		Wutilities.returner()


print("the waether there is in this condition right at this moment!")

Destination = Wutilities.get_citycode(Destination)

try:
	Wutilities.returner()
	weatherGotten = Wutilities.message_decode(WweatherUE.getCityWeather_RealTime(Destination))
	print('city name: ' + weatherGotten.city_name)
	print('city temperature(Celcius): '+weatherGotten.city_temperature)
	print('city wind direction: '+weatherGotten.city_winddirection)
	print('city wind level: '+ weatherGotten.city_windlevel)
	print('city reletive humidity: '+weatherGotten.city_reletivehumidity)
	print('data published time: '+weatherGotten.city_timePublishing)
except:
	None

Wutilities.returner()

print('Hmmm let me think for a sec.....')

Wutilities.export_weatherInfo()


