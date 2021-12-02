#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

#Initialisation
LED=27
BUTTON=17
IS_PRESSED = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        STATUS_BUTTON = GPIO.input(BUTTON)

        if STATUS_BUTTON == False:
            IS_PRESSED = not IS_PRESSED
       
        if IS_PRESSED == True :
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
        
            
        else :
            GPIO.output(LED, GPIO.LOW)
            time.sleep(1)
        
            
        #time.sleep(1)    
    
except KeyboardInterrupt:
    GPIO.cleanup()
