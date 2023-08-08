
# 1-е Задание
con = [7, 2, 5]
a1 = con
a2 = con
a3 = con
print(a1)
print(a2)
print(a3)
print(id(a1))
print(id(a2))
print(id(a3))
# 2-е Задание
cin = [1, 2, 3]
a4 = tuple(cin)
a5 = tuple(cin)
print(a4)
print(a5)
print(id(a4))
print(id(a5))
# 3-е Задание
a1 = tuple(con)
a2 = tuple(con)
a3 = tuple(con)
a4 = cin
a5 = cin 
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(id(a1))
print(id(a2))
print(id(a3))
print(id(a4))
print(id(a5))
# 4-е Задание
couch = input("Введите произвольную строку:")
couch = couch.strip()
chetniy =couch[::2]
nechetniy = couch[1::2]
print("Введенная строка", couch)
print('\n\n')
print(chetniy, nechetniy, sep="     ", end='\n!!!\n')