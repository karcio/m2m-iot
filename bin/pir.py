import RPi.GPIO as GPIO
import time

SENSOR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


def checkMovement(channel):
    print('There was a movement!')


try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=checkMovement)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print('Finish...')

GPIO.cleanup()
