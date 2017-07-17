import dothat.backlight as backlight
import dothat.lcd as lcd
import RPi.GPIO as GPIO
import time
import pygame

lcd.clear()
backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write("Delay")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

delay = 0.0012
motor = 0

lcd.set_cursor_position(0,1)
lcd.write(str(delay))

lcd.set_cursor_position(0,2)
lcd.write("X inc - Y dec")

coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 22
coil_B_2_pin = 23

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)



# Settings for JoyBorg
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
interval = 0.1                          # Time between keyboard updates in seconds, smaller responds faster but uses more processor time

# Setup pygame and key states
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit
hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("JoyBorg - Press [ESC] to quit")

# Function to handle pygame events
def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    global moveQuit
    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = True
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_ESCAPE:
                moveQuit = False
        elif event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            if button == 0:
                delay = delay + 0.0001
            elif button == 3:
                delay = delay - 0.0001
                
        elif event.type == pygame.JOYBUTTONUP:
            button = event.button
            
        elif event.type == pygame.JOYAXISMOTION:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
                # Determine Up / Down values
                #if upDown < -0.5:
                #print 'Move Up'
                #elif upDown > 0.5:
                #print 'Move Down'          
                
                # Determine Left / Right values
                #if leftRight < -0.5:
                #print 'Move Left'
                #elif leftRight > 0.5:
                #print 'Move Right'  




def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

while True:
    PygameHandler(pygame.event.get())
    #lcd.set_cursor_position(0,1)
    #lcd.write(delay)
    setStep(motor,1,0,0,0)
    time.sleep(delay)
    setStep(motor,1,0,1,0)
    time.sleep(delay)
    setStep(motor,0,0,1,0)
    time.sleep(delay)
    setStep(motor,0,1,1,0)
    time.sleep(delay)
    setStep(motor,0,1,0,0)
    time.sleep(delay)
    setStep(motor,0,1,0,1)
    time.sleep(delay)
    setStep(motor,0,0,0,1)
    time.sleep(delay)
    setStep(motor,1,0,0,1)
    time.sleep(delay)
