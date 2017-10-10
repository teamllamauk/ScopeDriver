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
backlight.rgb(255, 255, 0)

btn_red_pin = 27            # A
btn_green_pin = 24          # Y
btn_blue_pin = 9            # X
btn_yellow_pin = 19         # B
btn_black_top_pin = 16      # purple wire
btn_black_bottom_pin = 26   # grey wire

def backLight(r, g, b):
    backlight.rgb(r, g, b)

def exitProg():
    a = 1
    # Do exit and shutdown system
    
# Callback Functions
def btn_Callback(button_pin):
    if button_pin == btn_green_pin:
        menu.select_option()        
    elif button_pin == btn_black_top_pin:
        menu.up()
    elif button_pin == btn_black_bottom_pin:
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


menu = Menu(
    structure={
        'test': exitProg(),
        'Setup': backLight(0, 255, 255),        
        'Tracking': backLight(0, 100, 255),
        'Exit': exitProg()
    },
    lcd=lcd,    
    input_handler=Text())



while 1:    
    menu.redraw()
    time.sleep(0.05)
