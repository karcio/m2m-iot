import paho.mqtt.subscribe as subscribe
from datetime import datetime
import psycopg2
from config import configuration
import logging
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("topic", help="insert topic you want to subscribe")
parser.add_argument("host", help="insert hostname you want to subscribe")
args = parser.parse_args()

logging.basicConfig(
    format=" %(levelname)s - %(asctime)s - %(message)s ", level=logging.INFO
)


class Readings(object):
    def currentTime(self):
        return datetime.now().isoformat()

    def connectionToDb(self, payload, topic):
        connection = psycopg2.connect(
            user="",
            password="",
            host="",
            port="",
            database="",
        )
        cursor = connection.cursor()

        if args.topic == "celbridge/shed/temperature":
            cursor.execute(
                "INSERT INTO readings (temperature, pressure, humidity, light, channel, lastupdate) VALUES ('"
                + payload
                + "', null, null, null, '"
                + topic
                + "', '"
                + self.currentTime()
                + "');"
            )
        elif args.topic == "celbridge/shed/pressure":
            cursor.execute(
                "INSERT INTO readings (temperature, pressure, humidity, light, channel, lastupdate) VALUES (null,'"
                + payload
                + "', null, null, '"
                + topic
                + "','"
                + self.currentTime()
                + "');"
            )
        elif args.topic == "celbridge/shed/humidity":
            cursor.execute(
                "INSERT INTO readings (temperature, pressure, humidity, light, channel, lastupdate) VALUES (null,null, '"
                + payload
                + "', null, '"
                + topic
                + "','"
                + self.currentTime()
                + "');"
            )
        elif args.topic == "celbridge/shed/light":
            cursor.execute(
                "INSERT INTO readings (temperature, pressure, humidity, light, channel, lastupdate) VALUES (null,null,null,'"
                + payload
                + "','"
                + topic
                + "','"
                + self.currentTime()
                + "');"
            )

        connection.commit()
        cursor.close()
        connection.close()
        logging.info("Data %s inserted to database", payload)

    def subscribe(self):
        while True:
            try:
                msg = subscribe.simple(args.topic, hostname="")
                payload = msg.payload.decode("utf-8")
                topic = msg.topic
                self.connectionToDb(payload, topic)
            except:
                print("host does not exists - waiting...")

    def main(self):
        self.subscribe()


if __name__ == "__main__":
    Readings().main()
