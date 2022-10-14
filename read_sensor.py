#!/usr/bin/python3
import sys
import Adafruit_DHT
from signal import signal, SIGTERM, SIGHUP, pause

def safe_exit():
    pass

while True:
    #signal(SIGTERM, safe_exit)
    #signal(SIGHUP, safe_exit)
    humidity, temperature = Adafruit_DHT.read_retry(11, 4) # (sensor, gpio_pin) 
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
