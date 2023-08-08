import json 
data = {
    'Alice': 26, 
    'Bob': 23,
    'Gibson': 20
}
json_file_path = 'typo.json'
with open(json_file_path, 'w') as json_file:
    for name, age in data.items():
        new_data = {'name': name, 'age': age}
        json.dump(new_data, json_file)
        json_file.write('\n')

json_file_path = 'typo.json'
new_data_dict = {}
with open(json_file_path, 'r') as json_file:
    for line in json_file:
        new_data = json.loads(line)
        new_data_dict[new_data['name']] = new_data['age']
print(new_data_dict)