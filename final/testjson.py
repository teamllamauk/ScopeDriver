import sys
import os
import json

data = {}
data['settings'] = []
data['settings'].append({'speed': 0.0012})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)


with open('data.json') as json_file:
    data = json.load(json_file)
    print(data)
    print(data['settings'][0])
    print(data['settings'][0]['speed'])
    #for p in data['settings']:
    #    print(p['speed'])

    
if os.path.isfile('data.jsona'):
    print("True")
else:
    print("False")
