from functions_lsm303 import mpd_LSM303

heading = mpd_LSM303.bearing()
tilt = mpd_LSM303.inclination()

print('Heading: {0}, Tilt: {1}'.format(heading,tilt))
