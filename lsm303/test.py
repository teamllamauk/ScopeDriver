from functions_lsm303 import mpd_LSM303

heading = functions_lsm303.bearing()
tilt = functions_lsm303.inclination()

print('Heading: {0}, Tilt: {1}'.format(heading,tilt))
