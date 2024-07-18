def TareaListaInvitados():
    listinv = []

    def orderlist():
        listinv.sort()

    def dele():
        print(f"Escribe el nombre de la persona que quieres eliminar de la lista de invitados")
        elemento = input()
        try:
            listinv.remove(elemento)
        except ValueError: #Encaso de no encontrar el elemento que debe eliminar sin generar el corte de la ejecución
            print(f"La persona que quieres eliminar no se encuentra en la lista.\n")
        orderlist()


    def agnuevo():
        print(f"Escriba el nombre de la persona invitada para agregar a la lista")
        elemento = input()
        listinv.append(elemento)
        orderlist()


    def list_invitados():
        print(f"\nEsta tarea consta de un programa que le permita al usuario gestionar una lista de invitados a una fiesta utilizando una lista, este debe permitirle agregar, eliminar, mostrar y contrar los invitados de la lista.\n")
        
        print (f"Según la función que desee ejecutar digite el númeroa")
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


def MainHomeworks():
    
    option = 'a'
    while option != 'E':
        print (f"\n==========TAREAS CURSO UNICORN==========\n")
        print ("A. Tarea Lista de invitados") 
        print ("B. ")
        print ("C. ") 
        print ("D. ")
        print ("E. Salir")
        option = input().upper()
        if option == 'A':
            TareaListaInvitados()
        elif option == 'B':
            print("Holi")

MainHomeworks()