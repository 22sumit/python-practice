import json
# f=open("D:\\FrontlineEd\\emp0.json")
# r=f.read()
# print(r)

f=open("D:\\FrontlineEd\\emp0.json")
k=json.load(f)
print(k)
ids=k["data"]
for i in ids:
    print(i["id"] + "     " + i["type"] + "     " + i["attributes"]["name"])