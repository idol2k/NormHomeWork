number_dict = {'first': 1, 'second': 2, 'third': 3}
new_dict = {value: key for key, value in number_dict.items()}
print(new_dict)