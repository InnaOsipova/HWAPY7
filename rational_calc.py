from fractions import Fraction

def calc ():
    x1 = int(input('Введите числитель первого числа: '))
    x2 = int(input('Введите знаменатель первого числа: '))
    y1 = int(input('Введите числитель второго числа: '))
    y2 = int(input('Введите знаменатель второго числа: '))
    x = Fraction(x1, x2)
    y = Fraction(y1, y2)
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