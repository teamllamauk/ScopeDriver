import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

btn_red_pin = 26            # A
btn_green_pin = 19          # Y
btn_blue_pin = 13            # X
btn_yellow_pin = 6         # B
btn_black_top_pin = 5      # purple wire
btn_black_bottom_pin = 9   # grey wire


GPIO.setup(btn_red_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_green_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_blue_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_yellow_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_black_top_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_black_bottom_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Main loop
while True:
    if GPIO.input(btn_red_pin): 
        print "Red Button ON" 
    else:
        print "Red Button Off"
