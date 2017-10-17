import functions_ReadWriteJson

global JSON_settings

JSON_ReadWrite = functions_ReadWriteJson.functions_ReadWriteJson()

JSON_settings = JSON_ReadWrite.readJSON()
delayString = JSON_settings["speed"]
print("JSON Speed String: ", delayString)
delay = int(delayString)
print("JSON Speed Int: ", delay)
