#this code utilizes interrupts rather than constantly polling the pins
#should have better performance, but unsure how it will behave with the temp sensor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 11
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
               #motion is detected
               #do the thing
time.sleep(2)

try:
               GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
               while 1:
                              time.sleep(100)
except KeyboardInterrupt:
               GPIO.cleanup()
