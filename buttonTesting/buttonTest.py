#Imports
import RPi.GPIO as GPIO
from time import sleep

#Declaring pin layout
GPIO.setmode(GPIO.BCM)

#Declaring pin numbers
buttonPin = 26
ledPin = 21
sleepTime = 0.1

#Declaring input pins and output pins
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#If button is pressed led will turn on else it will turn off
try:
    while True:
        if not GPIO.input(buttonPin):
            GPIO.output(ledPin, True)
            sleep(sleepTime)
        else:
            GPIO.output(ledPin, False)
finally:
    #Cleans up gpio pins when script is ended
    GPIO.cleanup()