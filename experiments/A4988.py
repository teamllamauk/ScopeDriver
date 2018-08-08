# Useful links
# https://www.pololu.com/product/2128
# http://howtomechatronics.com/tutorials/arduino/how-to-control-stepper-motor-with-a4988-driver-and-arduino/
# Vref = 0.870v for 1.6A


#import wiringpi2 as wiringpi
#import time

#wiringpi.wiringPiSetupGpio()

#wiringpi.pinMode(18, 2)
#wiringpi.pwmSetMode(1)

#wiringpi.pwmWrite(18, 500)

#time.sleep(20)

#wiringpi.pwmWrite(18, 0)
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
pinStep = 22
pinDir = 27


GPIO.setup(pinStep, GPIO.OUT)
GPIO.output(pinStep, 0)

GPIO.setup(pinDir, GPIO.OUT)
GPIO.output(pinDir, 0)


#stepTime = 0.05
stepTime = 2
delay = stepTime / 2
count = 0
direction = 0

print(delay)

while True:
    
    GPIO.output(pinStep, 1)    
    time.sleep(delay)
    GPIO.output(pinStep, 0)
    time.sleep(delay)
    
    count = count + 1
    
    print(count)
    
    if count == 20 and direction == 0:
        count = 0
        direction = 1
        GPIO.output(pinDir, direction)
    else:
        break
