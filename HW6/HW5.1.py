x = int(input('Введите число:'))
f = list(map(lambda x: x % 2 == 0, [x]))
if x % 2 == 0:
    print('Чётное')
else:
    print('Нечётное')