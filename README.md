RPi-backup
==========

* Creator: Thiemo Schuff, thiemo@schuff.eu
* Source: https://github.com/Starwhooper/RPi-outlet433
* License: CC-BY-SA-4.0

Prepare your System
-------------------
```bash
sudo apt-get install python3-pip
pip3 install rpi-rf
cd /opt
sudo git clone https://github.com/Starwhooper/RPi-outlet433
```

First configurtion
------------------
```bash
copy /opt/RPi-outlet433/config.json.example /opt/RPi-outlet433/config.json
sudo nano /opt/RPi-outlet433/config.json
```
Change in config.json:
* set "[gpio_send]" to the GPIO that you use to send
* set "[outlets][*][name]" to Name that you want to identity the outlet
* set "[outlets][*][code_on]" to code to switch on the outlet
* set "[outlets][*][code_off]" to code to switch off the outlet
* set "[outlets][*][operations][*][type] to time or calculate
  * case type = "time"
    * set "[outlets][][operations][][on] to time in 24h format. as example 0600 für 6am, 2205 for 5 minutes after 10pm.
  * case type = "calculate"
    * set "[outlets][][operations][][on] to command and offset in mins. As example "sunset;+45" means 45minutes after local sunset. "sunrise;-120" means 2hours before sunrise.


Start direct
-----
```bash
/opt/RPi-out433/outlet.py A on
```

Start service
-----
```bash
/opt/RPi-out433/service.py
```
