import serial
import time

# Establish a serial connection (make sure to replace '/dev/ttyUSB0' with your Arduino serial port)
ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2) # Wait for the connection to be established

def blink_led():
    ser.write(b'H')  # Send 'H' to turn on the LED
    time.sleep(0.3)    # Wait for 1 second
    ser.write(b'L')  # Send 'L' to turn off the LED
    time.sleep(0.3)    # Wait for 1 second

# Blink the LED 5 times
for _ in range(10):
    blink_led()

# Close the serial connection
ser.close()
