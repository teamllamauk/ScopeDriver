import dothat.backlight as backlight
import dothat.lcd as lcd
from dot3k.menu import Menu, MenuOption
import RPi.GPIO as GPIO
import time
import threading
#import functions_l298
import functions_A4988
import functions_ReadWriteJson

from subprocess import call

global delay
global tracking
global direction  # forward = 1, reverse = 0
global softwareMode
global JSON_settings

JSON_ReadWrite = functions_ReadWriteJson.functions_ReadWriteJson()

delay = 0 # Step delay
running = 0
direction = 1
softwareMode = 'displayMenu'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LCD
lcd.clear()
backlight.rgb(255, 0, 0)

# Pin assignments
RA_Step_pin = 18
RA_Dir_pin = 17

DEC_A1_pin = 1
DEC_A2_pin = 5
DEC_B1_pin = 6
DEC_B2_pin = 13

RAMotor = functions_A4988.functions_A4988(delay, '1')
RAMotor.setupGPIO(RA_Step_pin, RA_Dir_pin)

#L298Motor2 = functions_l298.functions_l298(delay, '1')
#L298Motor2.setupGPIO(DEC_A1_pin, DEC_A2_pin, DEC_B1_pin, DEC_B2_pin)


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

def setSoftwareMode(newMode):
    global softwareMode
    lcd.clear()
    softwareMode = newMode    

def exitProg():
    global softwareMode
    softwareMode = ""
    # Do exit and shutdown system
    print("Shutting Down in 5...")
    lcd.clear()
    backlight.off()
    time.sleep(5)
    call("sudo shutdown -h now", shell=True)

# Button Press Callback Function
def btn_Callback(button_pin):
    global softwareMode     
    global delay
    global running
    global direction
    global JSON_settings

    # print('btn callback - %s', button_pin)

    if button_pin == btn_blue_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet
        elif softwareMode == 'manual':
            a = 1 # do nothing yet    
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet   
        elif softwareMode == 'checkSpeed':
            # Slow Down
            delay = delay + 0.0001
            RAMotor.updateDelay(delay)

    elif button_pin == btn_yellow_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet    
        elif softwareMode == 'manual':
            a = 1 # do nothing yet    
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet    
        elif softwareMode == 'checkSpeed':
            # Speed Up
            delay = delay - 0.0001
            RAMotor.updateDelay(delay)

    elif button_pin == btn_green_pin:
        if softwareMode == 'displayMenu':
            menu.select_option()
        elif softwareMode == 'manual':
            a = 1 # do nothing yet    
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet    
        elif softwareMode == 'checkSpeed':
            # Start
            if running == 0:
                JSON_settings = JSON_ReadWrite.readJSON()
                delay = JSON_settings["speed"]
                print("JSON Speed: ", delay)
                RAMotor.updateDelay(delay)
                RAMotor.breakTheLoop('0')        
                RAMotor.updateSteps(-1) # Run non stop
                RAMotor.motorDirection(direction)
                t1 = threading.Thread(target=RAMotor.driveMotor)
                t1.start()
                #L298Motor2.breakTheLoop('0')
                #L298Motor2.updateSteps(-1)
                #L298Motor2.motorDirection(direction)
                #t2 = threading.Thread(target=L298Motor2.halfStepDriveMotor)
                #t2.start()
                running = 1
                print('Start')
    elif button_pin == btn_red_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet    
        elif softwareMode == 'manual':
            a = 1 # do nothing yet    
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet    
        elif softwareMode == 'checkSpeed':
            # Stop
            running = 0
            RAMotor.breakTheLoop('1')
            #L298Motor2.breakTheLoop('1')
            JSON_settings["speed"] = delay
            JSON_ReadWrite.writeJSON(JSON_settings)
            print('Stop')
    elif button_pin == btn_black_top_pin:
        if softwareMode == 'displayMenu':
            menu.up()
        elif softwareMode == 'manual':
            a = 1 # do nothing yet    
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet    
        elif softwareMode == 'checkSpeed':
            # Change direction
            if direction == 1:
                direction = 0
            else:
                direction = 1

            RAMotor.motorDirection(direction)
            #L298Motor2.motorDirection(direction)
    elif button_pin == btn_black_bottom_pin:
        if softwareMode == 'displayMenu':
            menu.down()
        elif softwareMode == 'manual':
            setSoftwareMode('displayMenu')
        elif softwareMode == 'tracking':
            setSoftwareMode('displayMenu')   
        elif softwareMode == 'checkSpeed':
            setSoftwareMode('displayMenu')
    

# GPIO inputs
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

# Menu Structure
menu = Menu(
    structure={
        'Exit': lambda: exitProg(),
        'Tracking': lambda: setSoftwareMode('tracking'),
        'Manual': lambda: setSoftwareMode('manual'),
        'Check Speed': lambda: setSoftwareMode('checkSpeed')        
    },
    lcd=lcd
    )

# Main loop
while True:
        
    if softwareMode == 'displayMenu':
        menu.redraw()
        time.sleep(0.05)
    elif softwareMode == 'manual':
        a = 1 # do nothing yet
    elif softwareMode == 'tracking':
        a = 1 # do nothing yet        
    elif softwareMode == 'checkSpeed':       
        lcd.set_cursor_position(0, 0)
        lcd.write("Mode: ")
        lcd.set_cursor_position(0, 1)
        lcd.write("Delay: ")
        lcd.set_cursor_position(0, 2)
        lcd.write("Dir: ")
        
        lcd.set_cursor_position(9, 0)
        if running == 1:
            lcd.write("Running")
        else:
            lcd.write("Stopped")

        lcd.set_cursor_position(10, 1)
        lcd.write("{:.4f}".format(delay))

        lcd.set_cursor_position(9, 2)
        if direction == 1:
            lcd.write("Forward")
        else:
            lcd.write("Reverse")
    else:
        break
