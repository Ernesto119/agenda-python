import os

def lisitado_de_tareas():
    leer = open("guardado.txt","r")
    leer.close()
    return leer.read()

def agregar_tarea(tarea):
    agregar = open("guardado.txt","a")
    agregar.write(tarea + "\n")
    agregar.close()
    

def eliminar_tarea():
    pass


def completar_tarea():
    pass


menu ="""Menu
1.Lista de tareas
2.Agregar tarea
3.Eliminar tarea
4.Completar tarea
5.Salir
"""

opcion = 0
while opcion != 5:
    print(menu)
    opcion = int(input("Seleccione una opcion:"))

    if opcion == 1:
        print(lisitado_de_tareas())
    elif opcion == 2:
        print(agregar_tarea())
    elif opcion == 3:
        print(eliminar_tarea())
    elif opcion == 4:
        print(completar_tarea())

print("Adiós")
