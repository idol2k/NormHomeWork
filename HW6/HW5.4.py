import time

res = [2, 5, 4, 7, 4, -5, -1, 3, 2]

def decorator(func):
    def wrapper(res):
        a = time.time()
        func(res)
        b = time.time() - a
        print(b)
    return wrapper



@decorator
def code(res):
     result = list(map(lambda x:(x+5)**2, res))
     print(result)


code(res)


@decorator
def count_num(res):
    result_dict = {}
    for i in res:
        result = res.count(i)
        result_dict[i] = result
    print(result_dict.get(2, 'Elementa Nima'))
count_num(res)
