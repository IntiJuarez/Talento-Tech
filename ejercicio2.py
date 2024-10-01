
def ingresaMonto(cantidad_ingreso:int):
    suma=0
    for i in range(cantidad_ingreso):
        monto = input(f"Ingresar monto: ")
        suma+=int(monto)
    return suma

def calcularPromedio(suma:int, cantidad_ingreso:int):
    return suma / cantidad_ingreso 


#Variables
cantidad_ingreso = 6
suma = ingresaMonto(cantidad_ingreso)
promedio = calcularPromedio(suma, cantidad_ingreso)


print(f"El ingreso promedio en el semestre es de {promedio}")

