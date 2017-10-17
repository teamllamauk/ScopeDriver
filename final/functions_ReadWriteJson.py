import sys
import os
import json

class functions_ReadWriteJson():

    def __init__(self):
                
        settingsAbsPath =  os.path.abspath("ScopeSettings.json")
        
        try:
            settingsResolved = settingsAbsPath.resolve()
        except:
            print "Unexpected error:", sys.exc_info()[0]
            data = {
                "speed":"0.0012"
            }
            jsonData = json.dumps(data)
            with open('ScopeSettings.json', 'w') as f:
                json.dump(jsonData, f)

    def readJSON(self):
        with open('ScopeSettings.json', 'r') as f:
            rawData = f.readlines()
            data = json.loads(rawData)
            return (data)
    
    def writeJSON(self, data):
        jsonData = json.dumps(data)
        with open('ScopeSettings.json', 'w') as f:
            json.dump(jsonData, f)
