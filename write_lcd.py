#!/usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
lcd = LCD()

heart = b'\x00\x0a\x1f\x1f\x0e\x04\x00\x00'


def safe_exit(signum, frame):
    exit(1)
try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("Putu <3".format(heart), 1)
    lcd.text("Tintin! :-) ", 2)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
