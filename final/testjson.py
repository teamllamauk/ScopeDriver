import os
import json
  
import functions_ReadWriteJson

JSON_ReadWrite = functions_ReadWriteJson.functions_ReadWriteJson()

JSON_settings = JSON_ReadWrite.readJSON()
scope_Speed = JSON_settings['settings'][0]['speed']

print(scope_Speed)

JSON_settings['settings'][0]['speed'] = 0.017

scope_Speed = JSON_settings['settings'][0]['speed']
print(scope_Speed)
