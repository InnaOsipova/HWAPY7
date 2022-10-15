def calc ():
    x1 = float(input('Введите реальную часть первого комплексного числа: '))
    x2 = float(input('Введите мнимую часть первого комплексного числа, без j: '))
    y1 = float(input('Введите реальную часть второго комплексного числа: '))
    y2 = float(input('Введите мнимую часть  второгокомплексного числа, без j: '))
    x = complex(x1, x2)
    y = complex(y1, y2)
    choice_operation = input("Выбирите действие - сложение - s, вычитание- v, умножение - m, деление - d")
    if choice_operation == 's':
        rezult = x + y
        simbol = '+'
    elif choice_operation == 'v':
        rezult = x - y
        simbol = '-'
    elif choice_operation == 'm':
        rezult = x * y
        simbol = '*'
    elif choice_operation == 'd':
        rezult = x / y
        simbol = '/'
    print(f'{x} {simbol} {y} = {rezult}')
    return f'{x} {simbol} {y} = {rezult}'


