#Archivos
import json

def guardar_alumnos_json(ruta, lista_alumnos):
    archivo = open(ruta, "w")
    json.dump(lista_alumnos, archivo, indent=4)
    archivo.close()

def cargar_alumnos_json(ruta):
    archivo = open(ruta, "r")
    lista = json.load(archivo)
    archivo.close()
    return lista