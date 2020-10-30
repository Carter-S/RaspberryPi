import RPi.GPIO as GPIO
import time

controlPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin, GPIO.OUT)

p = GPIO.PWM(controlPin, 50)
p.start(7.5)

try:
    while True:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
finally:
    p.stop()
    GPIO.cleanup()