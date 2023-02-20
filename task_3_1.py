num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
num3 = int(input('Введите 3-е число: '))


def my_func(arg1, arg2, arg3):
    if arg1 < arg2:
        return arg2 + arg3
    elif arg2 < arg1:
        return arg1 + arg3
    else:
        return arg1 + arg2


print(f'сумма наибольших двух чисел: {my_func(num1, num2, num3)}')
