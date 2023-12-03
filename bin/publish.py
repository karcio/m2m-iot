import paho.mqtt.client as mqtt
import time
import logging
import argparse

from bmp280 import getTempAndPressure

# from bmp280_k import getTempAndPressure
from aht20 import getHumidity

# from aht20_k import getHumidity
from lightSensor import readLight

# from lightSensor_k import readLight


parser = argparse.ArgumentParser()
parser.add_argument("topic", help="insert topic you want to publish")
parser.add_argument("stream", help="insert stream you want to publish")
args = parser.parse_args()


logging.basicConfig(
    format=" %(levelname)s - %(asctime)s - %(message)s ", level=logging.INFO
)


mqttc = mqtt.Client()
mqttc.connect("localhost")
mqttc.loop_start()


class HomeSensors(object):
    def main(self):
        while True:
            if args.stream == "temperature":
                try:
                    list = getTempAndPressure()
                    mqttc.publish(args.topic, float(list[0]), qos=2)
                    logging.info(
                        "sending data: %s - %s with topic: %s ",
                        float(list[0]),
                        args.stream,
                        args.topic,
                    )
                except:
                    logging.error("wrong reading from sensor")

            elif args.stream == "pressure":
                try:
                    list = getTempAndPressure()
                    mqttc.publish(args.topic, float(list[1]), qos=2)
                    logging.info(
                        "sending data: %s - %s with topic %s ",
                        float(list[1]),
                        args.stream,
                        args.topic,
                    )
                except:
                    logging.error("wrong reading from sensor")

            elif args.stream == "humidity":
                try:
                    list = getHumidity()
                    mqttc.publish(args.topic, list, qos=2)
                    logging.info(
                        "sending data: %s - %s with topic: %s ",
                        list,
                        args.stream,
                        args.topic,
                    )
                except:
                    logging.error("wrong reading from sensor")

            elif args.stream == "light":
                try:
                    list = readLight()
                    mqttc.publish(args.topic, list, qos=2)
                    logging.info(
                        "sending data: %s - %s with topic: %s ",
                        list,
                        args.stream,
                        args.topic,
                    )
                except:
                    logging.error("wrong reading from sensor")

            time.sleep(30)


if __name__ == "__main__":
    HomeSensors().main()
