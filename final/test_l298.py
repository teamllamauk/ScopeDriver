import time
import functions_l298

L298 = functions_l298.functions_l298('0.0055', '10')

while True:
    print('Drive 0, 0')
    L298.driveMotor(0, 0)
    time.sleep(2)
    
    print('Drive 0, 1')
    L298.driveMotor(0, 1)
    time.sleep(2)
    
    print('Drive 1, 0')
    L298.driveMotor(1, 0)
    time.sleep(2)
    
    print('Drive 1, 1')
    L298.driveMotor(1, 1)
    time.sleep(2)
