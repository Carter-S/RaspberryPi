import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ledPin = 12
pirPin = 21

GPIO.setup(pirPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)

def LIGHTS(pirPin):
	print("Motion detected!")
	print("Lights on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(2)
	print("Light off")
	GPIO.output(ledPin, GPIO.LOW)
try:
	GPIO.add_event_detect(pirPin, GPIO.RISING, callback=LIGHTS)
	while True:
		time.sleep(1)
except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()
