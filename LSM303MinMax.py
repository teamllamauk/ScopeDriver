import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

AccelMinX = 0
AccelMaxX = 0
AccelMinY = 0
AccelMaxY = 0
AccelMinZ = 0
AccelMaxZ = 0

MagMinX = 0
MagMaxX = 0
MagMinY = 0
MagMaxY = 0
MagMinZ = 0
MagMaxZ = 0


print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    
    if accel_x < AccelMinX:
        AccelMinX = accel_x
        
    
