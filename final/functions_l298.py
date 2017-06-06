import time
import RPi.GPIO as GPIO


class functions_l298():
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        self.delay = 0.0055
        self.steps = 10
        
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
    
    def rawData(self):
        
        self.acc, self.mag = lsm303.read()
        
        return (self.acc, self.mag)
   
