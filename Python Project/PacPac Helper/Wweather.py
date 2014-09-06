import os, io, sys, re, time, base64, json
import webbrowser, urllib.request
import Wutilities

os.system('clear')

print('--------------Weather Conselling---------------')
print('   MADE BY 5000 DOGS DATA FROM WEATHER CHINA')
print('-----------------VERSION 0.5.4-----------------')
# city codes
Citycode_dictionary = {"北京":101010100, "杭州":101210101, "上海":101020100, "深圳":101280601}

#default city
Hangzhou_citycode = 101210101

#User input the decination city
Decination = input("please tell me where you'd like to go to. : ")
#Search in the Citycode_dictionary to get the city
if Decination != '':
	Decination = Citycode_dictionary[Decination]
else:
	Decination = Hangzhou_citycode
# Testing use ONLY
# Decination = Hangzhou_citycode

# The weather info getting model
def getCityWeather_RealTime(cityID):
    url = "http://www.weather.com.cn/data/sk/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInfomation = stdout.read().decode('utf-8')
 
        jsonDatas = json.loads(weatherInfomation)
 
        city        = jsonDatas["weatherinfo"]["city"]
        temp        = jsonDatas["weatherinfo"]["temp"]
        wd          = jsonDatas["weatherinfo"]["WD"]        #Wind direction
        wl          = jsonDatas["weatherinfo"]["WS"]        #Wind level
        rh          = jsonDatas["weatherinfo"]["SD"]        #Reletive humidity
        tm          = jsonDatas["weatherinfo"]["time"]	 	#Time of Publishing this info
 
        content = city + " " + temp + " " + wd + ' ' + wl + " " + rh + " " + tm
        twitter = {'image': "", 'message': content}
 
    except (SyntaxError) as err:
        print(">>>>>> SyntaxError: " + err.args)
    except:
        print("No internet Connection! Please Connect me to my friends!")
    else:
        return twitter
    finally:
    	None

Wutilities.returner()

# the output model
def main():
    try:
        weatherGotten = Wutilities.message_decode(getCityWeather_RealTime(Decination)['message'])
        print('city name: ' + weatherGotten.city_name)
        print('city temperature(Celcius): '+weatherGotten.city_temperature)
        print('city wind direction: '+weatherGotten.city_winddirection)
        print('city wind level: '+ weatherGotten.city_windlevel)
        print('city reletive humidity: '+weatherGotten.city_reletivehumidity)
        print('data published time: '+weatherGotten.city_timePublishing)
    except TypeError:
	    print("Oops, Something Wrong!")

if __name__ == '__main__':
	main()




