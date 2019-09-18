# m2m-iot 0.1

* Tested on raspberry pi 1 and 3 (should work on 2 as well), os raspbian "Raspbian Buster Lite" Version: July 2019

* Python implementation for publish, subscribe (mqtt) and feed database with readings from supporting sensors like following:

   - BMP085
   - DHT11
   - DHT22

1. Install mqtt, python dependencies and start mosquitto

```
sudo apt-get -y install mosquitto git python3-dev vim
sudo systemctl start mosquitto.service
sudo systemctl enable mosquitto.service
sudo apt-get install python3-venv
```

2. Clone git repository

```
git clone https://github.com/karcio/m2m-iot.git
```

3. create python environment

```
cd m2m-iot
python3 -m venv virtenv
source virtenv/bin/activate
```

4. install python modules for

- publish.py

```
pip install paho-mqtt
pip install psycopg2
pip install Adafruit_BMP
pip install Adafruit_DHT
pip install configparser
pip install wheel
```

- subscribe.py

```
pip install paho-mqtt
pip install psycopg2
```

\*alternatively you can install all modules

```
pip install -r requirements.txt
```

5. Install postgress database (only for server)

```
sudo apt install postgresql
```

6. Create postgres user (only for server)

```
sudo su postgres
createuser pi -P --interactive
```

7. Create database table and add user permissions to table (only for server)

```
psql -d homereadings

DROP TABLE readings;
CREATE TABLE readings(
   id serial PRIMARY KEY,
   temperature NUMERIC NULL,
   pressure NUMERIC NULL,
   channel VARCHAR (30) NOT NULL,
   lastupdate TIMESTAMP NOT NULL
   );
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO dbuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to dbuser;
```

8. Update config file (only for server)

```
mv config.template config
```

\*and edit file with database details

# Publish

```
sudo python publish.py home/kitchen/bmp085/temp temp
sudo python publish.py home/kitchen/bmp085/pres pres
```

# Subscribe

```
python subscribe.py home/kitchen/bmp085/temp hostname
python subscribe.py home/kitchen/bmp085/pres hostname
```
