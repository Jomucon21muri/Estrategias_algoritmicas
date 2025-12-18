"""
Ejemplo: Fibonacci con Programación Dinámica

Demuestra la diferencia entre recursión simple,
memoización (top-down) y tabulación (bottom-up).

Complejidad:
- Recursiva: O(2^n) - Exponencial
- DP: O(n) - Lineal
"""

import time
from functools import wraps


def medir_tiempo(func):
    """Decorador para medir tiempo de ejecución."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"  Tiempo: {(fin - inicio)*1000:.4f} ms")
        return resultado
    return wrapper


# Enfoque 1: Recursión Simple (Ineficiente)
@medir_tiempo
def fibonacci_recursivo(n):
    """
    Implementación recursiva simple de Fibonacci.
    
    Complejidad Temporal: O(2^n) - EXPONENCIAL
    Complejidad Espacial: O(n) - stack de llamadas
    
    Recalcula los mismos valores múltiples veces.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Enfoque 2: Memoización (Top-Down DP)
@medir_tiempo
def fibonacci_memoizacion(n, memo=None):
    """
    Fibonacci con memoización (cacheo de resultados).
    
    Complejidad Temporal: O(n)
    Complejidad Espacial: O(n) - memo + stack
    
    Calcula cada valor solo una vez y lo almacena.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoizacion(n - 1, memo) + fibonacci_memoizacion(n - 2, memo)
    return memo[n]


# Enfoque 3: Tabulación (Bottom-Up DP)
@medir_tiempo
def fibonacci_tabulacion(n):
    """
    Fibonacci con tabulación (iterativo).
    
    Complejidad Temporal: O(n)
    Complejidad Espacial: O(n) - tabla
    
    Construye la solución de abajo hacia arriba.
    """
    if n <= 1:
        return n
    
    tabla = [0] * (n + 1)
    tabla[1] = 1
    
    for i in range(2, n + 1):
        tabla[i] = tabla[i - 1] + tabla[i - 2]
    
    return tabla[n]


# Enfoque 4: Optimizado en Espacio
@medir_tiempo
def fibonacci_optimizado(n):
    """
    Fibonacci optimizado en espacio.
    
    Complejidad Temporal: O(n)
    Complejidad Espacial: O(1)
    
    Solo mantiene los dos últimos valores.
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        actual = prev1 + prev2
        prev2, prev1 = prev1, actual
    
    return prev1


def comparar_metodos(n):
    """Compara todos los métodos para un valor de n."""
    print(f"\n{'='*50}")
    print(f"Calculando Fibonacci({n})")
    print(f"{'='*50}")
    
    # Recursivo (solo para n pequeños)
    if n <= 35:
        print("1. Recursivo:")
        resultado = fibonacci_recursivo(n)
        print(f"  Resultado: {resultado}")
    else:
        print("1. Recursivo: OMITIDO (demasiado lento)")
    
    # Memoización
    print("\n2. Memoización (Top-Down):")
    resultado = fibonacci_memoizacion(n)
    print(f"  Resultado: {resultado}")
    
    # Tabulación
    print("\n3. Tabulación (Bottom-Up):")
    resultado = fibonacci_tabulacion(n)
    print(f"  Resultado: {resultado}")
    
    # Optimizado
    print("\n4. Optimizado en Espacio:")
    resultado = fibonacci_optimizado(n)
    print(f"  Resultado: {resultado}")


def main():
    print("DEMOSTRACIÓN: Fibonacci con Programación Dinámica")
    print("=" * 50)
    
    # Comparar para valores pequeños
    comparar_metodos(10)
    comparar_metodos(30)
    
    # Para valores grandes, solo DP
    print(f"\n{'='*50}")
    print("Para valores grandes (n=100):")
    print(f"{'='*50}")
    n = 100
    resultado = fibonacci_optimizado(n)
    print(f"Fibonacci({n}) = {resultado}")


if __name__ == "__main__":
    main()
