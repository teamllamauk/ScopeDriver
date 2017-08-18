import time
import RPi.GPIO as GPIO

class functions_A4988():

    def __init__(self, delay, steps):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.delay = float(delay)  # 0.0055
        self.steps = int(steps)  # 10
        self.breakLoop = 0  # 1 = escape from thread
        self.direction = 1  # Forward = 1, Reverse = 0
    
    def setupGPIO(self, pinStep, pinDir):
        # Motor Pins
        self.pin_Step = pinStep  # 18
        self.pin_Dir = pinDir  # 17        

        # Setup GPIO pins
        GPIO.setup(self.pin_Step, GPIO.OUT)
        GPIO.setup(self.pin_Dir, GPIO.OUT)
        
        GPIO.output(self.pin_Step, 0)
        GPIO.output(self.pin_Dir, 0)

    def updateDelay(self, delay):
        if self.delay > 1:
            self.delay = float(delay)

    def updateSteps(self, steps):
        self.steps = int(steps)

    def motorDirection(self, direction):
        self.direction = int(direction)
        if self.direction == 1:
            GPIO.output(self.pin_Dir, 1)
        else:
            GPIO.output(self.pin_Dir, 0)

    def breakTheLoop(self, breakloop):
        self.breakLoop = int(breakloop)

    def driveMotor(self):
        count = 0
        while True:
            
            GPIO.output(self.pin_Step, 1)    
            time.sleep(delay / 2)
            GPIO.output(self.pin_Step, 0)
            time.sleep(delay / 2)
            
            count = count + 1
            if count == self.steps:
                break

            if self.breakLoop == 1:
                self.breakLoop = 0
                break
            
