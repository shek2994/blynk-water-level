"""
Blynk is a platform with iOS and Android apps to control
Arduino, Raspberry Pi and the likes over the Internet.
You can easily build graphic interfaces for all your
projects by simply dragging and dropping widgets.

  Downloads, docs, tutorials: http://www.blynk.cc
  Sketch generator:           http://examples.blynk.cc
  Blynk community:            http://community.blynk.cc
  Social networks:            http://www.fb.com/blynkapp
                              http://twitter.com/blynk_app

This example shows how to initialize your ESP8266/ESP32 board
and connect it to Blynk.

Don't forget to change WIFI_SSID, WIFI_PASS and BLYNK_AUTH ;)
"""

'''Micropython import modules'''
from machine import Pin, ADC, PWM, Timer
import machine
import time

'''blynk cloud connected import modules'''
import BlynkLib
import network
from BlynkTimer import BlynkTimer

'''app utils modules'''
import random

'''for HW sensor v/s random'''
_SIMUL = True

WIFI_SSID = 'vivo xxxx'
WIFI_PASS = 'shekxxxx'

BLYNK_AUTH="ntDBx7-dkNt7gT3A6nTx4xoKBhwEw71F"

wifi = network.WLAN(network.STA_IF)
if not wifi.isconnected():
    print("Connecting to WiFi...")
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)
    while not wifi.isconnected():
        pass

print('IP:', wifi.ifconfig()[0])

blynk = BlynkLib.Blynk(BLYNK_AUTH, insecure=True)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')






'''data push section'''
timer = BlynkTimer()

def send_temp_data():
    if _SIMUL :
        val = random.uniform(1.5, 10.9)

    print(val)
    blynk.virtual_write(0, val)

# Add Timers
timer.set_timeout(2, send_temp_data)
timer.set_interval(1.2, send_temp_data)

def runLoop():
    while True:
        blynk.run()
        timer.run()
        machine.idle()
# Run blynk in the main thread
runLoop()

# You can also run blynk in a separate thread (ESP32 only)
#import _thread
#_thread.stack_size(5*1024)
#_thread.start_new_thread(runLoop, ())


 
