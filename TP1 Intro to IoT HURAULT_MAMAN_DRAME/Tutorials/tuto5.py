#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import random
RED=17
GREEN=187
BLUE=27
LEGS = (RED,GREEN, BLUE)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)
try:
    while True:
        x = int(random.random()*2)
        GPIO.output(LEGS[x], GPIO.HIGH)
        time.sleep(0.05)
        x = int(random.random()*2)
        GPIO.output(LEGS[x], GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    
