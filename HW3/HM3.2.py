while True:
    name = input('Введите свое имя:')
    vozrast = int(input('Введите свой возраст:'))
    if vozrast <= 0 or type(vozrast) != int:
        print('Ошибка, повторите ввод')
    elif 0 < vozrast < 10:
        print(f'Привет, шкет {name}!')
    elif 10 <= vozrast <= 18:
        print(f'Как жизнь {name}?')
    elif 18 < vozrast < 100:
        print(f'Что желаете, {name}?')
    else:
        print(f'{name}, вы лжете - в наше время столько не живут...')
        choice = input('Желаете продолжить? (Да/Нет):')
        if choice.lower() != 'Да':
            break