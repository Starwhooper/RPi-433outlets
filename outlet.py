#!/usr/bin/python3
# Creator: Thiemo Schuff, thiemo@schuff.eu
# Source: https://github.com/Starwhooper/RPi-outlet433

import json
import os
import sys
from rpi_rf import RFDevice

##### import config.json
try:
 with open(os.path.split(os.path.abspath(__file__))[0] + '/config.json','r') as file:
  cf = json.loads(file.read())
except:
 sys.exit('exit: The configuration file ' + os.path.split(os.path.abspath(__file__))[0] + '/config.json does not exist or has incorrect content. Please rename the file config.json.example to config.json and change the content as required ')

#try:
# check = cf['outlets'][sys.argv[1]]
# except:
# exit('invalid command. Please do like:\n   ./outlet A on\nThe code for each outlet have to set in config.json')

rfdevice = RFDevice(cf['gpio_send'])
rfdevice.enable_tx()
rfdevice.tx_repeat = cf['radio']['repeats']
if sys.argv[2] == 'on': code = cf['outlets'][sys.argv[1]]['code_on']
if sys.argv[2] == 'off': code = cf['outlets'][sys.argv[1]]['code_off']
rfdevice.tx_code(code, cf['radio']['protocol'], cf['radio']['pulselength'], cf['radio']['codelength'])
rfdevice.cleanup()
