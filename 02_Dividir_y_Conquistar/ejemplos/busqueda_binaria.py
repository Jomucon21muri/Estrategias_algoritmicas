"""
Ejemplo: Búsqueda Binaria (Dividir y Conquistar)

Busca un elemento en un array ORDENADO dividiendo
repetidamente el espacio de búsqueda a la mitad.

Complejidad Temporal: O(log n)
Complejidad Espacial: O(log n) recursivo, O(1) iterativo
"""

def busqueda_binaria_recursiva(arr, objetivo, inicio=0, fin=None):
    """
    Implementación recursiva de búsqueda binaria.
    
    Args:
        arr: Array ordenado donde buscar
        objetivo: Elemento a buscar
        inicio: Índice inicial del rango de búsqueda
        fin: Índice final del rango de búsqueda
    
    Returns:
        Índice del elemento si se encuentra, -1 en caso contrario
    """
    if fin is None:
        fin = len(arr) - 1
    
    # Caso base: espacio de búsqueda vacío
    if inicio > fin:
        return -1
    
    # Dividir: encontrar el punto medio
    medio = (inicio + fin) // 2
    
    # Conquistar: comparar y buscar en la mitad apropiada
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] > objetivo:
        # Buscar en la mitad izquierda
        return busqueda_binaria_recursiva(arr, objetivo, inicio, medio - 1)
    else:
        # Buscar en la mitad derecha
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, fin)


def busqueda_binaria_iterativa(arr, objetivo):
    """
    Implementación iterativa de búsqueda binaria.
    Más eficiente en espacio que la versión recursiva.
    
    Returns:
        Índice del elemento si se encuentra, -1 en caso contrario
    """
    inicio = 0
    fin = len(arr) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return -1


def encontrar_primera_ocurrencia(arr, objetivo):
    """
    Encuentra la primera ocurrencia de un elemento
    en un array ordenado que puede tener duplicados.
    """
    inicio, fin = 0, len(arr) - 1
    resultado = -1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if arr[medio] == objetivo:
            resultado = medio
            fin = medio - 1  # Continuar buscando a la izquierda
        elif arr[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    
    return resultado


def main():
    # Ejemplo 1: Búsqueda binaria básica
    numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    objetivo = 11
    
    print(f"Array ordenado: {numeros}")
    print(f"Buscar: {objetivo}")
    
    # Versión recursiva
    indice_rec = busqueda_binaria_recursiva(numeros, objetivo)
    print(f"Recursiva: Índice = {indice_rec}")
    
    # Versión iterativa
    indice_iter = busqueda_binaria_iterativa(numeros, objetivo)
    print(f"Iterativa: Índice = {indice_iter}")
    
    # Ejemplo 2: Elemento no presente
    no_existe = 8
    print(f"\nBuscar elemento que no existe: {no_existe}")
    resultado = busqueda_binaria_iterativa(numeros, no_existe)
    print(f"Resultado: {resultado}")
    
    # Ejemplo 3: Array con duplicados
    con_duplicados = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
    print(f"\nArray con duplicados: {con_duplicados}")
    print(f"Primera ocurrencia de 5: índice {encontrar_primera_ocurrencia(con_duplicados, 5)}")
    print(f"Primera ocurrencia de 2: índice {encontrar_primera_ocurrencia(con_duplicados, 2)}")


if __name__ == "__main__":
    main()
