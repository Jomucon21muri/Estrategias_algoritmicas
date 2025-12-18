"""
Ejemplo: Búsqueda Lineal (Fuerza Bruta)

Busca un elemento en una lista de forma secuencial,
revisando cada elemento hasta encontrarlo.

Complejidad Temporal: O(n)
Complejidad Espacial: O(1)
"""

def busqueda_lineal(lista, objetivo):
    """
    Busca un elemento en una lista de forma secuencial.
    
    Args:
        lista: Lista donde buscar
        objetivo: Elemento a buscar
    
    Returns:
        Índice del elemento si se encuentra, -1 en caso contrario
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_lineal_todas(lista, objetivo):
    """
    Busca todas las ocurrencias de un elemento.
    
    Returns:
        Lista con los índices donde aparece el objetivo
    """
    indices = []
    for i in range(len(lista)):
        if lista[i] == objetivo:
            indices.append(i)
    return indices


def main():
    # Ejemplo 1: Búsqueda simple
    numeros = [4, 2, 7, 1, 9, 5, 3, 7]
    objetivo = 7
    
    indice = busqueda_lineal(numeros, objetivo)
    print(f"Lista: {numeros}")
    print(f"Buscar: {objetivo}")
    
    if indice != -1:
        print(f"✓ Elemento encontrado en índice: {indice}")
    else:
        print(f"✗ Elemento no encontrado")
    
    # Ejemplo 2: Buscar todas las ocurrencias
    print(f"\nBuscar todas las ocurrencias de {objetivo}:")
    todos_indices = busqueda_lineal_todas(numeros, objetivo)
    print(f"Encontrado en índices: {todos_indices}")
    
    # Ejemplo 3: Búsqueda en lista de strings
    palabras = ["python", "java", "javascript", "ruby", "go"]
    palabra_buscar = "javascript"
    
    print(f"\nBuscar '{palabra_buscar}' en {palabras}:")
    pos = busqueda_lineal(palabras, palabra_buscar)
    print(f"Posición: {pos}")


if __name__ == "__main__":
    main()
