import board
import adafruit_dht


dhtDevice = adafruit_dht.DHT11(board.D4)


def getDHT11Humidity():
    humidity = dhtDevice.humidity

    return humidity


def main():
    getDHT11Humidity()
    dhtDevice.exit()


if __name__ == "__main__":
    main()
