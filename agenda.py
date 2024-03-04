import os
import time


def lisitado_de_tareas():
    listado = open("guardado.txt","r",encoding="utf-8")
    #Gracacias a utf-g8 se envitar problemas con careteres que infrese el usuario
    leer = listado.readlines()
    #readlines convierte los lineas del archivo de texto en elementos de una lis lista 
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]#enumera de la lista leer 
    print("".join(enumerada))
    listado.close()    

def agregar_tarea():

    hora = time.strftime("%I:%M:%p %d/%m/%Y")
    a =f"ñ {hora}"
    agregar = open("guardado.txt","a")
    agregar.write("\n" + a)
    agregar.close()
    
def modificar_tarea():
    pass
    
def eliminar_tarea():

    lista =  open("guardado.txt","r+",encoding="utf-8")
    seleccion = lista.readlines()
    seleccion.remove(seleccion[1-1])#remover lo que el usuario ingrese
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
    opcion = int(input("Seleccione una opcion:"))
    os.system("clear")
    
    if opcion == 1:
       
        lisitado_de_tareas()
        input("Presione enter para regresar")
        os.system("clear")

    elif opcion == 2:
        print(agregar_tarea())
    elif opcion == 3:
        modificar_tarea()
    elif opcion == 4:
        print(completar_tarea())
    elif opcion == 5:
        eliminar_tarea()
    elif opcion == 6:
        completar_tarea()
    elif opcion == 7:
        print("adios")
        break
    else:
        print("Ingrese una opcion valida")
