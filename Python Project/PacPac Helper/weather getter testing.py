import urllib  
import sys  
import re  
import pinyin  
city_info=urllib.urlopen( 'http://pv.sohu.com/cityjson').read()  
print city_info   #看输出结构  
addr=city_info.split('=')[1].split(',')[2].split('"')[3] #取出地址信息  
  
open('nj.txt','w').write(addr)  
pinyin = pinyin.Pinyin(file_path='./nj.txt')  
pinyin.label_chinese()   #将地址转换成拼音，写入文件  
  
f=open('nj.txt').read()  
print f     #看输出地址拼音结构  
provice=f.split('sheng',1)[0].replace(' ','')    #获取省份  
city=f.split('shi')[0].split('sheng')[1].strip().replace(' ','') #获取城市  
url='http://qq.ip138.com/weather/%s/%s.htm'%(provice,city)  
#分析url可知某省某市的天气url即为上面格式  
wea_info=urllib.urlopen(url).read()  
tianqi_pattern='alt="(.+?)"'  
tianqi=re.findall(tianqi_pattern, wea_info)  #获取天气信息  
  
wendu_pattern='<td>([-]?\d{1,2}.+)</td>'  
wendu=re.findall(wendu_pattern, wea_info)  #获取温度信息  
  
wind_pattern='<td>(\W+\d{1,2}.+)</td>'  
wind=re.findall(wind_pattern, wea_info)   #获取风向信息  
  
print '位置：',addr  
print '天气：',tianqi[0]  #当天天气，明天天气即为tianqi[1],最多获取6天天气  
print '温度：',wendu[0]   #当天温度  
print '风向：',wind[0]    #当天风向  