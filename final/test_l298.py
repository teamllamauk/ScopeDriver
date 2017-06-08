import time
import functions_l298

L298 = functions_l298.functions_l298('0.0055', '40')
L298.setupGPIO(17, 18, 22, 23, 1, 5, 6, 13)

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
    
    print('Half Drive 0, 0')
    L298.halfStepDriveMotor(0, 0)
    time.sleep(2)
    
    print('Half Drive 0, 1')
    L298.halfStepDriveMotor(0, 1)
    time.sleep(2)
    
    print('Half Drive 1, 0')
    L298.halfStepDriveMotor(1, 0)
    time.sleep(2)
    
    print('Half Drive 1, 0')
    L298.halfStepDriveMotor(1, 0)
    time.sleep(2)
