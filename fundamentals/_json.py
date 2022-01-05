import json

# person = {"name": "Mustafa", "languages": ["python", "C#", "Java"]}
# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

person_string = '{"name": "Mustafa", "languages": ["python", "C#", "Java"]}'

# Json string to Dict
# result = json.loads(person_string)

# print(type(result))
# print(result["name"])


# file close auto
# with open("person.json") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])


# dict to json
person_dict = {
    "name": "Mustafa",
    "languages": [
        "python",
        "C#",
        "Java"
    ]
}

# result = json.dumps(person_dict)
# print(result)
# print(type(result))


with open("person_2.json", "w") as f:
    json.dump(person_dict, f)



