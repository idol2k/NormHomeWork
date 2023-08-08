# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print([b for b in a if b < 5])


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print([spisok for spisok in a if spisok in b])

# a, b, c = [1, 2, 3]
# print(a is b is c)

# print('!{p} ! {x}!'.format(p='Привет ', x='Юный падаван'))

# p = 'Привет тебе'
# x = 'Юный падаван'

# print(f'!{p} ! {x}!') 

# Тоже саммое что и снизу но короче
# num = [4, 4, 3, 4, 1, 3, 2]

# def count_num(a):
#     my_dict = {i:num.count(i) for i in num}
#     print(my_dict)
# count_num(num)

# Сколько чисел определенного значения в списке
# num = [4, 1, 4, 3, 2, 3, 1, 2, 4]

# def count_num(num):
#     result_dict = {}
#     for i in num:
#         result = num.count(i)
#         result_dict[i] = result
#     print(result_dict.get(4, 'Elementa Nima'))
# count_num(num)


# Каждое число в массиве возвести в корень
# num_list = [3, 4, 5, 54, 64, 23, 89]
# vivod = {i ** 0.5 for i in num_list}
# print(vivod)


# def new_func(a, b, c):
#     return a + b / c
# print(new_func(1, 14, 2))

# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» до величины «end» включительно. 
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.
# def sum_range(start, end):
#     if end < start:
#         end, start = start, end
#     return sum(range(start, end + 1))
# print(sum_range(1, 12))    
# print(sum_range(5, 16))



# import math
# AB = input('Введите 1-ю длинну катета:')
# BC = input('Введите 2-ю длинну катета:')
# AB = float(AB)
# BC = float(BC)
# AC = math.sqrt((AB ** 2) + (BC ** 2))
# perimetr = AB + BC + AC
# ploshad = (AB + BC) / 2
# print(perimetr)
# print(ploshad)


# cup = [1, 2, 3, 4]
# f = list(map(lambda x: x**2, cup))
# print(f)


# f = list(map(lambda x, y: (x*x)**y, [2,2,3,4], [2, 4, 5, 6]))
# print(f)

# 1 вариант
# def funt(x):
#     if x % 2 == 0:
#         return True
#     return False
# print(list(filter(funt, [54, 3, 26, 1])))

# 2-ой вариант сжатый
# print(list(filter(lambda x: x % 2 == 0 ,[4, 2, 55, 4, 32])))


# from functools import reduce
# result = reduce(lambda a, x: a + x**2, [1, 2, 3], 0)
# print(result)

# from functools import reduce
# result = reduce(lambda x, y: x + y, [2,3,5], 5)
# print(result)

# res = [1, 2, 3, 4, 5]
# """Функция map которая увеличиват число на 10 
# и умножает результат на 2
# """
# print(list(map(lambda x: (x + 10) * 2, res))) 


# res = [-1, 2, -3, -4, 5, 6, -7, -8, -9, 10]
# def fn(x):
#     if(x < 0):
#         return fn
# minus = filter(fn, res)
# print(list(minus))


# def code_1(res):
#     if(res < 0):
#         return code_1
# new_res = filter(code_1, res)
# print(list(new_res))



import json
