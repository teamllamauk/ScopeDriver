
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

import time
import pygame

class functions_joypad():
    
    def __init__(self):

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
                    
        return (moveUp, moveDown, moveLeft, moveRight, button)
