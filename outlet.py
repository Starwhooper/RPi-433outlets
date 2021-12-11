#!/usr/bin/python3
# Creator: Thiemo Schuff, thiemo@schuff.eu
# Source: https://github.com/Starwhooper/RPi-outlet433

##### import config.json

import json
import os
import sys

try:
 with open(os.path.split(os.path.abspath(__file__))[0] + '/config.json','r') as file:
  cf = json.loads(file.read())
except:
 sys.exit('exit: The configuration file ' + os.path.split(os.path.abspath(__file__))[0] + '/config.json does not exist or has incorrect content. Please rename the file config.json.example to config.json and change the content as required ')

try:
 code = cf['outlet'][sys.argv[1]][sys.argv[2]]
except:
 exit('invalid')



os.system('/opt/rpi-rf/scripts/rpi-rf_send ' + str(cf['outlet'][sys.argv[1]][sys.argv[2]]) +' -g ' + str(cf['gpio_send']) )
