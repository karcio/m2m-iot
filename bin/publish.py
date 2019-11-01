import paho.mqtt.client as mqtt
import time
import Adafruit_BMP.BMP085 as BMP085
import logging
import argparse
from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

parser = argparse.ArgumentParser()
parser.add_argument("topic", help="insert topic you want to publish")
parser.add_argument("stream", help="insert stream you want to publish")
args = parser.parse_args()

logging.basicConfig(
    format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)
sensor = BMP085.BMP085()
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

mqttc = mqtt.Client()
mqttc.connect("localhost")
mqttc.loop_start()


class HomeSensors(object):

    def temp(self):

        return str(sensor.read_temperature())

    def hum(self):

        return str(sensor.read_pressure()/100)

    def bmp280temp(self):

        return str(bmp280.get_temperature())

    def bmp280pres(self):

        return str(bmp280.get_pressure())

    def main(self):
        while True:

            if args.stream == "temp":
                mqttc.publish(args.topic, float(self.temp()), qos=2)
                logging.info("sending data %s to %s ",
                             float(self.temp()), args.topic)

            elif args.stream == "press":
                mqttc.publish(args.topic, float(self.press()), qos=2)
                logging.info("sending data %s to %s ",
                             float(self.press()), args.topic)

            elif args.stream == "bmp280temp":
                mqttc.publish(args.topic, float(self.bmp280temp()), qos=2)
                logging.info("sending data %s to %s ", float(
                    self.bmp280temp()), args.topic)

            elif args.stream == "bmp280pres":
                mqttc.publish(args.topic, float(self.bmp280pres()), qos=2)
                logging.info("sending data %s to %s ", float(
                    self.bmp280pres()), args.topic)

            time.sleep(5)


if __name__ == "__main__":
    HomeSensors().main()
