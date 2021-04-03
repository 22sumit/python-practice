import json

# load/loads: converts a file/string to a json object
# dump/dumps: converts a json object to a file/string

with open("..\\resources\\states.json") as f:
    data=json.load(f)

print(data)
for state in data['states']:
    print(state["name"],state["abbreviation"])

new_str=json.dumps(data, indent=2, sort_keys=True) #dumping the json to string format in python
print(new_str)

with open("..\\resources\\states_new.json", "w") as fnew:
    json.dump(data,fnew,indent=4)  #dumping json to a file in python