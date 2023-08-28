isxod = b'r\xc3\xa9sum\xc3\xa9'
vivod = str(isxod.decode("UTF-8"))
new_vivod = vivod.encode("Latin1")
polniy_vivod = str(new_vivod.decode("Latin1"))
print(isxod)
print(vivod)
print(new_vivod)
print(polniy_vivod)