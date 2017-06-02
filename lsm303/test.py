import functions_lsm303

compass = functions_lsm303.functions_lsm303()

accRaw, magRaw = compass.rawData()


heading, headingCal, headingTilt = compass.bearing()
altHeadingA = compass.bearingAltA()
tilt = compass.inclination()

print('Raw Acc Data: {0}'.format(accRaw))
print('Raw Mag Data: {0}'.format(magRaw))
print('Heading: {0}'.format(heading))
print('Heading Cal: {0}'.format(headingCal))
print('Heading Tilt: {0}'.format(headingTilt))
print('Alt Heading: {0}'.format(altHeadingA))
#print('Tilt: {0}'.format(tilt))
