#! /usr/bin/env python
# enable functions and methods to manage the Pi
import RPi.GPIO as GPIO
# enable use of functions of time
import time
# GPIO used to connect an anode leg LED
# GPIO 17 is equal PIN 11 follow the physical enumeration
LED=17

# setup the enumeration based on GPIO references 1
GPIO.setmode(GPIO.BCM)
# setup the port 17 as output, in this PIN the energy will go out
   
GPIO.setup(LED, GPIO.OUT)
# setup to have not energy by the port 17


GPIO.output(LED, GPIO.HIGH)
#The LED lights up only when the button is pressed 
    
