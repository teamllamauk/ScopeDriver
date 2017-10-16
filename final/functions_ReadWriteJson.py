import os
import json

class functions_ReadWriteJson():

    def __init__(self):
                
        settingsAbsPath =  os.path.abspath("ScopeSettings.json")
        
        try:
            settingsResolved = settingsAbsPath.resolve()
        except FileNotFoundError:
            data = {
                "speed":"0.0012"
            }
            jsonData = json.dumps(data)
            with open('JSONData.json', 'w') as f:
                json.dump(jsonData, f)

    def readJSON(self):
        with open('JSONData.json', 'r') as f:
            data = json.load(f)
            return (data)
    
    def writeJSON(self, data):
        jsonData = json.dumps(data)
        with open('JSONData.json', 'w') as f:
            json.dump(jsonData, f)
