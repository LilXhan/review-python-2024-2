try:
    n1 = int(input('Enter a first number'))
except Exception as e:
    print('Error')
else:
    print('no ocurrio ningun error')


try:
    n1 = int(input('Enter a first number'))
except Exception as e:
    print('Error')
else:
    print('no ocurrio un error')
finally:
    print('se ejecuta siempre')