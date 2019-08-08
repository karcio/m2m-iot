# m2m-iot 0.1

## python implementation for publish, subscribe (mqtt) and feed database with readings from supporting sensors like following:

- BMP085

1. Install mqtt, python dependencies and start mosquitto

```
sudo apt-get -y mosquitto python3-devel
sudo systemctl start mosquitto.service
sudo apt-get install python3-venv
```

2. Clone git repository

```
git clone git@github.com:karcio/m2m-iot.git
```

3. create python environment

```
cd m2m-io
python3 -m venv virtenv
source virtenv/bin/activate
```

4. install python modules for

- publish.py

```
pip install paho-mqtt
pip install psycopg2
pip install Adafruit_BMP
pip install configparser
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

5. Install postgress database

```
sudo apt install postgresql
```

6. Create postgres user

```
sudo su postgres
createuser pi -P --interactive
```

7. Create database table and add user permissions to table

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
