


print('LISTA DE COMPRA')

inputa = None

lista = []

while inputa not in ['Q']:
    inputa = input('Que desea comprar? [Q para salir]: ')
    if  inputa == 'Q':
        pass

    elif inputa in lista:
        print(inputa, 'Ya esta en la lista de la compra')

    else:
        lista.append(inputa)

print('La lista de compra es:', lista)




