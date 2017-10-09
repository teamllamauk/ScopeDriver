#!/usr/bin/env python

import sys
import time
import RPi.GPIO as GPIO

import dothat.backlight as backlight
import dothat.lcd as lcd
import dothat.touch as nav
from dot3k.menu import Menu, MenuOption

# Add the root examples dir so Python can find the plugins
sys.path.append('../')

#from plugins.clock import Clock
#from plugins.graph import IPAddress, GraphTemp, GraphCPU, GraphNetSpeed
from plugins.text import Text
#from plugins.utils import Backlight, Contrast
#from plugins.wlan import Wlan

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LCD
lcd.clear()
backlight.rgb(255, 0, 0)

btn_red_pin = 27            # A
btn_green_pin = 24          # Y
btn_blue_pin = 9            # X
btn_yellow_pin = 19         # B
btn_black_top_pin = 16      # purple wire
btn_black_bottom_pin = 26   # grey wire

# Callback Functions
def btn_Callback(button_pin):
    if button_pin == btn_green_pin:
        menu.select_option()        
    elif button_pin == btn_black_top_pin:
        menu.up()
    elif button_pin == btn_black_top_pin:
        menu.down()


GPIO.setup(btn_red_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_red_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_green_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_green_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_blue_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_blue_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_yellow_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_yellow_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_black_top_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_black_top_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_black_bottom_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_black_bottom_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

print("""
This advanced example uses the menu framework.
It gives you a basic menu setup with plugins. You should be able to view system info and adjust settings!
Press CTRL+C to exit.
""")


"""
Using a set of nested lists you can describe
the menu you want to display on dot3k.
Instances of classes derived from MenuOption can
be used as menu items to show information or change settings.
See GraphTemp, GraphCPU, Contrast and Backlight for examples.
"""

menu = Menu(
    structure={
        'Setup': '1',        
        'Tracking': '2',
        'Exit': '3'
    },
    lcd=lcd,    
    input_handler=Text())

"""
You can use anything to control dot3k.menu,
but you'll probably want to use dot3k.touch
"""
#nav.bind_defaults(menu)

while 1:    
    menu.redraw()
    time.sleep(0.05)
