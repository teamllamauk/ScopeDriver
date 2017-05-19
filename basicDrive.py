#!/usr/bin/env python
# coding: Latin-1

#pre-req : sudo apt-get -y install joystick
#pre-req : jstest /dev/input/js0

# Button 0: X
# Button 1: A
# Button 2: B
# Button 3: Y
# Button 4: L
# Button 5: R

# Button 8: Select
# Button 9: Start


# Load library functions we want
import time
import threading
import pygame
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

delay = 0.0055
steps = 10

# RA Motor Pins
RA_coil_A_1_pin = 17
RA_coil_A_2_pin = 18
RA_coil_B_1_pin = 22
RA_coil_B_2_pin = 23

# DEC Motor Pins
DEC_coil_A_1_pin = 8
DEC_coil_A_2_pin = 9
DEC_coil_B_1_pin = 10
DEC_coil_B_2_pin = 11

# Setup GPIO pins
GPIO.setup(RA_coil_A_1_pin, GPIO.OUT)
GPIO.setup(RA_coil_A_2_pin, GPIO.OUT)
GPIO.setup(RA_coil_B_1_pin, GPIO.OUT)
GPIO.setup(RA_coil_B_2_pin, GPIO.OUT)
GPIO.setup(DEC_coil_A_1_pin, GPIO.OUT)
GPIO.setup(DEC_coil_A_2_pin, GPIO.OUT)
GPIO.setup(DEC_coil_B_1_pin, GPIO.OUT)
GPIO.setup(DEC_coil_B_2_pin, GPIO.OUT)

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
global drivingUpDown
global drivingLeftRight
hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False
drivingUpDown = False
drivingLeftRight = False
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
            # print("Button {} on".format(button))
            
        elif event.type == pygame.JOYBUTTONUP:
            button = event.button
            # print("Button {} off".format(button))
            
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
            if upDown < -0.5: # Move Up (Dec)
                moveUp = True
                moveDown = False
            elif upDown > 0.5: # Move Down (Dec)
                moveUp = False
                moveDown = True
            else:
                moveUp = False
                moveDown = False
            
            print moveUp
            print moveDown
            
            # Determine Left / Right values
            if leftRight < -0.5: # Move Left (RA)
                moveLeft = True
                moveRight = False
            elif leftRight > 0.5: # Move Right (RA)
                moveLeft = False
                moveRight = True
            else:
                moveLeft = False
                moveRight = False

def driveMotor(motor, direction):
    if motor == 1:
        drivingUpDown = True
    else:
        drivingLeftRight = True
    
    if direction == 1: # Forward
        setStep(motor,1,0,1,0)
        time.sleep(delay)
        setStep(motor,0,1,1,0)
        time.sleep(delay)
        setStep(motor,0,1,0,1)
        time.sleep(delay)
        setStep(motor,1,0,0,1)
        time.sleep(delay)
    else: # Reverse
        setStep(motor,1,0,0,1)
        time.sleep(delay)
        setStep(motor,0,1,0,1)
        time.sleep(delay)
        setStep(motor,0,1,1,0)
        time.sleep(delay)
        setStep(motor,1,0,1,0)
        time.sleep(delay)
        
    if motor == 1:
        drivingUpDown = False
    else:
        drivingLeftRight = False

# Function for step sequence
def setStep(motor, w1, w2, w3, w4):
    if motor == 1: # Dec
        GPIO.output(DEC_coil_A_1_pin, w1)
        GPIO.output(DEC_coil_A_2_pin, w2)
        GPIO.output(DEC_coil_B_1_pin, w3)
        GPIO.output(DEC_coil_B_2_pin, w4)
    else: # RA
        GPIO.output(RA_coil_A_1_pin, w1)
        GPIO.output(RA_coil_A_2_pin, w2)
        GPIO.output(RA_coil_B_1_pin, w3)
        GPIO.output(RA_coil_B_2_pin, w4)
        
        
try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())                 
        # Wait for the interval period
        
        if moveUp == True and moveDown == False and drivingUpDown == False:
            #Drive motor Up (Dec)
            t = threading.Thread(target=driveMotor,args=(1,1))
            t.start()            
        elif moveUp == False and moveDown == True and drivingUpDown == False:
            #Drive motor Down (Dec)           
            t = threading.Thread(target=driveMotor,args=(1,0))
            t.start()
        #else:
            #Stop motor
            
            
        if moveLeft == True and moveRight == False and drivingLeftRight == False:
            #Drive motor Left (RA)
            t = threading.Thread(target=driveMotor,args=(0,1))
            t.start()
        elif moveLeft == False and moveRight == True and drivingLeftRight == False:
            #Drive motor Right (RA)
            t = threading.Thread(target=driveMotor,args=(0,0))
            t.start()
        #else:
            #Stop motor   
        
        time.sleep(interval)
except:        
    print 'Error'
