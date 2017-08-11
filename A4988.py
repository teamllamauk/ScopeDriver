import wiringpi2 as wiringpi
import time

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, 2)
wiringpi.pwmWrite(18, 500)

time.sleep(20)

wiringpi.pwmWrite(18, 0)
