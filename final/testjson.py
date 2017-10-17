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
    for p in data['people']:
        print('speed: ' + p['speed'])
