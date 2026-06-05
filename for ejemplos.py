vocales = ['a','e,', 'i', 'o', 'u']

frase = 'hola, hoy estoy aprendiendo for y python'
print(frase)
encontradas = 0

for letra in frase:
    if letra in vocales:
        print('He encontrado una "{}"'.format(letra))
        encontradas += 1

print('Vocales encontradas: {}'.format(encontradas))

#EJEMPLO DE REPETICIONES DE MENSAJE USANDO FOR


repeticiones = int(input('Cuantas veces queires repetir el mensaje? '))

for a in range(repeticiones):
    print('hola')