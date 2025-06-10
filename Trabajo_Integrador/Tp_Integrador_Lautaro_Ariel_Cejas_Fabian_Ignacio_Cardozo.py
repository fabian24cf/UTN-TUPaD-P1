# Trabajo Integrador - Búsqueda y Ordenamiento - TUPaD - UTN - Comisión 11

# Temática: Paradas de colectivo

# Autores: Lautaro Ariel Cejas, Fabian Ignacio Cardozo

# Descripción: Implementa algoritmos de búsqueda (lineal, binaria, interpolación, hash)
# para una lista de paradas de colectivo con nombre y distancia.

import time  # Librería para medir tiempo de ejecución

# Lista de paradas de colectivo (diccionarios con nombre y distancia)
paradas = [
    {"nombre": "Plaza Central", "distancia": 0},
    {"nombre": "Calle 10", "distancia": 2},
    {"nombre": "Estación Sur", "distancia": 3},
    {"nombre": "Universidad", "distancia": 4},
    {"nombre": "Hospital", "distancia": 5},
]

# -----------------------------------------
# Ordenamiento - Bubble Sort por nombre
# -----------------------------------------
def bubble_sort_por_nombre(lista):
    """
    Ordena una lista de diccionarios por la clave 'nombre' (alfabéticamente).
    Usa Bubble Sort, comparando e intercambiando elementos adyacentes.
    """
    n = len(lista)  # Tamaño de la lista
    for i in range(n):  # Pasadas para mover los mayores al final
        for j in range(0, n - i - 1):  # Compara hasta los ya ordenados
            if lista[j]["nombre"] > lista[j + 1]["nombre"]:  # Compara nombres
                # Intercambia diccionarios si el de la izq. es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# -----------------------------------------
# Ordenamiento - Bubble Sort por distancia
# -----------------------------------------
def bubble_sort_por_distancia(lista):
    """
    Ordena una lista de diccionarios por la clave 'distancia' (numérico, ascendente).
    Usa Bubble Sort, ideal para listas pequeñas y aprendizaje.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]["distancia"] > lista[j + 1]["distancia"]:  # Compara distancias
                # Intercambia si la distancia de la izq. es mayor
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# -----------------------------------------
# 1. Búsqueda lineal
# -----------------------------------------
def busqueda_lineal(paradas, nombre):
    """
    Busca una parada por nombre recorriendo la lista secuencialmente.
    No necesita orden previo. Devuelve el diccionario o None si no encuentra.
    """
    for parada in paradas:  # Revisa cada elemento
        if parada["nombre"] == nombre:  # Compara nombre
            return parada  # Encontró, retorna el diccionario
    return None  # No encontró nada

# -----------------------------------------
# 1b. Búsqueda lineal por dististancia
# -----------------------------------------
def busqueda_lineal_distancia(paradas, distancia):
    """
    Busca una parada por distancia recorriendo la lista secuencialmente.
    No necesita orden previo. Devuelve el diccionario o None si no encuentra.
    """
    for parada in paradas:  # Revisa cada elemento
        if parada["distancia"] == distancia:  # Compara distancia
            return parada  # Encontró, retorna el diccionario
    return None  # No encontró nada

# -----------------------------------------
# 2. Búsqueda binaria
# Requiere que la lista esté ordenada alfabéticamente por nombre
# -----------------------------------------
def busqueda_binaria(paradas, nombre):
    """
    Busca una parada por nombre en una lista ordenada alfabéticamente.
    Divide el rango a la mitad en cada iteración. Muy eficiente (O(log n)).
    """
    izquierda = 0  # Índice inicial (bajo)
    derecha = len(paradas) - 1  # Índice final (alto)
    while izquierda <= derecha:  # Mientras el rango sea válido
        medio = (izquierda + derecha) // 2  # Calcula punto medio
        actual = paradas[medio]["nombre"]  # Nombre en la posición media
        if actual == nombre:  # Encontró el nombre
            return paradas[medio]
        elif actual < nombre:  # Busca en la mitad derecha
            izquierda = medio + 1
        else:  # Busca en la mitad izquierda
            derecha = medio - 1
    return None  # No encontró nada

# -----------------------------------------
# 2b. Búsqueda binaria por distancia
# Requiere que la lista esté ordenada de forma ascendiente por distancia
# -----------------------------------------
def busqueda_binaria_distancia(paradas, distancia):
    """
    Busca una parada por distancia en una lista ordenada de forma ascendiente.
    Divide el rango a la mitad en cada iteración. Muy eficiente (O(log n)).
    """
    izquierda = 0  # Índice inicial (bajo)
    derecha = len(paradas) - 1  # Índice final (alto)
    while izquierda <= derecha:  # Mientras el rango sea válido
        medio = (izquierda + derecha) // 2  # Calcula punto medio
        actual = paradas[medio]["distancia"]  # Distancia en la posición media
        if actual == distancia:  # Encontró la distancia
            return paradas[medio]
        elif actual < distancia:  # Busca en la mitad derecha
            izquierda = medio + 1
        else:  # Busca en la mitad izquierda
            derecha = medio - 1
    return None  # No encontró nada

# -----------------------------------------
# 3. Búsqueda por interpolación
# Requiere que la lista esté ordenada por distancia y distribuida uniformemente
# -----------------------------------------
def busqueda_interpolacion(paradas, distancia_objetivo):
    """
    Busca una parada por distancia en una lista ordenada por distancia.
    Estima la posición según la distribución de valores. Ideal para datos uniformes.
    """
    paradas_ordenadas = bubble_sort_por_distancia(paradas.copy())  # Copia ordenada
    bajo = 0  # Índice inicial
    alto = len(paradas_ordenadas) - 1  # Índice final

    while bajo <= alto and distancia_objetivo >= paradas_ordenadas[bajo]["distancia"] and distancia_objetivo <= paradas_ordenadas[alto]["distancia"]:
        # Calcula posición estimada según la fórmula de interpolación
        pos = bajo + ((distancia_objetivo - paradas_ordenadas[bajo]["distancia"]) * (alto - bajo)) // \
                    (paradas_ordenadas[alto]["distancia"] - paradas_ordenadas[bajo]["distancia"])
        if paradas_ordenadas[pos]["distancia"] == distancia_objetivo:  # Encontró
            return paradas_ordenadas[pos]
        elif paradas_ordenadas[pos]["distancia"] < distancia_objetivo:  # Busca derecha
            bajo = pos + 1
        else:  # Busca izquierda
            alto = pos - 1
    return None  # No encontró nada

# -----------------------------------------
# 4. Búsqueda hash
# Se construye un diccionario donde la clave es el nombre de la parada
# -----------------------------------------
def busqueda_hash(tabla, nombre):
    """
    Busca una parada por nombre en una tabla hash.
    Usa el método get para acceso directo (O(1) en promedio).
    """
    return tabla.get(nombre, None)  # Retorna diccionario o None si no existe

# -----------------------------------------
# 4b. Búsqueda hash por distancia
# -----------------------------------------
def busqueda_hash_distancia(tabla, distancia):
    """
    Busca una parada por distancia en una tabla hash.
    """
    return tabla.get(distancia, None)

# -----------------------------------------
# Función para realizar pruebas dinámicas
# -----------------------------------------
def realizar_prueba(tipo_busqueda, parametro):
    """
    Realiza pruebas dinámicas según el tipo de búsqueda solicitado.
    tipo_busqueda: 'nombre' o 'distancia'
    parametro: el nombre o distancia a buscar
    """
    print(f"\n=== PRUEBA DINÁMICA - Búsqueda por {tipo_busqueda}: {parametro} ===")
    
    if tipo_busqueda == "nombre":
        # Búsqueda por nombre
        # 1. Búsqueda lineal
        inicio = time.perf_counter() # Inicia el crónometro
        resultado_lineal = busqueda_lineal(paradas, parametro)
        fin = time.perf_counter() # Apaga el crónometro
        print(f"Búsqueda Lineal: {resultado_lineal}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms") # Muestra el tiempo de ejecución en ms (milisegundos)
        
        # 2. Búsqueda binaria
        inicio = time.perf_counter()
        paradas_ordenadas_nombre = bubble_sort_por_nombre(paradas.copy())
        resultado_binaria = busqueda_binaria(paradas_ordenadas_nombre, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Binaria: {resultado_binaria}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")
        
        # 3. Búsqueda hash
        inicio = time.perf_counter()
        tabla_hash = {p["nombre"]: p for p in paradas}
        resultado_hash = busqueda_hash(tabla_hash, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Hash: {resultado_hash}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")
        
    elif tipo_busqueda == "distancia":
        # Búsqueda por distancia
        # 1. Búsqueda lineal
        inicio = time.perf_counter()
        resultado_lineal = busqueda_lineal_distancia(paradas, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Lineal: {resultado_lineal}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")
        
        # 2. Búsqueda binaria
        inicio = time.perf_counter()
        paradas_ordenadas_distancia = bubble_sort_por_distancia(paradas.copy())
        resultado_binaria = busqueda_binaria_distancia(paradas_ordenadas_distancia, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Binaria: {resultado_binaria}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")
        
        # 3. Búsqueda por interpolación
        inicio = time.perf_counter()
        resultado_interpolacion = busqueda_interpolacion(paradas, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Interpolación: {resultado_interpolacion}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")
        
        # 4. Búsqueda hash
        inicio = time.perf_counter()
        tabla_hash_distancia = {p["distancia"]: p for p in paradas}
        resultado_hash = busqueda_hash_distancia(tabla_hash_distancia, parametro)
        fin = time.perf_counter()
        print(f"Búsqueda Hash: {resultado_hash}")
        print(f"Tiempo: {(fin - inicio) * 1000:.6f} ms")

# -----------------------------------------
# Menú para pruebas dinámicas
# -----------------------------------------
def menu_pruebas():
    """
    Menú sencillo para elegir tipo de búsqueda
    """
    print("\n=== MENÚ DE PRUEBAS ===")
    print("1. Buscar por nombre")
    print("2. Buscar por distancia")
    
    opcion = input("Seleccione opción (1 o 2): ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre de la parada: ")
        realizar_prueba("nombre", nombre)
    elif opcion == "2":
        distancia = int(input("Ingrese la distancia: "))
        realizar_prueba("distancia", distancia)

# -----------------------------------------
# Ejecución de pruebas dinámicas
# -----------------------------------------

# Ejecutar menú
menu_pruebas()