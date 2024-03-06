import os
import time


def lisitado_de_tareas():
    
    listado = open("guardado.txt","r",encoding="utf-8")
    #Gracacias a utf-g8 se envitar problemas con careteres que infrese el usuario
    leer = listado.readlines()
    #readlines convierte los lineas del archivo de texto en elementos de una lis lista 
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]#muestra la informacion  estilo cascada y enumera cada tarea
    print("".join(enumerada))
    listado.close()    

def agregar_tarea(usuario):

    hora = time.strftime("%I:%M:%p %d/%m/%Y")
    insetar =f"{usuario} pendiente {hora}"
    agregar = open("guardado.txt","a")
    agregar.write(insetar + "\n")
    agregar.close()
    
def modificar_tarea():
    pass
    
def eliminar_tarea(usuario):

    lista =  open("guardado.txt","r+",encoding="utf-8")
    seleccion = lista.readlines()
    seleccion.remove(seleccion[usuario-1])#remover lo que el usuario ingrese
    lista = open("guardado.txt","w")
    
    lista.writelines(seleccion)
    lista.close()
    

def completar_tarea():
    pass


menu ="""Menu
1.Lista de tareas
2.Agregar tarea
3.Modificar tarea
4.Guardar tarea
5.Eliminar tarea
6.Completar tarea
7.Salir
"""

while True:

    print(menu)
    opcion = (input("Seleccione una opcion:"))
    os.system("cls" if os.name == "nt" else "clear") # Limpia la panatalla de los usuarios de Linux,Mac y Windows
    
    if opcion == "1":
       
        lisitado_de_tareas()
        input("Presione enter para regresar")
        os.system("cls" if os.name == "nt" else "clear")

    elif opcion == "2":
        
        salir = 0
        while salir ==0:

            agregar = input("Ingrese: ")
            agregar_tarea(agregar)

            elegir = input("Ingrese N para salir:")
            if elegir == "n" or elegir == "N":
                salir+=1
            
            os.system("cls" if os.name == "nt" else "clear")

    elif opcion == "3":
        modificar_tarea()
    elif opcion == "4":
        print(completar_tarea())
    elif opcion == "5":

        if  os.path.getsize("guardado.txt") == 0:
            print("no hay tareas")
        else:
            llave = 0
            while llave == 0:
                try:
                    lisitado_de_tareas()
                    eliminar = int(input("ingrese un numero para eliminar: "))
                    eliminar_tarea(eliminar)
                    input("Presione enter para volver")
                    llave += 1
                except:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("error")

    elif opcion == "6":
        completar_tarea()
    elif opcion == "7":
        print("Adios")
        break
    else:
        print("Ingrese una opcion valida")
