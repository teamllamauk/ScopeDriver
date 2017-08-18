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

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, 0)

#stepTime = 0.05
stepTime = 0.05
delay = stepTime / 2
count = 0

print(delay)

while True:
    
    GPIO.output(18, 1)    
    time.sleep(delay)
    GPIO.output(18, 0)
    time.sleep(delay)
    
    count = count + 1
    
    print(count)
    
    if count == 20:
        break
