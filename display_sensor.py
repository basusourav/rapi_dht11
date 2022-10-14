#!/usr/bin/python3
import sys
import time
from signal import signal, SIGTERM, SIGHUP, pause
import Adafruit_DHT
import RPi.GPIO as GPIO
from rpi_lcd import LCD

# GPIO pin settings for DIP 3 color rgb led
red=13
blue=6
green=5
RED=None
BLUE=None
GREEN=None
FULL=100
HALF=50
QTR=25
OFF=0


def init():
    # Setup for 3 Color RGB LED
    global RED
    global BLUE
    global GREEN
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    GPIO.setup(blue, GPIO.OUT)
    Freq = 100
    RED = GPIO.PWM(red, Freq)
    GREEN = GPIO.PWM(green, Freq)
    BLUE = GPIO.PWM(blue, Freq)
    BLUE.start(1)
    RED.start(1)
    GREEN.start(1)
    # Setup for LED 16x2 setup
    global lcd
    lcd=LCD()

def set_blue():
    global RED
    global BLUE
    global GREEN
    RED.ChangeDutyCycle(OFF)
    BLUE.ChangeDutyCycle(QTR)
    GREEN.ChangeDutyCycle(OFF)

def set_red():
    global RED
    global BLUE
    global GREEN
    RED.ChangeDutyCycle(QTR)
    BLUE.ChangeDutyCycle(OFF)
    GREEN.ChangeDutyCycle(OFF)

def set_green():
    global RED
    global BLUE
    global GREEN
    RED.ChangeDutyCycle(OFF)
    BLUE.ChangeDutyCycle(OFF)
    GREEN.ChangeDutyCycle(QTR)

def safe_exit(signum, frame):
    exit(1)

if __name__ == "__main__":
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        init()
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(11, 4)
            farenheit = (temperature * 9/5) + 32
            lcd.text("T:{}{}C {}{}F".format(temperature,chr(223),farenheit,chr(223),), 1)
            lcd.text("Humidity: {} %".format(humidity), 2)
            if humidity > 90:
                set_red()
            elif humidity >= 80 and humidity < 90: 
                set_blue()
            else:
                set_green()
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Shutting down GPIO for LED...")
        RED.stop()
        BLUE.stop()
        GREEN.stop()
        GPIO.cleanup()
        print("Shutting Down lcd")
        lcd.clear()
