import os
import time

def lista_de_tareas_completadas():
    listado = open("completado.txt","r",encoding="utf-8")
    leer = listado.readlines()#conierve el contenido del archivo en una lista
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]
    #El contenido de la lista "leer" se imprimira linea por linea y seran enumerada por su posicion + 1
    print("".join(enumerada))
    listado.close()    

def lisitado_de_tareas():
    
    listado = open("pendientes.txt","r",encoding="utf-8")
    leer = listado.readlines()
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]
    print("".join(enumerada))
    listado.close()    
#muestra la informacion  estilo cascada y enumera cada tarea
def agregar_tarea(usuario):

    hora = time.strftime("/fecha: %I:%M:%p %d/%m/%Y") #agrega la hora y la fecha del sistema a la tarea
    insetar =f"{usuario.capitalize()} /Pendiente {hora}"
    agregar = open("pendientes.txt","a")
    agregar.write(insetar + "\n")
    agregar.close()
    
def modificar_tarea(seleccion,usuario):
    
    hora = time.strftime("/fecha: %I:%M:%p %d/%m/%Y") 
    lista =  open("pendientes.txt","r+",encoding="utf-8")
    modificar = lista.readlines()
    nueva_tarea = f"{usuario.capitalize()} /Pendiente {hora}"
    modificar[seleccion-1] = nueva_tarea
    lista = open("pendientes.txt","w")
    lista.writelines(modificar)
    lista.close()
    
def eliminar_tarea(usuario):

    lista =  open("pendientes.txt","r+",encoding="utf-8")
    seleccion = lista.readlines()
    seleccion.remove(seleccion[usuario-1])
    lista = open("pendientes.txt","w")
    lista.writelines(seleccion)
    lista.close()

def vaciar_completadas():
    lista =  open("completado.txt","w")
    lista.truncate(0)
    lista.close
    print("borrado")

    
def completar_tarea(estado):

    listado = open("pendientes.txt","r",encoding="utf-8")
    leer = listado.readlines()
    completado = open("completado.txt","a")
    c = leer[estado-1]
    completado.write(c.replace("Pendiente","Completado"))
    eliminar_tarea(estado)
    # copiara la tarea del archivo "pendiente" y la pondra en el archivo "completado" replazando el string pendiente por Completado ademas,
    #eliminara del primer archivo archivo  la tarea elegida por el usuario

#menu principal
menu ="""Menu
1.Lista de tareas
2.Agregar tarea
3.Modificar tarea
4.Eliminar tarea
5.Completar tarea
6.Salir
"""


while True:

    print(menu)
    opcion = (input("Seleccione una opcion: "))
    os.system("cls" if os.name == "nt" else "clear")# el modulo limpiara la panatalla de los usuarios de Linux,Mac y Windows
    
    if opcion == "1":
        
        print("1.Tareas pendiente \n2.Tareas completadas")
        elegir = input("seleccione una opcion: ")

        if elegir == "1":

            lisitado_de_tareas()
            input("Presione enter para regresar")
            os.system("cls" if os.name == "nt" else "clear")

        elif elegir == "2":

            lista_de_tareas_completadas()
            input("Presione enter para regresar")
            os.system("cls" if os.name == "nt" else "clear")

        else:

            os.system("cls" if os.name == "nt" else "clear")
            print("opcion invalida")

    elif opcion == "2":
        
        salir = True
        while salir == True:
            agregar = input("Ingrese la tarea: ")
            if len(agregar) > 0:
              
                agregar_tarea(agregar)

                elegir = input("Ingrese N para salir o enter para continuar: ")
                if elegir.upper() == "N":
                    salir = False
                
                os.system("cls" if os.name == "nt" else "clear")
            else:
                print("Ingrese alguna tarea")
                
    elif opcion == "3":
        if  os.path.getsize("pendientes.txt") == 0:

            print("no hay tareas")

        else:

            salir = True
            while salir == True:

                try:

                    lisitado_de_tareas()
                    elegir = int(input("Elija por el por orden: "))
                    modificar = input("Ingrese la nueva tarea: ")
                    modificar_tarea(elegir,modificar)
                    elegir = input("Ingrese N para salir o enter para continuar: ")
                    os.system("cls" if os.name == "nt" else "clear")
                    if elegir == "n" or elegir == "N":
                         salir = False

                except:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Opcion invalidad")
                       
    elif opcion == "4":

        print("1.Eliminar tareas pendiente\n2.Vaciar lista de tareas completadas")
        seleccion = input("que desea hacer: ")

        if seleccion == "1":
            if  os.path.getsize("pendientes.txt") == 0:

                print("no hay tareas")

            else:

                salir = True
                while salir == True:

                    try:
                        lisitado_de_tareas()
                        eliminar = int(input("Elija por el por orden: "))
                        eliminar_tarea(eliminar)
                        input("Presione enter para volver")
                        salir = False
                        os.system("cls" if os.name == "nt" else "clear")
                    except:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Ingrese una opcion valiida")

        elif seleccion == "2":

            vaciar_completadas()

    elif opcion == "5":
        if  os.path.getsize("pendientes.txt") == 0:

            print("No hay tareas")

        else:

            lisitado_de_tareas()
            completa = int(input("Ingrese para completar: "))
            completar_tarea(completa)

    elif opcion == "6":

        print("Adios")
        break

    else:
        print("Ingrese una opcion valida")
