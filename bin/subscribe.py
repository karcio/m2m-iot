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
    format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)


class Readings(object):

    def currentTime(self):

        return datetime.now().isoformat()

    def connectionToDb(self, payload, topic):
        connection = psycopg2.connect(user=configuration().getDbUser(),
                                      password=configuration().getDbPassword(),
                                      host=configuration().getDbHost(),
                                      port=configuration().getDbPort(),
                                      database=configuration().getDbDatabase())
        cursor = connection.cursor()

        if args.topic == "kitchen/temp":
            cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES ('" +
                           payload+"',null,'"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "kitchen/pres":
            cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES (null,'" +
                           payload+"','"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "livingroom/temp":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES ('"+payload+"',null,'"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "livingroom/pres":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES (null,'"+payload+"','"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "bedroom1/temp":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES ('"+payload+"',null,'"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "bedroom1/pres":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES (null,'"+payload+"','"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "bedroom2/temp":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES ('"+payload+"',null,'"+topic+"','" + self.currentTime() + "');")
        elif args.topic == "bedroom2/pres":
                cursor.execute("INSERT INTO readings (temperature, pressure, channel, lastupdate) VALUES (null,'"+payload+"','"+topic+"','" + self.currentTime() + "');")


        connection.commit()
        cursor.close()
        connection.close()
        logging.info("Data %s inserted to database", payload)

    def subscribe(self):
        while True:
            msg = subscribe.simple(args.topic, hostname=args.host)
            payload = msg.payload.decode("utf-8")
            topic = msg.topic
            self.connectionToDb(payload, topic)

    def main(self):
        self.subscribe()


if __name__ == "__main__":
    Readings().main()
