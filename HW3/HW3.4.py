#for
chislo = int(input('Введите целое число:'))
sum = 0
for i in range(1, chislo+1):
    sum += i**3
print('Сумма чисел кубов от 1 до n равна', sum)   



#while
chislo = int(input('Введите целое число:'))
sum = 0
i = 1
while i <= chislo:
    sum += i**3
    i += 1
print('Сумма чисел кубов от 1 до n равно', sum)