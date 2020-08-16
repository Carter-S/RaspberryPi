import os
import glob
import time
import RPi.GPIO as GPIO
import threading

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buttonUp = 16
buttonDown = 20
fanPin = 19
dTemp = 24

GPIO.setup(fanPin, GPIO.OUT)
GPIO.setup(buttonUp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonDown, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(fanPin,True)
 
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
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
def tempMeth():
	while True:
        	if read_temp() > dTemp:
            		GPIO.output(fanPin,False)
        	else:
            		GPIO.output(fanPin,True)
def upMeth():
	global dTemp
	while True:
        	if(GPIO.input(buttonUp) == 0):
            		dTemp += 1
            		print(dTemp)
			time.sleep(0.5)
def downMeth():
	global dTemp
	while True:
        	if(GPIO.input(buttonDown) == 0):
            		dTemp-= 1
            		print(dTemp)
			time.sleep(0.5)

t1 = threading.Thread(target=tempMeth)
t2 = threading.Thread(target=upMeth)
t3 = threading.Thread(target=downMeth)
t1.start()
t2.start()
t3.start()
