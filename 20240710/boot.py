# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()


ssid = 'vivo xxxx'
password = 'shxxxxxx'
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)
import time
while station.isconnected() == False:
    time.sleep(0.5)
    pass

print('Connection successful')
print(station.ifconfig())
