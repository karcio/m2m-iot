import board
import adafruit_bmp280


def getTempAndPressure():
    i2c = board.I2C()
    sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

    return round(sensor.temperature, 1), round(sensor.pressure, 0)


def main():
    getTempAndPressure()


if __name__ == "__main__":
    main()
