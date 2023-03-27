import Adafruit_BMP.BMP085 as BMP085


def getBmp085Readings():
    sensor = BMP085.BMP085()
    temperature = sensor.read_temperature()
    pressure = sensor.read_pressure()/100
    #altitude = sensor.read_altitude()

    return temperature, pressure


def main():
    getBmp085Readings()


if __name__ == "__main__":
    main()
