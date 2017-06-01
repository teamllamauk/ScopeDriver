import time
import dothat.backlight as backlight
import dothat.lcd as lcd
import functions_lsm303


compass = functions_lsm303.functions_lsm303()

lcd.clear()
backlight.rgb(255, 0, 0)

while True:
    heading = compass.bearing()
    tilt = compass.inclination()

    lcd.clear()
    
    lcd.set_cursor_position(0,0)
    lcd.write('H: {0}'.format(heading))

    lcd.set_cursor_position(9,0)
    lcd.write('T: {0}'.format(tilt))

    time.sleep(0.1)
