import dothat.backlight as backlight
import dothat.lcd as lcd

lcd.clear()

backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write("Line 1")

lcd.set_cursor_position(0,1)
lcd.write("Line 2")

lcd.set_cursor_position(0,2)
lcd.write("Line 3")
