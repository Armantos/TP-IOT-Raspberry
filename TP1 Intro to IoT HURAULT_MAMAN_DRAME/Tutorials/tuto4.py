import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
turn_off_GPIO_time = 0.1
value = 0 # this variable will be used to store the ldr value
ldr = 4
def ldr_read (ldr):
    count = 0
     #Output on the pin to turn it off before reading it again
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(turn_off_GPIO_time)
     #Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)
     #Count until the pin goes high
    while (GPIO.input(ldr) == 0):
        count += 1
    return count
try:
    while True:
        print("LDR Value:")
        value = ldr_read(ldr)
        print(value)
        if ( value <= 4000 ):
            print("Lights are ON")
        else:
            print("Lights are OFF")
except KeyboardInterrupt:
 GPIO.cleanup()