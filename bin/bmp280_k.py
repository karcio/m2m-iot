import board
import adafruit_bmp280
import numpy as np

# Kalman filter parameters for temperature
Q_temp = 1e-5  # Process noise covariance for temperature
R_temp = 0.1  # Measurement noise covariance for temperature
x_0_temp = 25.0  # Initial estimate of the state (temperature)
P_0_temp = 1.0  # Initial estimate of the state covariance for temperature

# Kalman filter parameters for pressure
Q_pressure = 1e-5  # Process noise covariance for pressure
R_pressure = 10.0  # Measurement noise covariance for pressure
x_0_pressure = 1000.0  # Initial estimate of the state (pressure)
P_0_pressure = 1.0  # Initial estimate of the state covariance for pressure

# Kalman filter variables for temperature
x_hat_temp = x_0_temp
P_temp = P_0_temp

# Kalman filter variables for pressure
x_hat_pressure = x_0_pressure
P_pressure = P_0_pressure


def kalman_filter(z, x_hat, P, Q, R):
    # Prediction step
    x_hat_minus = x_hat
    P_minus = P + Q

    # Update step
    K = P_minus / (P_minus + R)
    x_hat = x_hat_minus + K * (z - x_hat_minus)
    P = (1 - K) * P_minus

    return x_hat, P


def getTempAndPressure():
    i2c = board.I2C()
    sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

    num_measurements = 10
    temp_sum = 0
    pressure_sum = 0

    for _ in range(num_measurements):
        temperature_measurement = round(sensor.temperature, 1)
        pressure_measurement = round(sensor.pressure, 0)

        # Apply Kalman filter for temperature
        global x_hat_temp, P_temp
        x_hat_temp, P_temp = kalman_filter(
            temperature_measurement, x_hat_temp, P_temp, Q_temp, R_temp
        )

        # Apply Kalman filter for pressure
        global x_hat_pressure, P_pressure
        x_hat_pressure, P_pressure = kalman_filter(
            pressure_measurement, x_hat_pressure, P_pressure, Q_pressure, R_pressure
        )

        temp_sum += x_hat_temp
        pressure_sum += x_hat_pressure

    # Calculate the average of filtered values
    avg_temp = temp_sum / num_measurements
    avg_pressure = pressure_sum / num_measurements

    return round(avg_temp, 1), round(avg_pressure, 1)


def main():
    filtered_temp, filtered_pressure = getTempAndPressure()
    # print(
    #     f"Average Filtered Temperature: {filtered_temp} °C | Average Filtered Pressure: {filtered_pressure} hPa"
    # )


if __name__ == "__main__":
    main()
