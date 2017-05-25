from functions_lsm303 import *

heading = functions_lsm303.bearing()
tilt = functions_lsm303.inclination()

print('Heading: {0}, Tilt: {1}'.format(heading,tilt))
