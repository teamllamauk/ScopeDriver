# I2C Addresses for device registers
# ----------------------------------
# https://cdn-shop.adafruit.com/datasheets/LSM303DLHC.PDF
# https://github.com/adafruit/Adafruit_Python_LSM303
#
#
# Check Device addresses (0x33/0x3D) with 'i2cdetect -y 0' in shell
#
# Compass: 0x3D ??? 
# Compass X: 0x03 & 0x04
# Compass Y: 0x05 & 0x06
# Compass Z: 0x07 & 0x08
#
# Lin Accel: 0x33 ???
# Lin Accel X: 0x28 & 0x29
# Lin Accel Y: 0x2A & 0x2B
# Lin Accel Z: 0x2C & 0x2D
#
# Temp: 0x3D ???
# Temp: 0x31 & 0x32
#
#!/usr/bin/python

import smbus
busnumber = 0     # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
bus = smbus.SMBus(busnumber)    

COMPASS_ADDRESS = 0x3D      
LINACC_ADDRESS = 0x33
TEMP_ADDRESS = 0x3D

COMPASS_X_REGISTERS = [0x03, 0x04]
COMPASS_Y_REGISTERS = [0x05, 0x06]
COMPASS_Z_REGISTERS = [0x07, 0x08]

#Write an array of registers

compass_x = bus.read_i2c_block_data(COMPASS_ADDRESS, cmd)
