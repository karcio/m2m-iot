import paho.mqtt.client as mqtt
from datetime import datetime
import time
import configparser
config = configparser.ConfigParser()
config.read('config')

mqttc = mqtt.Client()


mqttc.connect("localhost")
mqttc.loop_start()


def currentTime():
    now = datetime.now()
    return now


while True:
    print (config.get('client', 'host'))
    mqttc.publish("test/topic", str(currentTime()))
    time.sleep(5)
