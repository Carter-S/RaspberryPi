import RPi.GPIO as GPIO
import time

controlPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(controlPin, GPIO.OUT)

servo = GPIO.PWM(controlPin, 50)
servo.start(0)
try:
    while True:
        servo.ChangeDutyCycle(2)
        time.sleep(1)
        servo.ChangeDutyCycle(7)
        time.sleep(1)
        servo.ChangeDutyCycle(12)
        time.sleep(1)
finally:
    servo.stop()
    GPIO.cleanup()