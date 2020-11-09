from threading import Timer, Event

#motion sensor set up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)


def check_the_temp():
    if not done.is_set():
        #get the temp
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        device_file = device_folder + '/w1_slave'

        def read_temp_raw():
            f = open(device_file, 'r')
            lines = f.readlines()
            f.close()
            return lines

        def read_temp():
            lines = read_temp_raw()
            while lines[0].strip()[-3:] != 'YES': #error checking
                time.sleep(0.2)
                lines = read_temp_raw()
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0
                return temp_c

        while True:
            print(read_temp())  #send temperature update to server
            time.sleep(1)

        Timer(5.0, check_the_temp).start()

done = Event()
Timer(5.0, every_so_often).start()

#this is where all other code goes

#MOTION sensor code ------------------------------------------------------
motionFlag = False
motionCount = 0

while True:
    if i == 0:
        #no MOTION
    elif i == 1:
        #motion detected
        motionCount ++


done.set()
