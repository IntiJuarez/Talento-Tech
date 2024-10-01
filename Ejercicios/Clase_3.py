"""
Operaciones Básicas

Crea un programa que solicite al usuario dos números enteros. 
Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
Muestra el resultado de cada operación en un formato claro y amigable. 
Asegúrate de incluir mensajes personalizados que expliquen cada resultado, por ejemplo: "La suma de tus números es: X".

"""


def suma(num:int ,num_dos:int):
    return num + num_dos


def resta(num:int ,num_dos:int):
    return num - num_dos


def multi(num:int ,num_dos:int):
    return num * num_dos


def modulo(num:int ,num_dos:int):
    return num % num_dos

def ingresar_opcion():
     return int(input("\n1 - Suma \n2 - Resta \n3 - Multiplicación \n4 - Módulo \n0 - Salir \n"))

"""

SELECTOR DE OPERACIONES

"""

print("SELECCIONE LA OPERACIÓN QUE DESEA REALIZAR: ")

opcion = ingresar_opcion()
while opcion !=0:

    if opcion == 1:
        num = int(input("Ingrese un número: "))
        num_dos = int(input("\nIngrese el segundo número: "))
        suma(num,num_dos)
        print(f"\nLa suma de {num} + {num_dos} es = ",suma(num,num_dos))
    elif opcion == 2:
        num = int(input("Ingrese un número: "))
        num_dos = int(input("\nIngrese el segundo número: "))
        resta(num,num_dos)
        print(f"\nLa resta de {num} - {num_dos} es = ",resta(num,num_dos))
    elif opcion == 3:
        num = int(input("Ingrese un número: "))
        num_dos = int(input("\nIngrese el segundo número: "))
        multi(num,num_dos)
        print(f"\nLa multiplicación de {num} * {num_dos} es = ",multi(num,num_dos))
    elif opcion == 4:
        num = int(input("Ingrese un número: "))
        num_dos = int(input("\nIngrese el segundo número: "))
        modulo(num,num_dos)
        print(f"\nEl módulo de {num} % {num_dos} es = ",modulo(num,num_dos))
    elif opcion == 0:
        exit
    else:
        print("\n\nDebe seleccionar una opción.\n")

    opcion = ingresar_opcion()













