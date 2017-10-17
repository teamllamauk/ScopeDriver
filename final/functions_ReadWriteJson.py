import os
import json

class functions_ReadWriteJson():

    def __init__(self):
                
        settingsAbsPath =  os.path.abspath("ScopeSettings.json")
        
        if os.path.isfile('ScopeSettings.json'):
            print("Found file")
        else:
            print("File Not Found")
            
            data = {}
            data['settings'] = []
            data['settings'].append({'speed': 0.0012})            
            with open('ScopeSettings.json', 'w') as json_file:
                json.dump(data, json_file)

    def readJSON(self):
        with open('ScopeSettings.json', 'r') as json_file:
            data = json.load(json_file)            
            return (data)
    
    def writeJSON(self, data):        
        with open('ScopeSettings.json', 'w') as json_file:
            json.dump(data, json_file)
