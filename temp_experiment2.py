    from threading import Timer, Event

    def every_so_often():
        if not done.is_set():
            print('Do the thing you want to every so often')

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
                print(read_temp())
                time.sleep(1)

            Timer(5.0, every_so_often).start()

    done = Event()
    Timer(5.0, every_so_often).start()

    for count in range(100_000_000):
        prod = count * count
        if count % 10_000_000 == 0:
            print('multiplied up to', count)

    done.set()
