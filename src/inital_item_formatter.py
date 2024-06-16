# Script that helped format the JSON file into a more useful format for my project (Used only once and not required for this project)

# JSON Source:
# https://github.com/PrismarineJS/minecraft-data/blob/master/data/pc/1.8/items.json


import json

# Read the JSON file
with open('~/items/1.8.9.json') as file:
    data = json.load(file)

# Create a new dictionary with attribute name as key name
formatted_data = {item['name']: item for item in data}

# Remove the 'name' key from each item in the formatted data
for item in formatted_data.values():
    del item['name']
    
# Write the formatted data back to the JSON file
with open('/home/ninja/Minecraft-API/items/1.8.9.json', 'w') as file:
    json.dump(formatted_data, file, indent=4)
