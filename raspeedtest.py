import dothat.backlight as backlight
import dothat.lcd as lcd
import RPi.GPIO as GPIO
import time
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

global delay 
delay = 0.0012

#Setup LCD
lcd.clear()
backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write("Delay")

lcd.set_cursor_position(0,1)
lcd.write(str(delay))

lcd.set_cursor_position(0,2)
lcd.write("X inc - Y dec")

# Pin assignments
coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 22
coil_B_2_pin = 23

# Button Layout
#
#       X                   Blue
#   Y       A           Green   Red
#       B                   Yellow
#

btn_red_pin = 27        # A
btn_green_pin = 24      # Y
btn_blue_pin = 9        # X
btn_yellow_pin = 19     # B
btn_black_top_pin = 16
btn_black_bottom_pin = 26

#GPIO outputs
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#Callback Functions
def btn_Callback(button_pin):
    
    global delay
    
    print('btn callback - %s', button_pin)
    
    if button_pin == btn_blue_pin:
        delay = delay + 0.0001
    elif button_pin == btn_yellow_pin:
        delay = delay - 0.0001

#GPIO inputs
GPIO.setup(btn_red_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_red_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

GPIO.setup(btn_green_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_green_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

GPIO.setup(btn_blue_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_blue_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

GPIO.setup(btn_yellow_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_yellow_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

GPIO.setup(btn_black_top_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_black_top_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

GPIO.setup(btn_black_bottom_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(btn_black_bottom_pin, GPIO.RISING, callback=btn_Callback, bouncetime=200)

#Functions
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

#Main loop
while True:
        
    lcd.set_cursor_position(0,1)
    lcd.write(str(delay))
    
    setStep(1,0,0,0)
    time.sleep(delay)
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(0,0,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
