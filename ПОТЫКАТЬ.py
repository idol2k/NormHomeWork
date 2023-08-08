my_list = list(range(1, 13))
pustio_list = []
for x in my_list:
    if x % 2 !=0:
        continue
    if x % 10 == 0:
        break
    pustio_list.append(x**2)

print(pustio_list)
