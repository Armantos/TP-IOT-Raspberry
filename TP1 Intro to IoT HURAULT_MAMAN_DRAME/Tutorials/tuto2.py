#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        button_state=GPIO.input(17)
        if button_state == True:
            print("Button not pressed")
        else:
            print("Button pressed")
except KeyboardInterrupt:
    GPIO.cleanup()
