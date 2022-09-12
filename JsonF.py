import json
new_countries = open("countries.json", "r")
lines = new_countries.read()
lines = lines[3:]
print(lines)
line = lines.replace("name:",'"name":').replace("code:",'"code":').replace("'",'"')
print(line)
str_dict=json.loads(line)
print(str_dict)

for item in str_dict:
    if item["name"].startswith("A"):
        print(item["name"])