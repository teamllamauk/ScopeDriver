import RPi.GPIO as GPIO
import time
import dothat.backlight as backlight
import dothat.lcd as lcd

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

delay = 0.0012

lcd.clear()

backlight.rgb(255, 0, 0)

lcd.set_cursor_position(0,0)
lcd.write("Delay")

lcd.set_cursor_position(0,1)
lcd.write(delay)

#lcd.set_cursor_position(0,2)
#lcd.write("Line 3")

coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 22
coil_B_2_pin = 23

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

while True:
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
