import random
while True:
    print("Empiezas en una carcel del salvaje oeste. El sheriff se acerca a ti  "
          "y tienes la posibilidad de agarrarlo para noquearlo y quitarle las llaves")

    plus=0
    opcion = input("Intentamos quitarle las llaves?")
    if opcion == "no":
        print(".-. \nEntonces te pudres en la carcel por tibio")
    elif opcion == "si":
        dificultad = 4
        print(f"La dificultad para noquear al sheriff es {dificultad}")
        suerte = random.randint(1,10)
        print(f"Tu atacas con un nivel de  {suerte}")
        if suerte <= dificultad:
            print("El sheriff se te solto y te disparo por idiota \n FIN")
        elif suerte > dificultad:
            print("Lo noqueas y agarras sus llaves para liberarte. "
                  "\n Ves que tiene un estuche en su bolsillo con algo misterioso \n")
            estuche = input("Agarras el estuche?")
            if estuche == "si":
                plus = 2
            print("Ya fuera de la celda, tienes 2 opciones. Ir por la puerta o la ventana \n")
            opcion = input("Eliges la puerta o la ventana?")
            if opcion == "puerta":
                print("Sales y hay un monton de policias y disparan sin dudar. "
                      "\n Mueres sin posibilidad de defenderte \n FIN")
            elif opcion == "ventana":
                print("Vas por la parte trasera y sales de la ciudad pero a las afueras"
                      "\n encuentras a un policia patrullando y trata de detenerte")
                if estuche == "si":
                    print("Abres el estuche y encuentras un revolver. "
                          "\n eso te ayuda al enfrentamiento")
                dificultad = 6
                suerte = random.randint(1,10) + plus
                print(f"Tu atacas con un nivel de  {suerte}")
                print(f"El enemigo ataca con una dificultad de {dificultad}")
                if suerte < dificultad:
                    print("El policia ataca y te elimina. Casi llegas al final \n FIN")
                elif suerte > dificultad:
                    print("Logras detenerlo y sigues por la carretera caminando"
                          "\n De repente te encuetnras a Arthur Morgan a mitad de la nada"
                          "\n Arthur te ofrece un lugar en la banda de dutch si contestas"
                          "\n su pregunta matematica correctamente")
                    print("El pregunta cuanto es 10 por 15?")
                    numero = 150
                    respuesta = int(input("Cual es tu respuesta?"))
                    if respuesta != numero:
                        print("Arthur se burla en tu cara por lo idiota que eres y se va")
                        print("Llegas a un muella con un barco a punto de irse. Te estan buscando"
                              "\n Llegas con el guardia de la entrada y le pides por favor que"
                              "\n te dejen pasar. Tu no hiciste nada malo.")
                        dificultad = 9
                        suerte = random.randint(1,10)
                        print(f"Tu nivel de convencimiento tiene un nivel de  {suerte}")
                        print(f"El nivel de dificultad de convencerl al guardia es {dificultad}")
                        if suerte < dificultad:
                            print("El guardia le da igual, y te arresta. Casi escapas \n FIN")
                        else:
                            print("El guardia se apiada de ti y te deja pasar para que inicies una nueva vida en TAHITI \n FIN")
                    elif respuesta == numero:
                        print("Arthur te ofrece llevarte en su caballo y te da la bienvenida a la banda de Dutch. Flicidaste. Escapaste \n FIN")
    op = input('quieres hacer el programa de nuevo?')
    if op == "no":
        break




