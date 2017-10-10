#!/usr/bin/env python

import sys
import time
import RPi.GPIO as GPIO

import dothat.backlight as backlight
import dothat.lcd as lcd
from dot3k.menu import Menu, MenuOption
from subprocess import call

# Add the root examples dir so Python can find the plugins
sys.path.append('../')

from plugins.text import Text


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

def setBackLightGreen():    
    backlight.rgb(0, 255, 0)
    
def setBackLightRed():
    backlight.rgb(255, 0, 0)

def exitProg(): 
    # Do exit and shutdown system
    print("Shutting Down")
    call("sudo shutdown -h now", shell=True)
    
    
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




print("Press CTRL+C to exit.")

menu = Menu(
    structure={
        'test': lambda: exitProg(),
        'Green': lambda: setBackLightGreen(),        
        'Red': lambda: setBackLightRed(),
        'Exit': lambda: exitProg()
    },
    lcd=lcd
    )



while 1:    
    menu.redraw()
    time.sleep(0.05)
