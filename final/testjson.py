import sys
import os
import json

data = {}
data['settings'] = []
data['settings'].append({'speed': 0.0012})

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
