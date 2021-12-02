#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

FRESH=1
BUTTON=17
LED=27
IS_PUSHED=False
IS_LIGHT_ON=False

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)

try:
    while True:
        button_state=GPIO.input(17)
        if button_state == True:
            print("Button not pressed")
            #IS_PUSHED = False
            #time.sleep(FRESH)
        else:
            print("Button pressed")
            time.sleep(FRESH)
            #If the light is off, we turn it on
            if IS_LIGHT_ON == True :
                GPIO.output(LED, GPIO.LOW)
                IS_LIGHT_ON == False
                time.sleep(FRESH)
            #If the light is on, we turn it off
            else:
                GPIO.output(LED, GPIO.HIGH)
                IS_LIGHT_ON == True
                time.sleep(FRESH)
            time.sleep(FRESH)
            
except KeyboardInterrupt:
    GPIO.cleanup()