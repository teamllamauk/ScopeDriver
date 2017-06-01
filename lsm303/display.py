import dothat.backlight as backlight
import dothat.lcd as lcd
import functions_lsm303


compass = functions_lsm303.functions_lsm303()

heading = compass.bearing()
tilt = compass.inclination()

lcd.clear()
backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write('Heading: {0}'.format(heading))

lcd.set_cursor_position(0,1)
lcd.write('Tilt: {0}'.format(tilt))
