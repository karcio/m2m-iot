# m2m-iot

version 0.3.1

---

- Tested on raspberry pi 1 and 3 (should work on 2 as well), os: `2023-02-21-raspios-bullseye-armhf-lite.img`
- Python3 implementation for publish, subscribe (mqtt) and feed database with readings from supporting sensors:
  - BMP085, BMP280
  - DHT11
  - AHT20
  - PIR sensor
  - BH1750

1. Setup your rpi
   ```
   sudo raspi-config
   ```

- Interface Options > I2C > set active
- Install I2c
  ```
  sudo apt-get install -y i2c-tools
  sudo reboot
  ```
- check if i2c can detect attached sensor (fe. BMP085)
  ```
  sudo i2cdetect -y 0
  or
  sudo i2cdetect -y 1
  ```

2. Add user to gpio group

   ```
   sudo usermod -a -G gpio $USER
   ```

3. Install mqtttart (mosquitto)

   ```
   sudo apt update -y
   sudo apt upgrade -y
   sudo apt install -y mosquitto
   ```

4. Start mqtt, optional enable during boot

   ```
   sudo systemctl enable --now mosquitto.service
   ```

5. Install python3 dependencies

   ```
   sudo apt install -y python3-dev python3-pip python3-venv
   ```

6. Install git

   ```
   sudo apt install -y git
   ```

7. Clone git repository

   ```
   cd ~ && git clone https://github.com/karcio/m2m-iot.git
   ```

8. create python environment

   ```
   cd m2m-iot
   python3 -m venv .venv
   source .venv/bin/activate
   ```

9. Install libgpiod2

   ```
   sudo apt install libgpiod2
   ```

10. Install python modules for

```
pip install -r requirements.txt
```

# Publish

```
python bin/publish.py celbridge/shed/temperature temperature 	# for temperature
python bin/publish.py celbridge/shed/pressure pressure 		   # for pressure
python bin/publish.py celbridge/shed/humidity humidity 		   # for humidity
python bin/publish.py celbridge/shed/light light 		         # for light
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
   CREATE DATABASE localweatherdb;
   CREATE USER dbuser;
   ALTER USER dbuser WITH ENCRYPTED PASSWORD 'pa88w0rd';
   ALTER DATABASE localweatherdb OWNER TO dbuser;
   \c localweatherdb;
   DROP TABLE readings;
   CREATE TABLE readings(
      id serial PRIMARY KEY,
      temperature NUMERIC NULL,
      pressure NUMERIC NULL,
      humidity NUMERIC NULL,
      light NUMERIC NULL,
      channel VARCHAR (30) NOT NULL,
      lastupdate TIMESTAMP NOT NULL
      );
   GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO dbuser;
   GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to dbuser;
   GRANT ALL PRIVILEGES ON DATABASE localweatherdb TO dbuser;
   ```

4. Update config file (only for server)

   ```
   mv config.template config
   ```

5. Edit file with database details

# Subscribe

```
python bin/subscribe.py celbridge/shed/temperature hostname
python bin/subscribe.py celbridge/shed/pressure hostname
python bin/subscribe.py celbridge/shed/humidity hostname
python bin/subscribe.py celbridge/shed/light hostname

```
