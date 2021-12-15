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
Check GPIO and Codes in config.json

```bash
copy /opt/RPi-outlet433/config.json.example /opt/RPi-outlet433/config.json
sudo nano /opt/RPi-outlet433/config.json
```

Start
-----
```bash
/opt/RPi-out433/outlet.py A on
```
