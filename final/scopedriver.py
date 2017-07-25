import dothat.backlight as backlight
import dothat.lcd as lcd
import RPi.GPIO as GPIO
import time
import threading
import functions_l298


global delay
global tracking
global direction # forward = 1, reverse = 0

delay = 0.0012 #Step delay
tracking = 1
direction = 1


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Setup LCD
lcd.clear()
backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write("Mode: ")

lcd.set_cursor_position(0,1)
lcd.write("Delay: ")

lcd.set_cursor_position(0,2)
lcd.write("Dir: ")

#lcd.set_cursor_position(7,1)
#lcd.write("{:.4f}".format(delay))



# Pin assignments
RA_coil_A_1_pin = 17
RA_coil_A_2_pin = 18
RA_coil_B_1_pin = 22
RA_coil_B_2_pin = 23

DEC_coil_A_1_pin = 1
DEC_coil_A_2_pin = 5
DEC_coil_B_1_pin = 6
DEC_coil_B_2_pin = 13

L298 = functions_l298.functions_l298(delay, '1')
L298.setupGPIO(RA_coil_A_1_pin, RA_coil_A_2_pin, RA_coil_B_1_pin, RA_coil_B_2_pin, DEC_coil_A_1_pin, DEC_coil_A_2_pin, DEC_coil_B_1_pin, DEC_coil_B_2_pin)

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
#GPIO.setup(RA_coil_A_1_pin, GPIO.OUT)
#GPIO.setup(RA_coil_A_2_pin, GPIO.OUT)
#GPIO.setup(RA_coil_B_1_pin, GPIO.OUT)
#GPIO.setup(RA_coil_B_2_pin, GPIO.OUT)

#Callback Functions
def btn_Callback(button_pin):
    
    global delay
    global tracking
    global direction
    
    #print('btn callback - %s', button_pin)
    
    if button_pin == btn_blue_pin:
        # Slow Down
        delay = delay + 0.0001
        L298.updateDelay(delay)
        #print(delay)
    elif button_pin == btn_yellow_pin:
        # Speed Up
        delay = delay - 0.0001
        L298.updateDelay(delay)
        #print(delay)
    elif button_pin == btn_green_pin:
        # Start
        L298.breakTheLoop('0')
        if tracking == 0:
            L298.updateSteps(-1)
            t = threading.Thread(target=L298.halfStepDriveMotor,args=(0,direction))
            t.start()
            tracking = 1
        print('Start')
    elif button_pin == btn_red_pin:
        # Stop
        tracking = 0
        L298.breakTheLoop('1')
        print('Stop')
    elif button_pin == btn_black_top_pin:
        # Change direction
        L298.breakTheLoop('1')
        L298.breakTheLoop('0')
        tracking = 0
        
        if direction == 1:
            direction = 0
        else:
            direction = 1
        
        L298.updateSteps(-1)
        t = threading.Thread(target=L298.halfStepDriveMotor,args=(0,direction))
        t.start()
        tracking = 1
        

#GPIO inputs
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

#Main loop
while True:
    
    lcd.set_cursor_position(6,0)
    if tracking == 1:
        lcd.write("Running")
    else:
        lcd.write("Stopped")
        
    lcd.set_cursor_position(7,1)
    lcd.write("{:.4f}".format(delay))
    
    lcd.set_cursor_position(5,2)
    if direction == 1:
        lcd.write("Forward")
    else:
        lcd.write("Reverse")
    
    
    
        #print('Drive 0, 1')
        
        #tracking = 1
        
    
    #print('End Loop')
    #time.sleep(10)
    
    #print('error')
