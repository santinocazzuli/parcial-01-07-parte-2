#Inputs
def agregar_elemento(lista, elemento):
    nuevo_largo = len(lista) + 1
    nueva_lista = [None] * nuevo_largo
    for i in range(nuevo_largo - 1):
        nueva_lista[i] = lista[i]
    nueva_lista[nuevo_largo - 1] = elemento
    return nueva_lista

def es_cadena_valida(cadena):
    if len(cadena) < 3:
        return False
    letras_y_espacios = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ "
    for caracter in cadena:
        valido = False
        for permitido in letras_y_espacios:
            if caracter == permitido:
                valido = True
                break
        if not valido:
            return False
    return True

def es_numero_valido(cadena):
    if len(cadena) == 0:
        return False
    numeros = "0123456789"
    for caracter in cadena:
        valido = False
        for num in numeros:
            if caracter == num:
                valido = True
                break
        if not valido:
            return False
    return True

def es_flotante_valido(cadena):
    if len(cadena) == 0:
        return False
    numeros = "0123456789"
    puntos = 0
    for caracter in cadena:
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                return False
        else:
            valido = False
            for num in numeros:
                if caracter == num:
                    valido = True
                    break
            if not valido:
                return False
    return True

def pedir_entero(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        if es_numero_valido(entrada):
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
        print(f"Error: Ingrese un entero válido ({minimo}-{maximo}).")

def pedir_flotante(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        if es_flotante_valido(entrada):
            valor = float(entrada)
            if minimo <= valor <= maximo:
                return valor
        print(f"Error: Ingrese un número válido ({minimo}-{maximo}).")

def pedir_texto(mensaje):
    while True:
        entrada = input(mensaje)
        if es_cadena_valida(entrada):
            return entrada
        print("Error: Mínimo 3 caracteres, solo letras.")