import json
aDict = { 'Alice': 61, 'Bob': 62 }
f = open("static/grade.json", "w")
json.dump(aDict, f)
f.close()

f = open("static/grade.json", "r")
bDict = json.load(f)
f.close()
print(bDict)