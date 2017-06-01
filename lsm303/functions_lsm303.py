import time
import math

import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303()

class functions_lsm303():
    
    def __init__(self):
        #set calibration values
        self.mag_Xmin = -767
        self.mag_Xmax = 886    
        self.mag_Ymin = -556
        self.mag_Ymax = 1013    
        self.mag_Zmin = -1018
        self.mag_Zmax = 670
        
        self.acc_Xmin = -1290
        self.acc_Xmax = 1010    
        self.acc_Ymin = -1306
        self.acc_Ymax = 1173    
        self.acc_Zmin = -1017
        self.acc_Zmax = 1217
    
    def bearing(self):
        
        self.acc, self.mag = lsm303.read()
        
        self.acc_X, self.acc_Y, self.acc_Z = self.acc
        self.mag_X, self.mag_Z, self.mag_Y = self.mag
        
        self.acc_Xnorm = self.acc_X / math.sqrt(self.acc_X * self.acc_X + self.acc_Y * self.acc_Y + self.acc_Z * self.acc_Z)
        self.acc_Ynorm = self.acc_Y / math.sqrt(self.acc_X * self.acc_X + self.acc_Y * self.acc_Y + self.acc_Z * self.acc_Z)
        
        self.pitch = math.asin(self.acc_Xnorm)
        self.roll = -math.asin(self.acc_Ynorm / math.cos(self.pitch))
        
        #self.mag_Xcal = (self.mag_X - self.mag_Xmin) / (self.mag_Xmax - self.mag_Xmin) * 2 - 1
        #self.mag_Ycal = (self.mag_Y - self.mag_Ymin) / (self.mag_Ymax - self.mag_Ymin) * 2 - 1
        #self.mag_Zcal = (self.mag_Z - self.mag_Zmin) / (self.mag_Zmax - self.mag_Zmin) * 2 - 1
        
        self.mag_Xcal = self.mag_X
        self.mag_Ycal = self.mag_Y
        self.mag_Zcal = self.mag_Z
        
        self.mag_Xtilt = self.mag_Xcal * math.cos(self.pitch) + self.mag_Zcal * math.sin(self.pitch)
        self.mag_Ytilt = self.mag_Xcal * math.sin(self.roll) * math.sin(self.pitch) + self.mag_Ycal * math.cos(self.roll) - self.mag_Zcal * math.sin(self.roll) * math.cos(self.pitch)
        
        self.heading = (math.atan2(self.mag_Xtilt, self.mag_Ytilt) * 180) / math.pi
    
        if self.heading < 0:
            self.heading = 360 + self.heading
        
        return self.heading
    
    def inclination(self):
        
        self.acc, self.mag = lsm303.read()
        
        self.acc_X, self.acc_Y, self.acc_Z = self.acc
                        
        self.tiltA = (math.atan2(self.acc_X, self.acc_Y) * 180) / math.pi
        self.tiltB = (math.atan2(self.acc_X, self.acc_Z) * 180) / math.pi
        self.tiltC = (math.atan2(self.acc_Y, self.acc_Z) * 180) / math.pi
        
        self.tilt = self.tiltA
        
        return self.tilt
