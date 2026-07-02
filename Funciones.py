#Funciones
from inputs import agregar_elemento

def verificar_legajo_repetido(lista_alumnos, legajo_ingresado):
    for alumno in lista_alumnos:
        if alumno["legajo"] == legajo_ingresado:
            return True
    return False

def convertir_a_minuscula(cadena):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"
    minusculas = "abcdefghijklmnñopqrstuvwxyzáéíóú"
    resultado = ""
    for caracter in cadena:
        cambiado = False
        for i in range(len(mayusculas)):
            if caracter == mayusculas[i]:
                resultado += minusculas[i]
                cambiado = True
                break
        if not cambiado:
            resultado += caracter
    return resultado

def verificar_coincidencia_parcial(subcadena, cadena_completa):
    sub = convertir_a_minuscula(subcadena)
    completa = convertir_a_minuscula(cadena_completa)
    
    len_sub = len(sub)
    len_comp = len(completa)
    
    if len_sub > len_comp:
        return False
        
    for i in range(len_comp - len_sub + 1):
        coincide = True
        for j in range(len_sub):
            if completa[i + j] != sub[j]:
                coincide = False
                break
        if coincide:
            return True
    return False

def buscar_por_nombre_apellido(lista, termino):
    resultados = []
    for alumno in lista:
        if verificar_coincidencia_parcial(termino, alumno["nombre"]) or verificar_coincidencia_parcial(termino, alumno["apellido"]):
            resultados = agregar_elemento(resultados, alumno)
    return resultados

def clonar_lista(lista):
    largo = len(lista)
    nueva_lista = [None] * largo
    for i in range(largo):
        nueva_lista[i] = lista[i]
    return nueva_lista

def ordenar_salon_fama(lista):
    copia_lista = clonar_lista(lista)
    n = len(copia_lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if copia_lista[j]["nota_promedio"] < copia_lista[j + 1]["nota_promedio"]:
                aux = copia_lista[j]
                copia_lista[j] = copia_lista[j + 1]
                copia_lista[j + 1] = aux
    return copia_lista