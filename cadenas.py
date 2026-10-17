# Archivo principal del sistema

# ============================================================
# LABORATORIO N° 4 - CADENAS DE CARACTERES Y ARREGLOS PARALELOS
# ============================================================

# ------------------------------------------------------------
# ETAPA 1: MANIPULACIÓN DE CADENAS (substring, indexOf, replace, split)
# Autor: Cristian Omar Huamán Rojas
# PEGA AQUÍ TU CÓDIGO (métodos de manipulación de texto)
# ------------------------------------------------------------



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
# ------------------------------------------------------------
def mostrar_menu():
    print("\n" + "=" * 45)
    print("   LABORATORIO N° 4 - CADENAS Y ARREGLOS")
    print("=" * 45)
    print("1. Manipulación de cadenas")
    print("2. Listas paralelas")
    print("3. Estructuras combinadas")
    print("4. Búsqueda textual y ordenamiento")
    print("5. Salir")
    print("=" * 45)

def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            manipular_cadena()
        elif opcion == "2":
            probar_listas_paralelas()
        elif opcion == "3":
            usuarios = crear_usuarios()
            mostrar_usuarios(usuarios)
        elif opcion == "4":
            probar_busqueda_y_ordenamiento()
        elif opcion == "5":
            print("\nSaliendo del sistema.")
        else:
            print("\nOpción inválida.")

if __name__ == "__main__":
    main()
