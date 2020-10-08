import serial
from CallPHP import*
from cameraFunction import*
from GetPHP import*
import urllib.request as urllib2
import time

ser = serial.Serial("/dev/ttyACM0", 115200)
motionDetected = True
PERIOD_OF_TIME = 60

while 1 :
    rawDataLine = ser.readline() #Read data from Arduino
    
    dataLine = str(rawDataLine.rstrip(), 'utf-8')#removes special character
    
    print("Dataline at line 8:",dataLine)
    
    # parse the line to get flag
    #dataFlag = dataLine[0]
    dataFlag = dataLine[0]
    
    print("This is dataFlag: ", dataFlag)
        
    # if statements to save to specific variable
    if dataFlag == "T":
        
        #save the rest as new temp variable (string)
        newTemperature = dataLine.replace("T","")
        
        print("Temperature is", newTemperature)
        
        #check if temperature is outside of safe parameters send special alert
        highTemp = str(fromPHP(1).rstrip(),'utf-8')
        lowTemp = str(fromPHP(0).rstrip(),'utf-8')
        
        if float(newTemperature) >= float(highTemp) or float(newTemperature) <= float(lowTemp):
            # set alert flag to send a push notification
            
            tempAlert = True
            #PUSH NOTIFICATION
        else:
            tempAlert = False
            
        #temp update
        toPHP(newTemperature, "NULL", "NULL")
            
        
    elif dataFlag == "M": # motion detect should only be one - would also like it get some kind of timestamp from Arduino
        
        motionDetect = dataLine.replace("M","")
        
        print("Motion is detected")
        
        #call the camera to begin recording and using Tensor flow
        if(motionDetected):
            startTheCamera()
            motionDetected = False
            start = time.time()
        
        #break
        
        #one minute cool down on motion detection afterwards
    elif dataFlag == "A":
        
        audioDetect = dataLine.replace("A","")
        print("Audio is detected")
        
        if audioDetect == "CONST":  #there has been a lot of loud noise over a period of time
            print("Theres a lot of noise")
            
            urllib2.urlopen("https://ecokennel.000webhostapp.com/NotifyConstantSound.php")
            
        elif audioDetect == "LOUD":
            print("There's been an extremely loud noise")
            
            urllib2.urlopen("https://ecokennel.000webhostapp.com/NotifyLoudSound.php")
   
    else:
        print("Nothing happened, this is the dataLine: ", dataLine )
        
    if motionDetected == False:
        if time.time() > start + PERIOD_OF_TIME:
            motionDetected = True
        
        
    
    
