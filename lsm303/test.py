import functions_lsm303

compass = functions_lsm303.functions_lsm303()

heading = compass.bearing()
tilt = compass.inclination()

print('Heading: {0}, Tilt: {1}'.format(heading,tilt))
