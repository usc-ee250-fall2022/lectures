import sys
import json

json_file = open(sys.argv[1], "r")
json_text = json_file.read()

# Read in JSON and convert to Python dict
person = json.loads(json_text)
print(person)

# Update the data using Python object syntax
person["friends"].append("Michael")

# Convert back to JSON
new_json = json.dumps(person, indent=4)
print(new_json)
