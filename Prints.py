#Prints
def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_alumno(alumno):
    print(f"Legajo: {alumno['legajo']} | Nombre: {alumno['nombre']} {alumno['apellido']} | Egreso: {alumno['egreso']} | Plan: {alumno['plan']} | Promedio: {alumno['nota_promedio']}")

def mostrar_lista_alumnos(lista):
    if len(lista) == 0:
        print("No se encontraron registros.")
    else:
        for alumno in lista:
            mostrar_alumno(alumno)