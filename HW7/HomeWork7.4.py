import csv
import json

json_file = "file.json"

phonenumber = {"Alice": "375447652398",
               "Vadim": "375290567821",
               "Alexander": "375446784523",
               "Ignat": "375445821069",
               "Nikita": "375333445676",
               "Egor": "375445932787"
}

with open(json_file, "r") as my_file:
    data_dict = json.load(my_file)

csv_file = "data.csv"
with open(csv_file, "w", newline='') as my_csv_file:
    fieldsname = ['id', 'name', 'age', 'phone']
    writer = csv.DictWriter(my_csv_file, fieldnames=fieldsname)
    writer.writeheader()
    for number_id, (name, age), in data_dict.items():
        phone = phonenumber.get(name, "")
        writer.writerow({'id': number_id, 'name': name, 'age': age, 'phone': phone})