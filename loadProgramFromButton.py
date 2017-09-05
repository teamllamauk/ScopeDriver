# Program to load scope driver on button press

# Install instructions
# sudo crontab -e
# add: @reboot sudo python /home/pi/ScopeDriver/loadProgramFromButton.py > /home/pi/ScopeDriver/log.txt
# save and exit
# will load on reboot
# if problems check: grep crom /var/log/syslog

import dothat.backlight as backlight
import dothat.lcd as lcd
import RPi.GPIO as GPIO
import subprocess
import fcntl
import socket
import struct

def get_addr(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return 'Not Found!'

GPIO.setmode(GPIO.BCM)  

lcd.clear()
backlight.rgb(0, 255, 0)

lcd.set_cursor_position(0, 0)
lcd.write("Ready...")

lcd.set_cursor_position(0, 1)
lcd.write("Top Blk btn")

lcd.set_cursor_position(0, 2)
lcd.write(get_addr('wlan0'))

btn_black_top_pin = 16

GPIO.setup(btn_black_top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 
#try:  
GPIO.wait_for_edge(btn_black_top_pin, GPIO.FALLING)
print("Button Pressed")
subprocess.call(["sudo", "python", "/home/pi/ScopeDriver/final/scopedriver.py"])
# except KeyboardInterrupt:  
#    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  
