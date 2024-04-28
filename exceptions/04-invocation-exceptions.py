def division(n = 0):

    if n == 0:
        raise ZeroDivisionError('I cant divide for zero', f'{n}')
    return 5 / n
try:
    division()
except ZeroDivisionError as e:
    print(e)