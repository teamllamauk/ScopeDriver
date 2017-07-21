import time
import RPi.GPIO as GPIO

# Dec motor = 1
# RA motor = 0

# Forward = 1
# Reverse = 0

class functions_l298():
    
    def __init__(self, delay, steps):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.delay = float(delay) #0.0055
        self.steps = int(steps) #10
        self.breakLoop = 0


    def setupGPIO(self, raA1, raA2, raB1, raB2, decA1, decA2, decB1, decB2):
        
        # RA Motor Pins
        self.RA_coil_A_1_pin = raA1 #17
        self.RA_coil_A_2_pin = raA2 #18
        self.RA_coil_B_1_pin = raB1 #22
        self.RA_coil_B_2_pin = raB2 #23

        # DEC Motor Pins
        self.DEC_coil_A_1_pin = decA1 #1
        self.DEC_coil_A_2_pin = decA2 #5
        self.DEC_coil_B_1_pin = decB1 #6
        self.DEC_coil_B_2_pin = decB2 #13

        # Setup GPIO pins
        GPIO.setup(self.RA_coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_B_2_pin, GPIO.OUT)
        
        GPIO.setup(self.DEC_coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_B_2_pin, GPIO.OUT)

    def updateDelay(self, delay):
        
        self.delay = float(delay)
    
    def updateSteps(self, steps):
        
        self.steps = int(steps)
        
    def breakLoop(self, breakloop):
        
        self.breakLoop = int(breakloop)
    
    
    #Full step sequence
    def driveMotor(self, motor, direction):
           
        if direction == 1: # Forward
            count = 0
            while var == 1 :
                #print('Loop 1')
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
                
                count = count + 1
                if count = self.steps:
                    break
                
                if self.breakLoop = 1:
                    break
                               
                
        else: # Reverse
            count = 0
            while var == 1 :
                #print('Loop 0')
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
                
                count = count + 1
                if count = self.steps:
                    break
                
                if self.breakLoop = 1:
                    break
                
            
    #Half step squence
    def halfStepDriveMotor(self, motor, direction):
    
        if direction == 1: # Forward
            count = 0
            while var == 1 :
                #print('Loop 1')
                self.setStep(motor,1,0,0,0)
                time.sleep(self.delay)
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,0,0,1)
                time.sleep(self.delay)
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
                
                count = count + 1
                if count = self.steps:
                    break
                
                if self.breakLoop = 1:
                    break
                
        else: # Reverse
            for _ in range(self.steps):
                #print('Loop 0')
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,0,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,1,0,0,0)
                time.sleep(self.delay)
                
                count = count + 1
                if count = self.steps:
                    break
                
                if self.breakLoop = 1:
                    break
                


    # Function for step sequence
    def setStep(self, motor, w1, w2, w3, w4):
        
        if motor == 1: # Dec
            #print('Motor 1')
            GPIO.output(self.DEC_coil_A_1_pin, w1)
            GPIO.output(self.DEC_coil_A_2_pin, w2)
            GPIO.output(self.DEC_coil_B_1_pin, w3)
            GPIO.output(self.DEC_coil_B_2_pin, w4)
        else: # RA
            #print('Motor 0')
            GPIO.output(self.RA_coil_A_1_pin, w1)
            GPIO.output(self.RA_coil_A_2_pin, w2)
            GPIO.output(self.RA_coil_B_1_pin, w3)
            GPIO.output(self.RA_coil_B_2_pin, w4)
