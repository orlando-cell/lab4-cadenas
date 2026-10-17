# Archivo principal del sistema

# ============================================================
# LABORATORIO N° 4 - CADENAS DE CARACTERES Y ARREGLOS PARALELOS
# ============================================================

# ------------------------------------------------------------
# ETAPA 1: MANIPULACIÓN DE CADENAS (substring, indexOf, replace, split)
# Autor: Cristian Omar Huamán Rojas
# PEGA AQUÍ TU CÓDIGO (métodos de manipulación de texto)
# ------------------------------------------------------------
def manipular_cadena():
    texto = "Bienvenidos al laboratorio de Fundamentos de Programación"
    print("\n Texto original:", texto)
    print(" Substring (0:11):", texto[0:11])
    print(" IndexOf 'laboratorio':", texto.find("laboratorio"))
    print(" Replace 'laboratorio' por 'taller':", texto.replace("laboratorio", "taller"))
    print(" Split por espacios:", texto.split())
    return texto


# ------------------------------------------------------------
# ETAPA 2: LISTAS PARALELAS (nombres y edades)
# Autor: Álvaro Leandro Gutiérrez Carranza
# PEGA AQUÍ TU CÓDIGO (búsqueda por nombre, retorno de edad)
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 3: ESTRUCTURAS COMBINADAS (lista de diccionarios)
# Autor: Zinedine Michael Callirgos Cabanillas
# PEGA AQUÍ TU CÓDIGO (crear estructura, mostrar datos)
# ------------------------------------------------------------



# ------------------------------------------------------------
# ETAPA 4: BÚSQUEDA TEXTUAL Y ORDENAMIENTO
# Autor: Juan Orlando Correa Flores
# ------------------------------------------------------------

def buscar_texto(lista_usuarios, ciudad_buscar):
    """Busca usuarios por ciudad y muestra coincidencias."""
    resultados = []
    for usuario in lista_usuarios:
        if usuario["ciudad"].lower() == ciudad_buscar.lower():
            resultados.append(usuario)
    if len(resultados) == 0:
        print(f"\nNo se encontraron usuarios en '{ciudad_buscar}'.")
    else:
        print(f"\nUsuarios encontrados en '{ciudad_buscar}':")
        for u in resultados:
            print(f"    - {u['nombre']} | {u['email']}")
    return resultados


def ordenar_alfabeticamente(lista_usuarios):
    """Ordena los usuarios alfabéticamente por nombre."""
    lista_ordenada = sorted(lista_usuarios, key=lambda u: u["nombre"])
    print("\nUsuarios ordenados alfabéticamente:")
    for u in lista_ordenada:
        print(f"    - {u['nombre']}")
    return lista_ordenada


def probar_busqueda_y_ordenamiento():
    """Prueba las funciones con datos de ejemplo."""
    usuarios = [
        {"nombre": "Juan", "email": "juan@upn.pe", "ciudad": "Cajamarca"},
        {"nombre": "María", "email": "maria@upn.pe", "ciudad": "Lima"},
        {"nombre": "Pedro", "email": "pedro@upn.pe", "ciudad": "Cajamarca"}
    ]
    print("\n" + "=" * 45)
    print("   PRUEBA DE BÚSQUEDA Y ORDENAMIENTO")
    print("=" * 45)
    buscar_texto(usuarios, "Cajamarca")
    ordenar_alfabeticamente(usuarios)
    print("=" * 45)

# ------------------------------------------------------------
# MENÚ PRINCIPAL Y PRUEBAS
# Autor: Anthony Rene Terraz Terrones
# PEGA AQUÍ TU CÓDIGO (main, menú, pruebas)
# ------------------------------------------------------------