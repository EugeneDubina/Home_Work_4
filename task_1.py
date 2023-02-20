def division(*args):

    try:
        arg1 = int(input("Введите числитель: "))
        arg2 = int(input("Введите знаменатель: "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Введите знаменатель отличный от 0"

    return res

print(f'{division()}')