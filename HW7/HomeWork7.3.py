import json
dict = {123456: ("Alice", 21), 
        654321: ("Vadim", 19),
        213654: ("Alexander", 19),
        652431: ("Ignat", 19),
        946732: ("Nikita", 18),
        987675: ("Egor", 17)
}

json_file = "file.json"
with open(json_file, "w") as file:
    json.dump(dict, file, indent = 1)