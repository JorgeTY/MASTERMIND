from random import randint
import os
vida_inicial_pikachu = 80
vida_inicial_squirtle = 90
vida_pikachu = 80
vida_squirtle = 90
TAMANO_BARRA = 20

while vida_pikachu > 0 and vida_squirtle > 0:

    print("Turno de pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con impactrueno")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con impactrueno")
        vida_squirtle -= 11

    vida_pikachu = max(0 , vida_pikachu)
    vida_squirtle = max(0 , vida_squirtle)
    barras_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA / vida_inicial_pikachu)
    print("pikachu:   [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANO_BARRA - barras_de_vida_pikachu),
                                             vida_pikachu, vida_inicial_pikachu))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA / vida_inicial_squirtle)
    print("Squirtle:  [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANO_BARRA - barras_de_vida_squirtle),
                                             vida_squirtle, vida_inicial_squirtle))



    input("Enter para continuar.... \n\n")
    os.system("cls")

    print("Turno de squirtle")

    ataque_squirtle = None
    while ataque_squirtle not in ['p', 'a', 'b', 'n']:
        ataque_squirtle = input("Que ataque deseas realizar? (P)lacaje, Pistola (A)gua, (B)urbuja, (N)ada: ")

        if ataque_squirtle == 'p':
            print("Squirtle ataca con placaje")
            vida_pikachu -= 10
        elif ataque_squirtle == 'a':
            print("Squirtle ataca con Pistola de Agua")
            vida_pikachu -= 12
        elif ataque_squirtle == 'b':
            print("Squirtle ataca con Burbuja")
            vida_pikachu -= 9
        elif ataque_squirtle == 'n':
            print("Squirtle ataca con nada")
            vida_pikachu -= 0


    vida_pikachu = max(0, vida_pikachu)
    vida_squirtle = max(0, vida_squirtle)
    barras_de_vida_pikachu = int(vida_pikachu * TAMANO_BARRA / vida_inicial_pikachu)
    print("pikachu:   [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (TAMANO_BARRA - barras_de_vida_pikachu),
                                             vida_pikachu, vida_inicial_pikachu))

    barras_de_vida_squirtle = int(vida_squirtle * TAMANO_BARRA / vida_inicial_squirtle)
    print("Squirtle:  [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (TAMANO_BARRA - barras_de_vida_squirtle),
                                             vida_squirtle, vida_inicial_squirtle))

    input("Enter para continuar.... \n\n")
    os.system("cls")
if vida_pikachu > vida_squirtle:
    print("Pikachu GANA")
else:
    print("Squirtle GANA")
