import functions_lsm303

compass = functions_lsm303.functions_lsm303()

heading, headingCal, headingTilt = compass.bearing()
altHeadingA = compass.bearingAltA()
tilt = compass.inclination()

print('Heading: {0}'.format(heading))
print('Heading Cal: {0}'.format(headingCal))
print('Heading Tilt: {0}'.format(headingTilt))
print('Alt Heading: {0}'.format(altHeadingA))
#print('Tilt: {0}'.format(tilt))
