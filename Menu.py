#Menu
from inputs import pedir_entero, pedir_texto, pedir_flotante, agregar_elemento
from Prints import mostrar_mensaje, mostrar_lista_alumnos, mostrar_alumno
from Archivos import cargar_alumnos_json, guardar_alumnos_json
from Funciones import verificar_legajo_repetido, buscar_por_nombre_apellido, ordenar_salon_fama

def ejecutar_menu_principal():
    lista_alumnos = []
    datos_cargados = False
    archivo_origen = "alumnos.json"

    while True:
        mostrar_mensaje("\n========================================")
        mostrar_mensaje("         SISTEMA DE EGRESADOS - UTN FRA ")
        mostrar_mensaje("========================================")
        mostrar_mensaje("1. Cargar Alumnos")
        mostrar_mensaje("2. Mostrar egresados por plan")
        mostrar_mensaje("3. Mostrar egresados anteriores al año 2000")
        mostrar_mensaje("4. Buscar alumno por nombre o apellido")
        mostrar_mensaje("5. Salón de la Fama")
        mostrar_mensaje("6. Salir")

        opcion = pedir_entero("Seleccione una opción: ", 1, 6)

        if opcion == 1:
            mostrar_mensaje("\n1. Cargar desde archivo alumnos.json")
            mostrar_mensaje("2. Carga manual")
            tipo_carga = pedir_entero("Seleccione tipo de carga: ", 1, 2)
            
            if tipo_carga == 1:
                lista_alumnos = cargar_alumnos_json(archivo_origen)
                mostrar_mensaje("Alumnos cargados desde JSON exitosamente.")
            else:
                while True:
                    legajo = pedir_entero("Ingrese número de legajo (100000-999999): ", 100000, 999999)
                    if verificar_legajo_repetido(lista_alumnos, legajo):
                        print("Error: Ese número de legajo ya pertenece a otro alumno registrado.")
                    else:
                        break

                nombre = pedir_texto("Ingrese nombre: ")
                apellido = pedir_texto("Ingrese apellido: ")
                egreso = pedir_entero("Ingrese año de egreso (1991-2026): ", 1991, 2026)
                
                mostrar_mensaje("Planes disponibles: 1991, 2003, 2024")
                while True:
                    plan = pedir_entero("Ingrese plan: ", 1991, 2024)
                    if plan in [1991, 2003, 2024]:
                        break
                    print("Plan inválido.")
                    
                nota = pedir_flotante("Ingrese nota promedio (6.0-10.0): ", 6.0, 10.0)
                
                nuevo_alumno = {
                    "legajo": legajo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "egreso": egreso,
                    "plan": plan,
                    "nota_promedio": nota
                }
                
                mostrar_mensaje("\nVista previa del Alumno:")
                mostrar_alumno(nuevo_alumno)
                mostrar_mensaje("1. Confirmar adicion\n2. Cancelar")
                confirmar = pedir_entero("Confirmación: ", 1, 2)
                if confirmar == 1:
                    lista_alumnos = agregar_elemento(lista_alumnos, nuevo_alumno)
                    mostrar_mensaje("Alumno registrado de manera exitosa.")
                    
            datos_cargados = True

        elif opcion in [2, 3, 4, 5]:
            if not datos_cargados:
                mostrar_mensaje("Error: Operación denegada. Debe realizar una carga de alumnos antes de consultar.")
            else:
                if opcion == 2:
                    mostrar_mensaje("Planes válidos: 1991, 2003, 2024")
                    plan_buscar = pedir_entero("Ingrese el plan a consultar: ", 1991, 2024)
                    filtrados = []
                    for al in lista_alumnos:
                        if al["plan"] == plan_buscar:
                            filtrados = agregar_elemento(filtrados, al)
                    mostrar_lista_alumnos(filtrados)

                elif opcion == 3:
                    filtrados = []
                    suma_promedios = 0.0
                    for al in lista_alumnos:
                        if al["egreso"] < 2000:
                            filtrados = agregar_elemento(filtrados, al)
                            suma_promedios += al["nota_promedio"]
                    
                    if len(filtrados) == 0:
                        mostrar_mensaje("No existen egresados registrados anteriores al año 2000.")
                    else:
                        mostrar_lista_alumnos(filtrados)
                        promedio_general = suma_promedios / len(filtrados)
                        mostrar_mensaje(f"\nNota promedio general de los encontrados: {promedio_general:.2f}")

                elif opcion == 4:
                    termino = pedir_texto("Ingrese el nombre o apellido a buscar (mínimo 3 letras): ")
                    encontrados = buscar_por_nombre_apellido(lista_alumnos, termino)
                    mostrar_mensaje(f"Cantidad de alumnos encontrados: {len(encontrados)}")
                    mostrar_lista_alumnos(encontrados)

                elif opcion == 5:
                    filtrados = []
                    for al in lista_alumnos:
                        if al["nota_promedio"] >= 9.0:
                            filtrados = agregar_elemento(filtrados, al)
                    
                    if len(filtrados) == 0:
                        mostrar_mensaje("Error: No hay ningún alumno con promedio mayor o igual a 9.")
                    else:
                        ordenados = ordenar_salon_fama(filtrados)
                        mostrar_lista_alumnos(ordenados)

        elif opcion == 6:
            if datos_cargados:
                guardar_alumnos_json(archivo_origen, lista_alumnos)
                mostrar_mensaje("Base de datos guardada en JSON.")
            mostrar_mensaje("Saliendo del sistema...")
            break