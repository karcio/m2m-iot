import board
import adafruit_ahtx0

# Kalman filter parameters
Q = 1e-5  # Process noise covariance
R = 0.01  # Measurement noise covariance
x_0 = 50.0  # Initial estimate of the state (humidity)
P_0 = 1.0  # Initial estimate of the state covariance

# Kalman filter variables
x_hat = x_0
P = P_0


def kalman_filter(z):
    global x_hat, P

    # Prediction step
    x_hat_minus = x_hat
    P_minus = P + Q

    # Update step
    K = P_minus / (P_minus + R)
    x_hat = x_hat_minus + K * (z - x_hat_minus)
    P = (1 - K) * P_minus

    return x_hat


def getHumidity():
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)

    num_measurements = 10
    humidity_sum = 0

    for _ in range(num_measurements):
        humidity_measurement = round(sensor.relative_humidity, 0)

        # Apply Kalman filter
        filtered_humidity = kalman_filter(humidity_measurement)

        humidity_sum += filtered_humidity

    # Calculate the average of filtered values
    avg_humidity = humidity_sum / num_measurements

    return round(avg_humidity, 1)


def main():
    filtered_humidity = getHumidity()
    print(f"Average Filtered Humidity: {filtered_humidity:.2f}%")


if __name__ == "__main__":
    main()
