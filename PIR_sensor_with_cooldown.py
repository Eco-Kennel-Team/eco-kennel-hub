#motion detector with cooldown
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 11
GPIO.setup(PIR_PIN, GPIO.IN)

motion_cooldown = 60 # how long before the motion sensor can detect motion again
motionFlag = False

while True:
    if PIR_PIN == 1:
        motiondetected = True
        #send motiondetectedflag to tensorflow server
    elif PIR_PIN == 0:
        motiondetected = False

    if(motionDetected):
        #send motiondetected to server
        motionDetected = False
        start = time.time()
    if motionDetected == False:
        if time.time() > start + motion_cooldown:
            motionDetected = True
