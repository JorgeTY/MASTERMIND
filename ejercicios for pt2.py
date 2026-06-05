


numeros = input('Introduzca los numeros separados por coma: ')
numerosusuario = [int (i) for i in numeros.split(',')]


pequeno = numerosusuario[0]
grande = numerosusuario[0]

print (numeros)

for i in numerosusuario:
    if i < pequeno:
        pequeno = i
    elif i > grande:
        grande = i

print('Grande: {}'.format(grande))
print('Pequeno: {}'.format(pequeno))