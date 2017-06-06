L298 = functions_l298.functions_l298('0.0055', '10')



while True:

    L298.driveMotor('0', '0')
    time.sleep(1000)
    
    L298.driveMotor('0', '1')
    time.sleep(1000)
    
    L298.driveMotor('1', '0')
    time.sleep(1000)
    
    L298.driveMotor('1', '1')
    time.sleep(1000)
