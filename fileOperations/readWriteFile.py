import json

f=open("..\\resources\\emp0.json")
k=json.load(f)
print(k)
ids=k["data"]
for i in ids:
    print(i["id"] + "     " + i["type"] + "     " + i["attributes"]["name"])

f.close()