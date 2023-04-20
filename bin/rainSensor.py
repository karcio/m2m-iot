from time import sleep
from gpiozero import InputDevice

no_rain = InputDevice(7)

while True:
    if not no_rain.is_active:
        print("It's raining - get the washing in!")

    sleep(1)
