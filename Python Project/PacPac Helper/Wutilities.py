
#VERSION 2014-9-7-12:05PM
Citycode_dictionary = {"北京":101010100, "杭州":101210101, "上海":101020100, "深圳":101280601}

def returner():
	print("\
		")
#weather object 
class Weather(object):
	def __init__(self, message):
		message = message.split()
		self.city_name = message[0]
		self.city_temperature = message[1]
		self.city_winddirection = message[2]
		self.city_windlevel = message[3]
		self.city_reletivehumidity = message[4]
		self.city_timePublishing = message[5]

def message_decode(message):
	return Weather(message)

def get_citycode(cityname):
	try:
		return Citycode_dictionary[cityname]
	except:
		print('City your going to is beyond my imagination, cannot help ya, srry!')

def export_weatherInfo():
	weatherInfo = open('WeatherInfo.txt', 'w')
	weatherInfo.close


# def import_user_settings():
# 	user_settings = open('US.txt')
# 	try:
