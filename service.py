#!/usr/bin/python3
# Creator: Thiemo Schuff, thiemo@schuff.eu
# Source: https://github.com/Starwhooper/RPi-433outlets
# <!--get awesomefonts from here: https://fontawesome.com/v5.15/icons/cloud-sun?style=solid //-->

##### import config.json

import json
import os
import sys
import urllib
import time
from datetime import datetime

codefolder = os.path.split(os.path.abspath(__file__))[0]

def hourmin (timestamp,extramin=0):
 timestamp = timestamp + (extramin * 60)
 hm = int(datetime.utcfromtimestamp(timestamp).strftime('%H%M'))
 return(hm)

def return_date(): return(datetime.date.today().strftime('%d. %b. \'%y'))
def return_time(): return(time.strftime('%H:%M', time.localtime()))

try:
 with open(codefolder + '/config.json','r') as file:
  cf = json.loads(file.read())
except:
 sys.exit('exit: The configuration file ' + codefolder + '/config.json does not exist or has incorrect content. Please rename the file config.json.example to config.json and change the content as required ')



ow_remotefile = "http://api.openweathermap.org/data/2.5/weather?" + cf["openweatherlocation"] + "&appid=" + cf["openweatherapikey"] + "&lang=de&units=metric"
ow_localfile = codefolder + '/cache/openweathermap.json'

try: owage = os.path.getmtime(ow_localfile)
except: owage = 0

if owage + 60*60*24 < time.time():
 from urllib.request import urlopen
 urllib.request.urlretrieve(ow_remotefile, ow_localfile)
with open(ow_localfile,'r') as file:
 ow = json.loads(file.read())

sunrise = int(ow['sys']['sunrise'])
sunrise_hm = int(hourmin(sunrise))
sunset = int(ow['sys']['sunset'])
sunset_hm = int(hourmin(sunset))
now = int(datetime.now().timestamp())
now_hm = int(hourmin(datetime.now().timestamp()))

try: htmlfile = open(cf["htmloutput"]["file"],'w')
except: print('file ' + cf["htmloutput"]["file"] + ' not aviable or permission missed')


htmlstring = '<!DOCTYPE HTML><html>\n'
htmlstring += '<head>\n'
htmlstring += '<title>outlets</title>\n'
htmlstring += '<meta charset="utf-8"/>\n'
htmlstring += '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
htmlstring += '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">\n'
htmlstring += '<style>\n'

try: htmlstring += open(parent_dir + '/style.css','r').read()
except: htmlstring += '<!-- NO STYLE.CSS FOUND //-->\n'

htmlstring += '</style>\n'

htmlstring += '</head>\n'
htmlstring += '<body>\n'
htmlstring += '<h1><i class="fas fa-power-off" style="color:black"></i> Outlets</h1>\n'

htmlstring += '<p>sunrise: <i class="far fa-sun"></i>' + str(sunrise_hm) + ' ' + str(sunrise) + '</p>';
htmlstring += '<p>sunset: <i class="far fa-moon"></i>' + str(sunset_hm) + ' ' + str(sunset) + '</p>';
htmlstring += '<p>now: <i class="far fa-clock"></i>' + str(now_hm) + ' ' + str(now) + '</p>';

for outlet in cf['outlets']:
 switch = 'off'
 for operation in cf['outlets'][outlet]['operations']:
  
  operation_type = cf['outlets'][outlet]['operations'][operation]['type']
  
  if operation_type == 'time':
   operation_on = cf['outlets'][outlet]['operations'][operation]['on']
   operation_off = cf['outlets'][outlet]['operations'][operation]['off']
  
  if operation_type == 'calculate':
   moment_on = cf['outlets'][outlet]['operations'][operation]['on'].split(';')
   if moment_on[0] == 'sunset': operation_on = hourmin(sunset,int(moment_on[1]))
   if moment_on[0] == 'sunrise': operation_on = hourmin(sunrise,int(moment_on[1]))
   moment_off = cf['outlets'][outlet]['operations'][operation]['off'].split(';')
   if moment_off[0] == 'sunset': operation_off = hourmin(sunset,int(moment_off[1]))
   if moment_off[0] == 'sunrise': operation_off = hourmin(sunrise,int(moment_off[1]))

  print(str(operation_on) + ' - ' + str(operation_off) + ' ' + operation_type)
  htmlstring += '<p>' + str(operation_on) + ' - ' + str(operation_off) + ' ' + operation_type + '</p>'
  if now_hm >= operation_on and now_hm < operation_off: switch = 'on'
 command = codefolder + '/outlet.py ' + outlet + ' ' + switch
 os.system(command)
 print(command + ': ' + cf['outlets'][outlet]['name'] + ' ' + switch)
 htmlstring += '<p>' + cf['outlets'][outlet]['name'] + ' ' + switch + '</p>'
 htmlstring += '</body></html>'

htmlfile.write(htmlstring)
htmlfile.close
