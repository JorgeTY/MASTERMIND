titulo="Bienvenido al test sobre quesos"
print(titulo + '\n' + '-' * len(titulo) + '\n')
i=0
j=0

print('Cuanto te gusta el queso?')
puntuacion = 0
for i in range (3):
    if i == 0:
        opcion = input('Pregunta 1: Que haces cuando ves una tabla de quesos?'
            '\nA - Salgo corriendo'
            '\nB - Pruebo uno de los quesos o incluso varios'
            '\nC - No puedo evitar devolrarla\n')

        if opcion == 'A':
            puntuacion = puntuacion + 0
        elif opcion == 'B':
            puntuacion = puntuacion + 5
        elif opcion =='C':
            puntuacion = puntuacion + 10
        else:
            print('opcion invalida\n'      
                'Las opcions posibles son A, B y C')
            exit()
        print('La puntuacion actual es ', puntuacion)
    elif i == 1:
        opcion = input('Pregunta 2: Como te gusta la hamburguesa?'
            '\nA - Sin queso'
            '\nB - Con queso'
            '\nC - Pan y queso\n')

        if opcion == 'A':
            puntuacion = puntuacion + 0
        elif opcion == 'B':
            puntuacion = puntuacion + 5
        elif opcion =='C':
            puntuacion = puntuacion + 10
        else:
            print('opcion invalida\n'      
                'Las opcions posibles son A, B y C')
            exit()

        print('La puntuacion actual es ', puntuacion)

    elif i == 2:
        opcion = input('Pregunta 3: Eres intolerante a la lactosa?'
            '\nA - Si'
            '\nB - A veces'
            '\nC - Nunca\n')

        if opcion == 'A':
            puntuacion = puntuacion + 0
        elif opcion == 'B':
            puntuacion = puntuacion + 5
        elif opcion =='C':
            puntuacion = puntuacion + 10
        else:
            print('opcion invalida\n'      
                'Las opcions posibles son A, B y C')
            exit()
        print('La puntuacion actual es ', puntuacion)

if puntuacion >= 25:
    print('TE ENCANTA EL QUESO')
elif puntuacion >= 15:
    print('OK, MEDIO TE GUSTA EL QUESO')
else:
    print('NO TE GUSTA EL QUESO')
