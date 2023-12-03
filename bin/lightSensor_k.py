import smbus
import time

# Define some constants from the datasheet
DEVICE = 0x23  # Default device I2C address
POWER_DOWN = 0x00  # No active state
POWER_ON = 0x01  # Power on
RESET = 0x07  # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

# Kalman filter parameters
Q = 1e-5  # Process noise covariance
R = 0.01  # Measurement noise covariance
x_0 = 0.0  # Initial estimate of the state (light)
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


def convertToNumber(data):
    # Simple function to convert 2 bytes of data
    # into a decimal number
    return (data[1] + (256 * data[0])) / 1.2


def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE)
    light_measurement = round(convertToNumber(data), 0)

    # Apply Kalman filter
    filtered_light = kalman_filter(light_measurement)

    return filtered_light


def main():
    filtered_light = readLight()
    print(f"Filtered Light: {filtered_light}")


if __name__ == "__main__":
    main()
