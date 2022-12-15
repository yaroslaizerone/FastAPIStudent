import json


with open('groups.json') as json_file:
    data: dict = json.load(json_file)

data_groups = data.get("groups")


def save_dict_to_json():

    with open('groups.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)