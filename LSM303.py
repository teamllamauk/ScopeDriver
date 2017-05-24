# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain
import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    
    Axn = accel_x / math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
    Ayn = accel_y / math.sqrt(accel_x**2 + accel_y**2 + accel_z**2)
    
    pitch = math.asin(-Axn)
    roll = math.asin(Ayn / math.cos(pitch))
    
    #Acc Mins: -1290, -1306, -1017
    #Acc Maxs: 1010, 1173, 1217
    #Mag Mins: -767, -556, -1018
    #Mag Maxs: 886, 1013, 670
    
    MminX = -767
    MmaxX = 886
    
    MminY = -556
    MmaxY = 1013
    
    MminZ = -1018
    MmaxZ = 670
    
    Mxc = (mag_x - MminX) / (MmaxX - MminX) * 2 - 1
    Myc = (mag_y - MminY) / (MmaxY - MminY) * 2 - 1
    Mzc = (mag_z - MminZ) / (MmaxZ - MminZ) * 2 - 1
    
    Mxh = Mxc * math.cos(pitch) + Mzc * math.sin(pitch)
    Myh = Mxc * math.sin(roll) * math.sin(pitch) + Myc * math.cos(roll) - Mzc * math.sin(roll) * math.cos(pitch)
        
    heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
    if heading < 0:
        heading = 360 + heading
        
    headingTilt = (math.atan2(Mxh, Mxh) * 180) / math.pi
    if headingTilt < 0:
        headingTilt = 360 + headingTilt
        
    print('Compass heading: {0}'.format(heading))
    print('Tilt Compass heading: {0}'.format(headingTilt))
    
    # Wait half a second and repeat.
    time.sleep(0.5)

