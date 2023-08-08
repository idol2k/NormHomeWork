new_list = [1,2,3,4]
def funt():
    tre = list(map(lambda new_list: str(new_list), new_list))
    return tre
print(funt())