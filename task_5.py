from timeit import timeit

num1 = int(input('Введите 1-е число: '))
num2 = int(input('Введите 2-е число: '))
num3 = int(input('Введите 3-е число: '))


def my_func(arg1, arg2, arg3):
    lst = list()
    lst.append(arg1)
    lst.append(arg2)
    lst.append(arg3)
    lst.sort()
    return lst[1]+lst[2]


print(f'сумма наибольших двух чисел: {my_func(num1, num2, num3)}')
print(timeit('my_func', globals=globals(), number=1000000))