# Examples of reading and writing from a json file

import json

# Read from json

with open('JSONDate.json', 'r') as f:
    data = json.load(f)

print(data)


# Write to Json

data = {
    "FirstName":"Bhairav",
    "MiddleName":"S",
    "LastName":"Ram",
    "DateOfBirth":"09-01-1984",
    "Contact":{
        "Phone":9988776655,
        "Email":"bhairav@gmail.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":560056,
            "Street":"Nagarbhavi Road",
            "City":"Bangalore",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":560004,
            "Street":"Gandhi Bazaar Road",
            "City":"Bangalore",
            "Country":"India"
        }
    ]
}

# json.dumps() method turns a Python data structure into JSON
jsonData = json.dumps(data)
print(jsonData)

with open('JSONData.json', 'w') as f:
     json.dump(jsonData, f)
