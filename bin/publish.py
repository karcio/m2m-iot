import paho.mqtt.client as mqtt
import time
import Adafruit_BMP.BMP085 as BMP085
import logging
import argparse
from gybmp280 import getReadings

parser = argparse.ArgumentParser()
parser.add_argument("topic", help="insert topic you want to publish")
parser.add_argument("stream", help="insert stream you want to publish")
args = parser.parse_args()

logging.basicConfig(
    format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)
#sensor = BMP085.BMP085()

mqttc = mqtt.Client()
mqttc.connect("localhost")
mqttc.loop_start()


class HomeSensors(object):

    def temp(self):

        return str(sensor.read_temperature())

    def pres(self):

        return str(sensor.read_pressure()/100)

    def main(self):
        while True:
            if args.stream == "bmp280-temp":
                list = getReadings()
                mqttc.publish(args.topic, float(list[0]), qos=2)
                logging.info("sending data %s to %s ", list[0], args.topic)
            
            elif args.stream == "bmp280-pres":
                list = getReadings()
                mqttc.publish(args.topic, float(list[1]), qos=2)
                logging.info("sending data %s to %s ", list[1], args.topic)
            
            elif args.stream == "temp":
                mqttc.publish(args.topic, float(self.temp()), qos=2)
                logging.info("sending data %s to %s ",
                             float(self.temp()), args.topic)

            elif args.stream == "press":
                mqttc.publish(args.topic, float(self.press()), qos=2)
                logging.info("sending data %s to %s ",
                             float(self.press()), args.topic)
           
            time.sleep(30)


if __name__ == "__main__":
    HomeSensors().main()
