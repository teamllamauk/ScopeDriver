import dothat.backlight as backlight
import dothat.lcd as lcd
import RPi.GPIO as GPIO
import time
import threading
import functions_l298


global delay
global tracking

delay = 0.0012 #Step delay
tracking = 1


L298 = functions_l298.functions_l298(delay, '1')
L298.setupGPIO(17, 18, 22, 23, 1, 5, 6, 13)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

btn_red_pin = 27            # A
btn_green_pin = 24          # Y
btn_blue_pin = 9            # X
btn_yellow_pin = 19         # B
btn_black_top_pin = 16      # purple wire
btn_black_bottom_pin = 26   # grey wire

#GPIO outputs
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

#Callback Functions
def btn_Callback(button_pin):
    
    global delay
    global tracking
    
    #print('btn callback - %s', button_pin)
    
    if button_pin == btn_blue_pin:
        # Slow Down
        delay = delay + 0.0001
        L298.updateDelay(delay)
        print(delay)
    elif button_pin == btn_yellow_pin:
        # Speed Up
        delay = delay - 0.0001
        L298.updateDelay(delay)
        print(delay)
    elif button_pin == btn_red_pin:
        # Start
        tracking = 0
        print('Start')
    elif button_pin == btn_red_pin:
        # Stop
        L298.breakLoop(1)
        print('Stop')
    

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

#Main loop
while True:

    lcd.set_cursor_position(0,1)
    lcd.write("{:.4f}".format(delay))
    #lcd.write("{:.4f}".format(str(delay)))
    
    if tracking == 0:
        print('Drive 0, 1')
        L298.updateSteps(-1)
        t = threading.Thread(target=L298.driveMotor,args=(0,1))
        t.start()
        tracking = 1
        
    
    #print('End Loop')
    #time.sleep(10)
