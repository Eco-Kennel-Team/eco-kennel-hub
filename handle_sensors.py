#This is essentially the main file
#It should get data from temp sensor, motion sensor, and handle the campera
#replaces "readFromArduino"

from temp_sensor.py import*
import RPi.GPIO as GPIO
import time



while(1)
    # Temp sensor
    # Should update at regular intervals
    # Once the temperature is updated, it should update to the database
    # Should there be a warning flag if it is outside of safe temperatures?
    # How can the user set the parameters from the app
    # Should the user perferred temps be stored on the database?

    if() #some sort of check to see if enough time has passed
        currentTemperature = temperature.get_temperature()







# Motion sensor
#if motion sensor is high for x amount of time, send say "Motion detected, begin recording"
