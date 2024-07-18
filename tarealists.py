listinv = []

def orderlist():
    global listinv
    listinv.sort()

def dele():
    print(f"Escribe el nombre de la persona que quieres eliminar de la lista de invitados")
    elemento = input()
    try:
        listinv.remove(elemento)
    except ValueError:
        print(F"La persona que quieres eliminar no se encuentra en la lista.\n")
    orderlist()


def agnuevo():
    print(f"Escriba el nombre de la persona invitada para agregar a la lista")
    elemento = input()
    listinv.append(elemento)
    orderlist()


def list_invitados():
    
    print (f"Según la función que desee ejecutar digite el número")
    print
    opt = 'a'
    while opt != 'E':
        print ("A. Agregar un nuevo invitado a la lista") 
        print ("B. Eliminar un invitado de la lista")
        print ("C. Mostrar la lista de invitados") 
        print ("D. Mostrar la cantidad de invitados en la lista")
        print ("E. Salir")
        opt = input().upper()

        if opt == 'A':
            agnuevo()
        elif opt == 'B':
            dele()
        elif opt == 'C':
            print("==========LISTA DE INVITADOS===========\n")
            for invitado in listinv:
                print(f"- {invitado}")
        elif opt == 'D':
            print(f"La lista tiene un total de {len(listinv)} invitados.\n")

list_invitados()