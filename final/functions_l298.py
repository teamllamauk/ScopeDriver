import time
import RPi.GPIO as GPIO


class functions_l298():
    
    def __init__(self, delay, steps):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.delay = float(delay) #0.0055
        self.steps = int(steps) #10
        
        self.drivingUpDown = False
        self.drivingLeftRight = False
        
        # RA Motor Pins
        self.RA_coil_A_1_pin = 17
        self.RA_coil_A_2_pin = 18
        self.RA_coil_B_1_pin = 22
        self.RA_coil_B_2_pin = 23

        # DEC Motor Pins
        self.DEC_coil_A_1_pin = 1
        self.DEC_coil_A_2_pin = 5
        self.DEC_coil_B_1_pin = 6
        self.DEC_coil_B_2_pin = 13

        # Setup GPIO pins
        GPIO.setup(self.RA_coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.RA_coil_B_2_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.DEC_coil_B_2_pin, GPIO.OUT)
        
    def driveMotor(self, motor, direction):
               
        if motor == 1:
            self.drivingUpDown = True
        else:
            self.drivingLeftRight = True
    
        if direction == 1: # Forward
            for _ in range(self.steps):
                print('Loop 1')
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
        else: # Reverse
            for _ in range(self.steps):
                print('Loop 0')
                self.setStep(motor,1,0,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,0,1)
                time.sleep(self.delay)
                self.setStep(motor,0,1,1,0)
                time.sleep(self.delay)
                self.setStep(motor,1,0,1,0)
                time.sleep(self.delay)
        
        if motor == 1:
            self.drivingUpDown = False
        else:
            self.drivingLeftRight = False

    # Function for step sequence
    def setStep(self, motor, w1, w2, w3, w4):
        
        if motor == 1: # Dec
            GPIO.output(self.DEC_coil_A_1_pin, w1)
            GPIO.output(self.DEC_coil_A_2_pin, w2)
            GPIO.output(self.DEC_coil_B_1_pin, w3)
            GPIO.output(self.DEC_coil_B_2_pin, w4)
        else: # RA
            GPIO.output(self.RA_coil_A_1_pin, w1)
            GPIO.output(self.RA_coil_A_2_pin, w2)
            GPIO.output(self.RA_coil_B_1_pin, w3)
            GPIO.output(self.RA_coil_B_2_pin, w4)
    
  

