
#Funciones.
def ingresarDato(datoIngresar:str):
    dato=input(f"Ingrese: {datoIngresar}")

    if dato.isdigit():
        return int(dato)
    
    return dato
    
def mostrarDatos(dato):
    print(dato)


#Variables.
nombre = ingresarDato("Nombre")
cantidadProductos = ingresarDato("Cantida productos")

mostrarDatos(nombre)
mostrarDatos(cantidadProductos)