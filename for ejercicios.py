
#Debe haber un for que cuente los espacios, puntos y comas ALV


import string

puntuacion = ['.', ',', ' ']
puntos_encontradas = 0
comas_encontradas = 0
espacios_encontradas = 0
mayusculas_encontradas = 0
texto_user = input('Ingresa el texto: ')
print(texto_user)

for letra in texto_user:
    if letra in puntuacion:
        if letra == '.':
            print('He encontrado una {}'.format(letra))
            puntos_encontradas += 1
        elif letra == ',':
            print('He encontrado una {}'.format(letra))
            comas_encontradas += 1
        elif letra == ' ':
            print('He encontrado un espacio ')
            espacios_encontradas += 1
    elif letra in string.ascii_uppercase:
            print('He encontrado una mayuscula {}'.format(letra))
            mayusculas_encontradas += 1


print('Recuento de espacios [{}] puntos[{}]  comas[{}]   Mayusculas[{}]"'.format(
    espacios_encontradas,
    puntos_encontradas,
    comas_encontradas,
    mayusculas_encontradas))





