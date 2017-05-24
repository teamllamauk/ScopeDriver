import time
import math

# Import the LSM303 module.
import Adafruit_LSM303


# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

AccelMinX = 0
AccelMaxX = 0
AccelMinY = 0
AccelMaxX = 0
AccelMinY = 0
AccelMaxZ = 0

MagMinX = 0
MagMaxX = 0
MagMinY = 0
MagMaxX = 0
MagMinY = 0
MagMaxZ = 0

lastmillis = int(round(time.time() * 1000))

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    
    millis = int(round(time.time() * 1000))
    
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    
    if accel_x < AccelMinX:
        AccelMinX = accel_x
            
    if accel_y < AccelMinY:
        AccelMinY = accel_y
        
    if accel_z < AccelMinZ:
        AccelMinZ= accel_z
    
    if accel_x > AccelMaxX:
        AccelMaxX = accel_x
            
    if accel_y > AccelMaxY:
        AccelMaxY = accel_y
        
    if accel_z > AccelMaxZ:
        AccelMaxZ= accel_z
    
    if mag_x < MagMinX:
        MagMinX = mag_x
            
    if mag_y < MagMinY:
        MagMinY = mag_y
        
    if mag_z < MagMinZ:
        MagMinZ = mag_z
        
    if mag_x > MagMaxX:
        MagMaxX = mag_x
            
    if mag_y > MagMaxY:
        MagMaxY = mag_y
        
    if mag_z > MagMaxZ:
        MagMaxZ = mag_z
        
    if (millies - lastmillis) > 1000:
        print('Acc Mins: {0}, {1}, {2}'.format(AccelMinX,AccelMinY,AccelMinZ))
        print('Acc Maxs: {0}, {1}, {2}'.format(AccelMinX,AccelMinY,AccelMinZ))
        print('Mag Mins: {0}, {1}, {2}'.format(MagMinX,MagMinY,MagMinZ))
        print('Mag Maxs: {0}, {1}, {2}'.format(MagMaxX,MagMaxY,MagMaxZ))
