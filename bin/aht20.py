import board
import adafruit_ahtx0


def getHumidity():
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    return round(sensor.relative_humidity, 0)


def main():
    getHumidity()


if __name__ == "__main__":
    main()
