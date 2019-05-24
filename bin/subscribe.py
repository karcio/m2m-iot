import paho.mqtt.subscribe as subscribe
import time

while True:
    msg = subscribe.simple("test/topic", hostname="localhost")
    print(msg.topic+" "+str(msg.payload))
    time.sleep(5)
