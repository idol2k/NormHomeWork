class Calculator():

    @classmethod
    def sum(cls, a, b):
        return a + b

    @classmethod
    def subtrack(cls, a, b):
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        return a * b
    
    @classmethod
    def divide(cls, a, b):
        return a / b
    
OPERATORS_NUM = {
    "+":Calculator.sum,
     "-":Calculator.subtrack,
     "*":Calculator.multiply,
     "/":Calculator.divide
     }


try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    action = (input("Выберите действие (+,-,*,/): "))
    
    result = OPERATORS_NUM[action](x,y)
    print(result)
except ValueError as value:
    print (f"Вы ввели некорректное значение:{value}")

except KeyError as key:
    print (f"Вы ввели некорректное значение:{key}")

except ZeroDivisionError as zero:
    print (f"На ноль делить нельга:{zero}")

except EOFError as eof:
    print (f"На ноль делить нельга:{eof}")