import json

# json_data = '{"name": "Tom", "age": 30, "is_student": false}'
# parsed_data = json.loads(json_data)  # JSON-string to Python-object (dict)
#
# # print(parsed_data)
# # print(parsed_data,type(parsed_data))
# # print(parsed_data["name"])  #

"""example #2"""
json_data_another = {
    "name": "Tom",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "QA Automation", "API Testing"],
    "address": {
        "city": "London",
        "zip": "101000"
    }
}
json_string = json.dumps(json_data_another)
parsed_data_result=json.loads(json_string)
# print(parsed_data_result)
# print(parsed_data_result['courses'])


"""example #3"""
data = {
    "name": "Maria",
    "age": 25,
    "is_student": True
}

# json_string = json.dumps(data, indent=4)  # Python-object to JSON-string
json_string = json.dumps(data)
# print(json_string)


"""example #4"""
data = {
    "name": "Maria",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Python-object to JSON-string
# json_string = json.dumps(data)
# print(json_string)

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Download JSON from file
    # print(data)


"""example #5"""
data = {
    "name": "Maria",
    "age": 25,
    "is_student": True
}

json_string = json.dumps(data, indent=4)  # Python-object to JSON-string
print(json_string)

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)


