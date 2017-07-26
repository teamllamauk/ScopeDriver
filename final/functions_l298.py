import time
import RPi.GPIO as GPIO

class functions_l298():
    
    def __init__(self, delay, steps):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.delay = float(delay) #0.0055
        self.steps = int(steps) #10
        self.breakLoop = 0 # 1 = escape from thread
        self.direction = 1 # Forward = 1, Reverse = 0

    def setupGPIO(self, pinA1, pinA2, pinB1, pinB2):
        
        # Motor Pins
        self.coil_A_1_pin = pinA1 #17
        self.coil_A_2_pin = pinA2 #18
        self.coil_B_1_pin = pinB1 #22
        self.coil_B_2_pin = pinB2 #23
        
        # Setup GPIO pins
        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)

    def updateDelay(self, delay):
        self.delay = float(delay)
    
    def updateSteps(self, steps):
        self.steps = int(steps)
    
    def motorDirection(self, direction):
        self.direction = int(direction)
    
    def breakTheLoop(self, breakloop):
        self.breakLoop = int(breakloop)
    
    
    #Full step sequence
    def driveMotor(self):
                
        count = 0
        while True :   
            if self.direction == 1: # Forward            
                self.setStep(1,0,1,0)
                time.sleep(self.delay)
                self.setStep(0,1,1,0)
                time.sleep(self.delay)
                self.setStep(0,1,0,1)
                time.sleep(self.delay)
                self.setStep(1,0,0,1)
                time.sleep(self.delay)               
            else: # Reverse            
                self.setStep(1,0,0,1)
                time.sleep(self.delay)
                self.setStep(0,1,0,1)
                time.sleep(self.delay)
                self.setStep(0,1,1,0)
                time.sleep(self.delay)
                self.setStep(1,0,1,0)
                time.sleep(self.delay)
                
            count = count + 1
            if count == self.steps:
                break
                
            if self.breakLoop == 1:
                self.breakLoop = 0
                break
                
            
    #Half step squence
    def halfStepDriveMotor(self):
        
        count = 0
        while True :
    
            if self.direction == 1: # Forward            
                self.setStep(1,0,0,0)
                time.sleep(self.delay)
                self.setStep(1,0,1,0)
                time.sleep(self.delay)
                self.setStep(0,0,1,0)
                time.sleep(self.delay)
                self.setStep(0,1,1,0)
                time.sleep(self.delay)
                self.setStep(0,1,0,0)
                time.sleep(self.delay)
                self.setStep(0,1,0,1)
                time.sleep(self.delay)
                self.setStep(0,0,0,1)
                time.sleep(self.delay)
                self.setStep(1,0,0,1)
                time.sleep(self.delay
            else: # Reverse
                self.setStep(1,0,0,1)
                time.sleep(self.delay)
                self.setStep(0,0,0,1)
                time.sleep(self.delay)
                self.setStep(0,1,0,1)
                time.sleep(self.delay)
                self.setStep(0,1,0,0)
                time.sleep(self.delay)
                self.setStep(0,1,1,0)
                time.sleep(self.delay)
                self.setStep(0,0,1,0)
                time.sleep(self.delay)
                self.setStep(1,0,1,0)
                time.sleep(self.delay)
                self.setStep(1,0,0,0)
                time.sleep(self.delay)
                
            count = count + 1
            if count == self.steps:
                break
                
            if self.breakLoop == 1:
                self.breakLoop = 0
                break

    # Function for step sequence
    def setStep(self, a1, a2, b1, b2):
    
        GPIO.output(self.coil_A_1_pin, a1)
        GPIO.output(self.coil_A_2_pin, a2)
        GPIO.output(self.coil_B_1_pin, b1)
        GPIO.output(self.coil_B_2_pin, b2)
