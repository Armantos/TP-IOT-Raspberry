#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

LED1=16 #vert
LED2=20 #jaune
LED3=21 #rouge

BUTTON2=17 #jaune
BUTTON3=22 #rouge
BUTTON1=27 #vert


# setup the enumeration based on GPIO references 1
GPIO.setmode(GPIO.BCM)
# setup the port 17 as output, in this PIN the energy will go out
   
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

GPIO.setup(BUTTON1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BOOL1 = False
BOOL2 = False
BOOL3 = False

try:
# infinite loop
    while True:
              
        STATUS_BUTTON1 = GPIO.input(BUTTON1)
        STATUS_BUTTON2 = GPIO.input(BUTTON2)
        STATUS_BUTTON3 = GPIO.input(BUTTON3)
        
        
        
        if STATUS_BUTTON1 == False :
            BOOL1 = not BOOL1
            
            # Active the transmission of energy by port 17
            
        time.sleep(0.15)
        if BOOL1 == True :
            GPIO.output(LED1, True)
             
        else :
       
            GPIO.output(LED1, False)
        
#####################################################
            
        if STATUS_BUTTON2 == False :
            BOOL2 = not BOOL2
            
            # Active the transmission of energy by port 17
            
        time.sleep(0.15)
        if BOOL2 == True :
            GPIO.output(LED2, True)
             
        else :
       
            GPIO.output(LED2, False)
            
            
        
##########################################################
            
            
            
        if STATUS_BUTTON3 == False :
            BOOL3 = not BOOL3
            
            # Active the transmission of energy by port 17
            
        time.sleep(0.15)
        if BOOL3 == True :
            GPIO.output(LED3, True)
             
        else :
       
            GPIO.output(LED3, False)
            
            
            
            ####################################
        
        
            
     
 # exceptions are anything that interrupt the try block.
 # if a CTRL_C be pressed
except KeyboardInterrupt:
# setup the GPIO to default values; finish any transmission of energy
    GPIO.cleanup()
