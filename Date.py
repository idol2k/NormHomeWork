def date(day, month, year):
    if (0 < day <= 31) and (0 < month <= 12) and (0 < year <= 2023):
        return True 
    else:
        return False
print(date(11, 12, 2003))