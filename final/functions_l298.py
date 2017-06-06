import time
import math



class functions_l298():
    
    def __init__(self):
        #set init values
        
    
    def rawData(self):
        
        self.acc, self.mag = lsm303.read()
        
        return (self.acc, self.mag)
   
