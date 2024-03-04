import os
import time


def lisitado_de_tareas():
    listado = open("guardado.txt","r",encoding="utf-8")#utf-8 evita problemas de texto con la gramatica española
    leer = listado.readlines() 
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]
    print("".join(enumerada))
    listado.close()    

def agregar_tarea():
    a ="cocinar"
    agregar = open("guardado.txt","a")
    agregar.write("\n" + a)
    print("h")
    agregar.close()
    
def eliminar_tarea():
    pass


def completar_tarea():
    pass

def modificar_tarea():
    pass



menu ="""Menu
1.Lista de tareas
2.Agregar tarea
3.Eliminar tarea
4.Completar tarea
5.Salir
"""

print(menu)
opcion = int(input("Seleccione una opcion:"))

# while True:
os.system("cls")
if opcion == 1:
    lisitado_de_tareas()
elif opcion == 2:
    print(agregar_tarea())
elif opcion == 3:
    print(eliminar_tarea())
elif opcion == 4:
    print(completar_tarea())
elif opcion == 5:
    print("Adiós") 
else:
    print("Ingrese una opcion valida")
