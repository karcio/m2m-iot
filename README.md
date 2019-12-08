# m2m-iot 
#### version 0.2
* Tested on raspberry pi 1 and 3 (should work on 2 as well), os: `2019-09-26-raspbian-buster-lite.img`
* Python3 implementation for publish, subscribe (mqtt) and feed database with readings from supporting sensors:
   - BMP085
   - DHT11 (in testing)
   - DHT22 (in testing)
   - BMP280 
1. Install mqtttart (mosquitto)
```
sudo apt update -y 
sudo apt upgrade -y 
sudo apt install -y mosquitto 
```
2. Start mqtt, optional enable during boot
```
sudo systemctl start mosquitto.service
sudo systemctl enable mosquitto.service
```
3. Install python3 dependencies 
```
sudo apt install -y python3-dev python3-venv
```
4. Install git 
```
sudo apt install -y git
```
5. Clone git repository

```
cd ~ && git clone https://github.com/karcio/m2m-iot.git
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
# Publish
```
python publish.py kitchen/temp temp -> for temperature
python publish.py kitchen/pres pres -> for pressure
```
# Install and configure database
1. Install postgress database (only for server)
```
sudo apt install postgresql
```
2. Create postgres user (only for server)
```
sudo su postgres
createuser pi -P --interactive
```
3. Create database table and add user permissions to table (only for server)
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
4. Update config file (only for server)

```
mv config.template config
```
5. Edit file with database details
# Subscribe
```
python subscribe.py kitchen/temp hostname
python subscribe.py kitchen/pres hostname
```