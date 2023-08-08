import random
guesses = 0
number = random.randint(1, 6)
while guesses < 3:
    guess = int(input('Введите число от 1 до 5:'))
    guesses += 1
    if guess < number:
        print('Это не то число(')
    if guess > number:
        print('Это число выше загадонного')
    if guess == number:
        break
if guess == number:
    print('Ты попал)))')
else:
    print ('Блииин, Я загадал число {0}'.format(number))