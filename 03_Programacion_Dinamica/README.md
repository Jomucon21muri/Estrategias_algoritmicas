# 3️⃣ Programación Dinámica (Dynamic Programming)

## 📖 Introducción

La **Programación Dinámica (DP)** es una técnica de optimización que resuelve problemas complejos dividiéndolos en subproblemas más simples y almacenando sus resultados para evitar cálculos redundantes. Es especialmente útil cuando los subproblemas se superponen.

## 🎯 Principios Fundamentales

### Condiciones para Aplicar DP

1. **Subestructura Óptima:** La solución óptima se puede construir a partir de soluciones óptimas de subproblemas
2. **Subproblemas Superpuestos:** Los mismos subproblemas se resuelven múltiples veces

### Diferencia con Dividir y Conquistar

| Aspecto | Dividir y Conquistar | Programación Dinámica |
|---------|---------------------|---------------------|
| Subproblemas | Independientes | Superpuestos |
| Almacenamiento | No reutiliza resultados | Memoriza resultados |
| Ejemplo | MergeSort | Fibonacci con memo |

## 📊 Enfoques de Implementación

### 1. Memoización (Top-Down)
- Enfoque recursivo
- Almacena resultados en caché
- Calcula solo lo necesario

### 2. Tabulación (Bottom-Up)
- Enfoque iterativo
- Llena una tabla sistemáticamente
- Calcula todos los subproblemas

## 💡 Problemas Clásicos

### 1. Secuencia de Fibonacci
Calcular el n-ésimo número de Fibonacci eficientemente.

### 2. Problema de la Mochila (Knapsack)
Maximizar el valor de items en una mochila con capacidad limitada.

### 3. Subsecuencia Común Más Larga (LCS)
Encontrar la subsecuencia más larga común a dos secuencias.

### 4. Camino Mínimo
Encontrar el camino de costo mínimo en una matriz.

### 5. Problema del Cambio de Monedas
Encontrar el número mínimo de monedas para dar un cambio.

## 📂 Estructura de Este Módulo

```
03_Programacion_Dinamica/
├── README.md
├── ejemplos/
│   ├── fibonacci.py
│   ├── mochila.py
│   ├── lcs.py
│   ├── camino_minimo.py
│   └── cambio_monedas.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Fibonacci - Comparación de Enfoques

```python
# Enfoque 1: Recursivo puro (Exponencial - O(2^n))
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Enfoque 2: Memoización (Top-Down - O(n))
def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Enfoque 3: Tabulación (Bottom-Up - O(n))
def fibonacci_tabla(n):
    if n <= 1:
        return n
    
    tabla = [0] * (n + 1)
    tabla[1] = 1
    
    for i in range(2, n + 1):
        tabla[i] = tabla[i-1] + tabla[i-2]
    
    return tabla[n]

# Enfoque 4: Optimizado en espacio (O(1) espacio)
def fibonacci_optimizado(n):
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        actual = prev1 + prev2
        prev2, prev1 = prev1, actual
    
    return prev1

# Comparación
n = 10
print(f"Fibonacci({n}) = {fibonacci_tabla(n)}")
```

### Ejemplo 2: Problema de la Mochila 0/1

```python
def mochila_01(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila 0/1.
    
    Args:
        pesos: Lista de pesos de los items
        valores: Lista de valores de los items
        capacidad: Capacidad máxima de la mochila
    
    Returns:
        Valor máximo que se puede obtener
    
    Complejidad: O(n * capacidad)
    """
    n = len(pesos)
    
    # Crear tabla DP
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]
    
    # Llenar la tabla
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            # No tomar el item i
            dp[i][w] = dp[i-1][w]
            
            # Tomar el item i si cabe
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i][w], 
                              dp[i-1][w - pesos[i-1]] + valores[i-1])
    
    # Reconstruir la solución
    items_seleccionados = []
    w = capacidad
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items_seleccionados.append(i-1)
            w -= pesos[i-1]
    
    return dp[n][capacidad], items_seleccionados[::-1]

# Uso
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidad = 8

valor_max, items = mochila_01(pesos, valores, capacidad)
print(f"Valor máximo: {valor_max}")
print(f"Items seleccionados: {items}")
```

### Ejemplo 3: Subsecuencia Común Más Larga (LCS)

```python
def lcs(X, Y):
    """
    Encuentra la longitud de la subsecuencia común más larga.
    
    Complejidad: O(m * n) donde m y n son las longitudes
    """
    m, n = len(X), len(Y)
    
    # Crear tabla DP
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Llenar la tabla
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruir la LCS
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return dp[m][n], ''.join(reversed(lcs_str))

# Uso
X = "ABCDGH"
Y = "AEDFHR"
longitud, subsecuencia = lcs(X, Y)
print(f"Longitud de LCS: {longitud}")
print(f"LCS: {subsecuencia}")
```

### Ejemplo 4: Camino Mínimo en Matriz

```python
def camino_minimo(matriz):
    """
    Encuentra el camino de costo mínimo desde la esquina
    superior izquierda hasta la inferior derecha.
    Solo se puede mover hacia abajo o hacia la derecha.
    
    Complejidad: O(m * n)
    """
    if not matriz or not matriz[0]:
        return 0
    
    m, n = len(matriz), len(matriz[0])
    dp = [[0] * n for _ in range(m)]
    
    # Inicializar primera celda
    dp[0][0] = matriz[0][0]
    
    # Inicializar primera fila
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + matriz[0][j]
    
    # Inicializar primera columna
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + matriz[i][0]
    
    # Llenar el resto de la tabla
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = matriz[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]

# Uso
matriz = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
costo = camino_minimo(matriz)
print(f"Costo mínimo: {costo}")
```

### Ejemplo 5: Cambio de Monedas

```python
def cambio_monedas(monedas, cantidad):
    """
    Encuentra el número mínimo de monedas para dar un cambio.
    
    Complejidad: O(cantidad * len(monedas))
    """
    dp = [float('inf')] * (cantidad + 1)
    dp[0] = 0  # 0 monedas para cantidad 0
    
    # Para cada cantidad
    for i in range(1, cantidad + 1):
        # Probar cada moneda
        for moneda in monedas:
            if moneda <= i:
                dp[i] = min(dp[i], dp[i - moneda] + 1)
    
    return dp[cantidad] if dp[cantidad] != float('inf') else -1

# Uso
monedas = [1, 5, 10, 25]
cantidad = 63
num_monedas = cambio_monedas(monedas, cantidad)
print(f"Número mínimo de monedas: {num_monedas}")
```

## 🎓 Proceso de Resolución

1. **Identificar la decisión:** ¿Qué elecciones se hacen en cada paso?
2. **Definir el estado:** ¿Qué información necesitamos para cada subproblema?
3. **Escribir la recurrencia:** Relación entre estados
4. **Determinar caso base:** Subproblemas más simples
5. **Decidir el orden:** ¿Top-down o bottom-up?
6. **Optimizar espacio:** Reducir dimensiones si es posible

## 🎓 Ejercicios Propuestos

1. **Subsecuencia Creciente Más Larga:** Encontrar la LIS en un array

2. **Edición de Distancia:** Mínimo número de operaciones para transformar una cadena en otra

3. **Partición de Subconjuntos:** ¿Se puede dividir un conjunto en dos subconjuntos de igual suma?

4. **Corte de Varilla:** Maximizar beneficio al cortar una varilla

5. **Escaleras:** ¿De cuántas formas se puede subir una escalera de n escalones si se pueden dar pasos de 1 o 2?

## ⚡ Optimización de Espacio

Muchos problemas de DP pueden optimizarse en espacio:

```python
# En lugar de tabla 2D completa
dp = [[0] * n for _ in range(m)]

# Usar solo dos filas
prev = [0] * n
curr = [0] * n
```

## 🔗 Recursos Adicionales

- [DP Patterns](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns)
- [Visualización de DP](https://visualgo.net/en/recursion)

## ⏭️ Siguiente Módulo

Continúa con [Algoritmos Voraces](../04_Algoritmos_Voraces/README.md) para aprender estrategias de optimización local.

---

[⬅️ Volver al índice principal](../README.md)
