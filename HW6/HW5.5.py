def perevod(vvedi_stroku):
    if vvedi_stroku.lstrip('-').replace('.', '', 1).isdigit():
        if '.' in vvedi_stroku:
            perevernotye_number = float(vvedi_stroku)
            if vvedi_stroku.startswith('-'):
                return f"Вы ввели отрицательное дробное число: {perevernotye_number}"
            else:
                return f"Вы ввели положительное дробное число: {perevernotye_number}"
        else:
            perevernotye_number = int(vvedi_stroku)
            if vvedi_stroku.startswith('-'):
                return f"Вы ввели отрицательное целое число: {perevernotye_number}"
            else:
                return f"Вы ввели положительное целое число: {perevernotye_number}"
    else:
        return f"Вы ввели некорректное число: {vvedi_stroku}"


print(perevod("-6.3")) 
print(perevod("6")) 
print(perevod("1.2rg"))
print(perevod("-.444")) 