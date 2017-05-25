from functions_lsm303 import functions_lsm303

mdp_lsm303 = functions_lsm303.mdp_lsm303

heading = mdp_lsm303.bearing()
tilt = mdp_lsm303.inclination()

print('Heading: {0}, Tilt: {1}'.format(heading,tilt))
