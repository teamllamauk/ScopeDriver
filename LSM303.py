# I2C Addresses for device registers
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

bus = smbus.SMBus(0)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

COMPASS_ADDRESS = 0x3D      #7 bit address (will be left shifted to add the read write bit)
LINACC_ADDRESS = 0x33
TEMP_ADDRESS = 0x3D
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

#Write a single register
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, 0x80)

#Write an array of registers
ledout_values = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG_LEDOUT0, ledout_values)
