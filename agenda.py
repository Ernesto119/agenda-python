import os
import time


def lisitado_de_tareas():
    listado = open("guardado.txt","r",encoding="utf-8")#utf-8 evita problemas de texto con la gramatica española
    leer = listado.readlines() 
    enumerada = [f"{1+enum}. {elem}" for enum, elem in enumerate(leer)]
    print("".join(enumerada))
    listado.close()    

def agregar_tarea():
    hora = time.strftime("%I:%M:%p %d/%m/%Y")
    a =f"caminar {hora}"
    agregar = open("guardado.txt","a")
    agregar.write("\n" + a)
    agregar.close()
    
def modificar_tarea():
    pass
    
def eliminar_tarea():
    pass

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
