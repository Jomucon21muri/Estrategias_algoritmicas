# 2️⃣ Dividir y Conquistar (Divide and Conquer)

## 📖 Introducción

**Dividir y Conquistar** es una estrategia algorítmica que descompone un problema en subproblemas más pequeños del mismo tipo, resuelve cada subproblema recursivamente y luego combina las soluciones para obtener la solución del problema original.

## 🎯 Paradigma de Tres Pasos

1. **Dividir:** Descomponer el problema en subproblemas más pequeños
2. **Conquistar:** Resolver los subproblemas recursivamente
3. **Combinar:** Fusionar las soluciones de los subproblemas

## 📊 Análisis de Complejidad

La complejidad se analiza mediante el **Teorema Maestro**:

$$T(n) = aT(n/b) + f(n)$$

Donde:
- $a$ = número de subproblemas
- $b$ = factor de reducción del tamaño
- $f(n)$ = costo de dividir y combinar

| Algoritmo | Recurrencia | Complejidad |
|-----------|-------------|-------------|
| Búsqueda Binaria | T(n) = T(n/2) + O(1) | O(log n) |
| MergeSort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| QuickSort (promedio) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Multiplicación Karatsuba | T(n) = 3T(n/2) + O(n) | O(n^1.58) |

## 🔑 Cuándo Usar Dividir y Conquistar

- ✅ El problema se puede dividir en subproblemas similares
- ✅ Los subproblemas son independientes entre sí
- ✅ Las soluciones parciales se pueden combinar eficientemente
- ✅ El caso base es simple de resolver

## 💡 Ejemplos Clásicos

### 1. Búsqueda Binaria
Buscar un elemento en un array ordenado dividiendo el espacio de búsqueda a la mitad.

### 2. MergeSort
Ordenar dividiendo el array en mitades, ordenando recursivamente y fusionando.

### 3. QuickSort
Ordenar eligiendo un pivote, particionando y ordenando las particiones.

### 4. Multiplicación de Matrices de Strassen
Multiplicar matrices grandes dividiéndolas en submatrices.

### 5. Problema de las Torres de Hanoi
Mover discos entre torres usando recursión.

## 📂 Estructura de Este Módulo

```
02_Dividir_y_Conquistar/
├── README.md
├── ejemplos/
│   ├── busqueda_binaria.py
│   ├── mergesort.py
│   ├── quicksort.py
│   ├── multiplicacion_matrices.py
│   └── torres_hanoi.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Búsqueda Binaria

```python
def busqueda_binaria(arr, objetivo, inicio=0, fin=None):
    """
    Busca un elemento en un array ordenado.
    Complejidad: O(log n)
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
        return busqueda_binaria(arr, objetivo, inicio, medio - 1)
    else:
        return busqueda_binaria(arr, objetivo, medio + 1, fin)

# Uso
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
indice = busqueda_binaria(numeros, 11)
print(f"Elemento encontrado en índice: {indice}")
```

### Ejemplo 2: MergeSort

```python
def mergesort(arr):
    """
    Ordena un array usando Merge Sort.
    Complejidad: O(n log n)
    """
    # Caso base: arrays de tamaño 0 o 1 están ordenados
    if len(arr) <= 1:
        return arr
    
    # Dividir: partir el array por la mitad
    medio = len(arr) // 2
    izquierda = arr[:medio]
    derecha = arr[medio:]
    
    # Conquistar: ordenar recursivamente cada mitad
    izquierda_ordenada = mergesort(izquierda)
    derecha_ordenada = mergesort(derecha)
    
    # Combinar: fusionar las mitades ordenadas
    return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
    """
    Fusiona dos arrays ordenados en uno solo ordenado.
    """
    resultado = []
    i = j = 0
    
    # Combinar elementos en orden
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    # Agregar elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado

# Uso
numeros = [38, 27, 43, 3, 9, 82, 10]
ordenados = mergesort(numeros)
print(f"Array ordenado: {ordenados}")
```

### Ejemplo 3: QuickSort

```python
def quicksort(arr, inicio=0, fin=None):
    """
    Ordena un array usando Quick Sort.
    Complejidad promedio: O(n log n)
    Complejidad peor caso: O(n²)
    """
    if fin is None:
        fin = len(arr) - 1
    
    # Caso base
    if inicio >= fin:
        return
    
    # Dividir: particionar el array
    pivote_indice = partition(arr, inicio, fin)
    
    # Conquistar: ordenar las dos particiones
    quicksort(arr, inicio, pivote_indice - 1)
    quicksort(arr, pivote_indice + 1, fin)

def partition(arr, inicio, fin):
    """
    Particiona el array alrededor de un pivote.
    """
    pivote = arr[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

# Uso
numeros = [10, 7, 8, 9, 1, 5]
quicksort(numeros)
print(f"Array ordenado: {numeros}")
```

### Ejemplo 4: Máximo y Mínimo

```python
def encontrar_max_min(arr, inicio, fin):
    """
    Encuentra el máximo y mínimo en un array usando D&C.
    Complejidad: O(n) con menos comparaciones que fuerza bruta
    """
    # Caso base: un solo elemento
    if inicio == fin:
        return arr[inicio], arr[inicio]
    
    # Caso base: dos elementos
    if fin == inicio + 1:
        if arr[inicio] < arr[fin]:
            return arr[inicio], arr[fin]
        else:
            return arr[fin], arr[inicio]
    
    # Dividir
    medio = (inicio + fin) // 2
    
    # Conquistar
    min_izq, max_izq = encontrar_max_min(arr, inicio, medio)
    min_der, max_der = encontrar_max_min(arr, medio + 1, fin)
    
    # Combinar
    minimo = min(min_izq, min_der)
    maximo = max(max_izq, max_der)
    
    return minimo, maximo

# Uso
numeros = [3, 5, 1, 9, 7, 2, 8]
minimo, maximo = encontrar_max_min(numeros, 0, len(numeros) - 1)
print(f"Mínimo: {minimo}, Máximo: {maximo}")
```

## 🎓 Ejercicios Propuestos

1. **Contar Inversiones:** Contar el número de pares (i, j) donde i < j pero arr[i] > arr[j]

2. **Par Más Cercano:** Encontrar el par de puntos más cercano en un plano 2D

3. **Potencia Rápida:** Calcular $x^n$ en O(log n)

4. **Búsqueda del Pico:** Encontrar un elemento pico en un array (mayor que sus vecinos)

5. **Multiplicación de Enteros Grandes:** Implementar multiplicación de Karatsuba

## ⚡ Ventajas y Desventajas

### Ventajas
- ✅ Muy eficiente para problemas dividibles
- ✅ Naturalmente paralelizable
- ✅ Reduce significativamente la complejidad

### Desventajas
- ⚠️ Overhead de llamadas recursivas
- ⚠️ Puede requerir espacio adicional
- ⚠️ No todos los problemas son dividibles eficientemente

## 🔗 Recursos Adicionales

- [Visualización de MergeSort](https://visualgo.net/sorting)
- [Teorema Maestro](https://en.wikipedia.org/wiki/Master_theorem)

## ⏭️ Siguiente Módulo

Continúa con [Programación Dinámica](../03_Programacion_Dinamica/README.md) para aprender a optimizar problemas con subproblemas superpuestos.

---

[⬅️ Volver al índice principal](../README.md)
