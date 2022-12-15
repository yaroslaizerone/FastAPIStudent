import json


with open('student.json') as json_file:
    data: dict = json.load(json_file)

data_students = data.get("students")
data_groups = data.get("groups")


def save_dict_to_json():
    with open('student.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)