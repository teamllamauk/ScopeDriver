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
