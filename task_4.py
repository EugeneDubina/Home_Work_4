x = int(input('Введите действительное положительное число х: '))
y = int(input('Введите целое отрицательное число у: '))

if x > 0 > y:
    def my_func(x, y):
        if x > 0 and y < 0:
            res = 1
            y_new = -y
            while y_new > 0:
                res = res * 1/x
                y_new = y_new - 1
            return res

    print(my_func(x, y))

else:
    print(f'Введены значения согласно условию')