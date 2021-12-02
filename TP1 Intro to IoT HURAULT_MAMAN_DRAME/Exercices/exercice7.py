#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

LED1=27
LED2=27
LED3=27

BUTTON1=17
BUTTON2=17
BUTTON3=17


# setup the enumeration based on GPIO references 1
GPIO.setmode(GPIO.BCM)
# setup the port 17 as output, in this PIN the energy will go out
   
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

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
