import RPi.GPIO as GPIO
import time

sleepTime = 1
blueLed = 21
greenLed = 20
redLed = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(blueLed, GPIO.OUT)
GPIO.setup(greenLed, GPIO.OUT)
GPIO.setup(redLed, GPIO.OUT)

try:
	while True:
		GPIO.output(blueLed, True)
		time.sleep(sleepTime)
		GPIO.output(blueLed, False)
		GPIO.output(greenLed, True)
		time.sleep(sleepTime)
		GPIO.output(greenLed, False)
		GPIO.output(redLed, True)
		time.sleep(sleepTime)
		GPIO.output(redLed, False)

finally:
	GPIO.output(blueLed, False)
	GPIO.output(greenLed, False)
	GPIO.output(redLed, False)
	print("keyboard interrupt detected")
