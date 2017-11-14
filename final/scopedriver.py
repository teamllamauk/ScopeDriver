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

global RA_delay
global Dec_delay
global tracking
global RA_Direction  # forward = 1, reverse = 0
global Dec_Direction  # forward = 1, reverse = 0
global softwareMode
global JSON_settings
global Jog_Steps

JSON_ReadWrite = functions_ReadWriteJson.functions_ReadWriteJson()

JSON_settings = JSON_ReadWrite.readJSON()
RA_delay = JSON_settings['settings'][0]['speed'] # Step delay
Dec_delay = 0.001

running = 0
RA_Direction = 1
Dec_Direction = 1
softwareMode = 'displayMenu'
Jog_Steps = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup LCD
lcd.clear()
backlight.rgb(255, 0, 0)
lcd.set_contrast(50)

# Pin assignments
RA_Step_pin = 22
RA_Dir_pin = 27

DEC_Step_pin = 17
DEC_Dir_pin = 4


RAMotor = functions_A4988.functions_A4988(RA_delay, '1')
RAMotor.setupGPIO(RA_Step_pin, RA_Dir_pin)

DecMotor = functions_A4988.functions_A4988(Dec_delay, '1')
DecMotor.setupGPIO(DEC_Step_pin, DEC_Dir_pin)

# Button Layout
#
#       X                   Blue
#   Y       A           Green   Red
#       B                   Yellow
#

btn_red_pin = 26            # A
btn_green_pin = 19          # Y
btn_blue_pin = 13            # X
btn_yellow_pin = 6         # B
btn_black_top_pin = 5      # purple wire
btn_black_bottom_pin = 9   # grey wire

def setSoftwareMode(newMode):
    global softwareMode
    lcd.clear()
    softwareMode = newMode    

def changeStepCount():
    global Jog_Steps
    
    if Jog_Steps == 1:
        Jog_Steps = 10
    elif Jog_Steps == 10:
        Jog_Steps = 50
    elif Jog_Steps == 50:
        Jog_Steps = 100
    else:
        Jog_Steps = 1
    
def exitProg():
    global softwareMode
    softwareMode = ""
    # Do exit and shutdown system
    print("Shutting Down in 5...")
    lcd.clear()
    backlight.off()
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    call("sudo shutdown -h now", shell=True)

# Button Press Callback Function
def btn_Callback(button_pin):
    global softwareMode     
    global RA_delay
    global running
    global RA_Direction
    global Dec_Direction
    global JSON_settings
    global Jog_Steps

    # print('btn callback - %s', button_pin)

    if button_pin == btn_blue_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet
        elif softwareMode == 'manual':
            print('Jog Dec+')
            DecMotor.updateDelay(Dec_delay)
            DecMotor.updateSteps(Jog_Steps)
            DecMotor.motorDirection(Dec_Direction)
            DecMotor.driveMotor()    
        elif softwareMode == 'tracking':
            print('Jog Dec+')
            DecMotor.updateDelay(Dec_delay)
            DecMotor.updateSteps(Jog_Steps)
            DecMotor.motorDirection(Dec_Direction)
            DecMotor.driveMotor()   
        elif softwareMode == 'checkSpeed':
            # Slow Down
            RA_delay = RA_delay + 0.0001
            RAMotor.updateDelay(RA_delay)

    elif button_pin == btn_yellow_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet    
        elif softwareMode == 'manual':
            print('Jog Dec-')
            DecMotor.updateDelay(Dec_delay)
            DecMotor.updateSteps(Jog_Steps)
            if Dec_Direction == 0:
                DecMotor.motorDirection(1)
            else:
                DecMotor.motorDirection(0)
            DecMotor.driveMotor()    
        elif softwareMode == 'tracking':
            print('Jog Dec-')
            DecMotor.updateDelay(Dec_delay)
            DecMotor.updateSteps(Jog_Steps)
            if Dec_Direction == 0:
                DecMotor.motorDirection(1)
            else:
                DecMotor.motorDirection(0)
            DecMotor.driveMotor()    
        elif softwareMode == 'checkSpeed':
            # Speed Up
            RA_delay = RA_delay - 0.0001
            RAMotor.updateDelay(RA_delay)

    elif button_pin == btn_green_pin:
        JSON_settings = JSON_ReadWrite.readJSON()
        RA_delay = JSON_settings['settings'][0]['speed'] # Step delay
        
        if softwareMode == 'displayMenu':
            menu.select_option()
        elif softwareMode == 'manual':
            print('Jog RA+')
            RAMotor.updateDelay(RA_delay)
            RAMotor.updateSteps(Jog_Steps)
            RAMotor.motorDirection(RA_Direction)
            RAMotor.driveMotor()
        elif softwareMode == 'tracking':
            if running == 0:
                
                RAMotor.updateDelay(RA_delay)
                RAMotor.breakTheLoop('0')        
                RAMotor.updateSteps(-1) # Run non stop
                RAMotor.motorDirection(RA_Direction)
                
                t1 = threading.Thread(target=RAMotor.driveMotor)
                t1.start()
                
                running = 1
                print('Start Tracking')    
        elif softwareMode == 'checkSpeed':
            # Start
            if running == 0:                
                
                RAMotor.updateDelay(RA_delay)
                RAMotor.breakTheLoop('0')        
                RAMotor.updateSteps(-1) # Run non stop
                RAMotor.motorDirection(RA_Direction)
                
                t1 = threading.Thread(target=RAMotor.driveMotor)
                t1.start()
                
                running = 1
                print('Start')
                
    elif button_pin == btn_red_pin:
        if softwareMode == 'displayMenu':
            a = 1 # do nothing yet    
        elif softwareMode == 'manual':
            print('Jog RA-')
            RAMotor.updateDelay(RA_delay)
            RAMotor.updateSteps(Jog_Steps)
            if RA_Direction == 0:
                RAMotor.motorDirection(1)
            else:
                RAMotor.motorDirection(0)
            RAMotor.driveMotor()    
        elif softwareMode == 'tracking':
            running = 0
            RAMotor.breakTheLoop('1')
            print('Stop Tracking')
        elif softwareMode == 'checkSpeed':
            # Stop
            running = 0
            RAMotor.breakTheLoop('1')
             
            JSON_settings = JSON_ReadWrite.readJSON()
            JSON_settings['settings'][0]['speed'] = RA_delay            
            JSON_ReadWrite.writeJSON(JSON_settings)
            
            print('Stop')
            
    elif button_pin == btn_black_top_pin:
        if softwareMode == 'displayMenu':
            menu.up()
        elif softwareMode == 'manual':
            changeStepCount()                
        elif softwareMode == 'tracking':
            a = 1 # do nothing yet    
        elif softwareMode == 'checkSpeed':
            # Change direction
            if RA_Direction == 1:
                RA_Direction = 0
            else:
                RA_Direction = 1

            RAMotor.motorDirection(RA_Direction)
            #L298Motor2.motorDirection(direction)
            
    elif button_pin == btn_black_bottom_pin:
        if softwareMode == 'displayMenu':
            menu.down()
        else:
            setSoftwareMode('displayMenu')    

# GPIO inputs
GPIO.setup(btn_red_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(btn_red_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_green_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(btn_green_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_blue_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(btn_blue_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_yellow_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(btn_yellow_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_black_top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(btn_black_top_pin, GPIO.RISING, callback=btn_Callback, bouncetime=300)

GPIO.setup(btn_black_bottom_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
        lcd.set_cursor_position(0, 0)
        lcd.write("Mode:     Manual")
        lcd.set_cursor_position(0, 1)
        lcd.write("Step Count: ")
        lcd.set_cursor_position(13, 1)
        if len(str(Jog_Steps)) == 1:
            lcd.write("00" + str(Jog_Steps))
        elif len(str(Jog_Steps)) == 2:
            lcd.write("0" + str(Jog_Steps))
        elif len(str(Jog_Steps)) == 3:
            lcd.write(str(Jog_Steps))
        lcd.set_cursor_position(0, 2)
        lcd.write("                ")
    elif softwareMode == 'tracking':
        lcd.set_cursor_position(0, 0)
        lcd.write("Mode:   Tracking")
        lcd.set_cursor_position(0, 1)
        lcd.write("Motor: ")
        lcd.set_cursor_position(9, 1)
        if running == 1:
            lcd.write("Running")
        else:
            lcd.write("Stopped")
        lcd.set_cursor_position(0, 2)
        lcd.write("                ")
            
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
        lcd.write("{:.4f}".format(RA_delay))

        lcd.set_cursor_position(9, 2)
        if RA_Direction == 1:
            lcd.write("Forward")
        else:
            lcd.write("Reverse")
        
    else:
        break
