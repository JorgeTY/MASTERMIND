


numero= int (input('Dame el numero pa darte las tablas de multiplicar: '))
opcion= input('Quieres que te den solo los resultados que son (M)ultiplos de 2 o nel?')

for i in range(1, 11):
    if opcion == 'm':

        n = numero * i
        if n % 2 == 0:
            print('Los resultados que son multiplos de 2 son: {} x {} = {}'.format(
                numero, i, n))
    else:

        n = numero * i
        print('Los resultados normales son: {} X {} = {}'.format(
            numero, i, n
        ))

