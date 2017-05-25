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
       
    #Acc Mins: -1346, -1375, -1143
    #Acc Maxs: 961, 1511, 1255
    #Mag Mins: -695, -529, -797
    #Mag Maxs: 503, 679, 323
    
    MminX = -695
    MmaxX = 503
    
    MminY = -529
    MmaxY = 679
    
    MminZ = -797
    MmaxZ = 323
    
    Axn = accel_x / math.sqrt(accel_x * accel_x + accel_y * accel_y + accel_z * accel_z)
    Ayn = accel_y / math.sqrt(accel_x * accel_x + accel_y * accel_y + accel_z * accel_z)
    
    pitch = math.asin(Axn)
    roll = -math.asin(Ayn / math.cos(pitch))
    
    Mxc = (mag_x - MminX) / (MmaxX - MminX) * 2 - 1
    Myc = (mag_y - MminY) / (MmaxY - MminY) * 2 - 1
    Mzc = (mag_z - MminZ) / (MmaxZ - MminZ) * 2 - 1
    
    magXcomp_cal = Mxc * math.cos(pitch) + Mzc * math.sin(pitch)
    magYcomp_cal = Mxc * math.sin(roll) * math.sin(pitch) + Myc * math.cos(roll) - Mzc * math.sin(roll) * math.cos(pitch)
    
    magXcomp = mag_x * math.cos(pitch) + mag_z * math.sin(pitch)
    magYcomp = mag_x * math.sin(roll) * math.sin(pitch) + mag_y * math.cos(roll) - mag_z * math.sin(roll) * math.cos(pitch)
    
    heading = (math.atan2(mag_y, mag_x) * 180) / math.pi
    if heading < 0:
        heading = 360 + heading
        
    headingTilt = (math.atan2(magYcomp, magXcomp) * 180) / math.pi
    if headingTilt < 0:
        headingTilt = 360 + headingTilt
        
    headingTiltCal = (math.atan2(magYcomp_cal, magXcomp_cal) * 180) / math.pi
    if headingTiltCal < 0:
        headingTiltCal = 360 + headingTiltCal
        
    print('Compass heading: {0}'.format(heading))
    print('Tilt Compass heading: {0}'.format(headingTilt))
    print('Cal Tilt Compass heading: {0}'.format(headingTiltCal))
    
    # Wait half a second and repeat.
    time.sleep(0.5)

