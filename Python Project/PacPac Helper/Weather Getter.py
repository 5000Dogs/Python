import urllib2,string  
from urllib2 import Request, urlopen  
  
def weather():#获取当地的天气信息  
  url1='http://61.4.185.48:81/g/'  
  try:  
    page1=urllib2.urlopen(url1)  
  except IOError, e:  
    if hasattr(e, 'reason'):  
      print '请检查您的网络连接'  
      page1=None  
    elif hasattr(e, 'code'):  
      print "请检查您的网络连接"  
      page1=None  
  if page1:  
    data1=page1.read()  
    city_code=data1[data1.index('d=')+2:data1.index('d=')+11]  
    url2=''.join(['http://www.weather.com.cn/data/cityinfo/',city_code,'.html'])  
    page2=urllib2.urlopen(url2)  
    data2=page2.read()  
    counter=0  
    for i in range (0,len(data2)):  
      if data2[i]== '"' : 
        counter+=1 
        if counter==5: 
          city1=i 
        elif counter==6: 
          city2=i 
        elif counter==13: 
          l_temp1=i 
        elif counter==14: 
          l_temp2=i 
        elif counter==17: 
          h_temp1=i 
        elif counter==18: 
          h_temp2=i 
        elif counter==21: 
          weather1=i 
        elif counter==22: 
          weather2=i 
    city=data2[city1+1:city2] 
    weather=data2[weather1+1:weather2] 
    h_temp=data2[h_temp1+1:h_temp2] 
    l_temp=data2[l_temp1+1:l_temp2] 
    result='  '.join([city,weather,l_temp+'~'+h_temp]) 
    print result 
def city_weather(city_name):#获取任意城市的天气信息 
  city_code=None 
  city_file=open("city.txt","r")#city.txt中存放着各城市的编码，这个编码详见附录。 
  for i in range (0,2586): 
    city_info=city_file.readline() 
    if city_name in city_info: 
      city_code=city_info[:9] 
      break 
  city_file.close 
  if city_code: 
    url2=''.join(['http://www.weather.com.cn/data/cityinfo/',city_code,'.html']) 
    try: 
      page1=urllib2.urlopen(url2) 
    except IOError, e: 
      if hasattr(e, 'reason'): 
        print '请检查您的网络连接' 
        page1=None 
      elif hasattr(e, 'code'): 
        print "请检查您的网络连接" 
        page1=None 
    if page1: 
      data2=page1.read() 
      counter=0 
      for i in range (0,len(data2)): 
        if data2[i]=='"':  
          counter+=1  
          if counter==5:  
            city1=i  
          elif counter==6:  
            city2=i  
          elif counter==13:  
            l_temp1=i  
          elif counter==14:  
            l_temp2=i  
          elif counter==17:  
            h_temp1=i  
          elif counter==18:  
            h_temp2=i  
          elif counter==21:  
            weather1=i  
          elif counter==22:  
            weather2=i  
      city=data2[city1+1:city2]  
      weather=data2[weather1+1:weather2]  
      h_temp=data2[h_temp1+1:h_temp2]  
      l_temp=data2[l_temp1+1:l_temp2]  
      result='  '.join([city,weather,l_temp+'~'+h_temp])  
      print result  
  else:  
    print '对不起，查不到此城市的天气信息。'  
if __name__=='__main__':  
  info=str(raw_input('我能帮你做点什么？'))  
  if '的天气'in info:  
    info=info[:info.index('的天气')]  
    city_weather(info)  
  elif '天气'in info:  
    weather()