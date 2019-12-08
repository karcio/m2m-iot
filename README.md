# m2m-iot 0.1

* Tested on raspberry pi 1 and 3 (should work on 2 as well), os raspbian "Raspbian Buster Lite" Version: September 2019

* Python implementation for publish, subscribe (mqtt) and feed database with readings from supporting sensors like following:

   - BMP085
   - DHT11 (in testing)
   - DHT22 (in testing)
   - BMP280 

1. Install mqtt, python dependencies and start mosquitto

```
sudo apt update -y 
sudo apt upgrade -y 
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
python publish.py kitchen/temp temp -> for temperature
python publish.py kitchen/pres pres -> for pressure
```

# Subscribe

```
python subscribe.py kitchen/temp hostname
python subscribe.py kitchen/pres hostname
```