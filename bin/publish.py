import paho.mqtt.client as mqtt
import time
import logging
import argparse
from bmp085 import getBmp085Readings

parser = argparse.ArgumentParser()
parser.add_argument("topic", help="insert topic you want to publish")
parser.add_argument("stream", help="insert stream you want to publish")
args = parser.parse_args()

logging.basicConfig(format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)

mqttc = mqtt.Client()
mqttc.connect("localhost")
mqttc.loop_start()


class HomeSensors(object):

    def main(self):
        while True:
            if args.stream == "temperature":
                list = getBmp085Readings()
                mqttc.publish(args.topic, float(list[0]), qos=2)
                logging.info("sending data: %s - %s with topic: %s ", float(list[0]), args.stream, args.topic)

            elif args.stream == "pressure":
                list = getBmp085Readings()
                mqttc.publish(args.topic, float(list[1]), qos=2)
                logging.info("sending data: %s - %s with topic %s ", float(list[1]), args.stream, args.topic)
           
            time.sleep(30)


if __name__ == "__main__":
    HomeSensors().main()
