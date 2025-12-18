# 5️⃣ Backtracking (Vuelta Atrás)

## 📖 Introducción

**Backtracking** es una técnica algorítmica que construye candidatos a solución incrementalmente y abandona (retrocede) cuando determina que un candidato no puede llevar a una solución válida.

## 🎯 Características Principales

- 🌳 **Exploración sistemática:** Recorre el espacio de soluciones como un árbol
- ✂️ **Poda:** Elimina ramas que no pueden llevar a soluciones
- 🔄 **Retroceso:** Deshace elecciones cuando no funcionan
- 🎯 **Completo:** Encuentra todas las soluciones posibles

## 📊 Esquema General

```python
def backtracking(solucion_parcial):
    # Caso base: solución completa
    if es_solucion_completa(solucion_parcial):
        procesar_solucion(solucion_parcial)
        return
    
    # Generar candidatos
    for candidato in generar_candidatos(solucion_parcial):
        # Poda: verificar si es prometedor
        if es_valido(solucion_parcial, candidato):
            # Hacer elección
            agregar(solucion_parcial, candidato)
            
            # Recursión
            backtracking(solucion_parcial)
            
            # Deshacer elección (backtrack)
            quitar(solucion_parcial, candidato)
```

## 💡 Problemas Clásicos

### 1. N-Reinas
Colocar N reinas en un tablero N×N sin que se ataquen.

### 2. Sudoku
Resolver el popular juego de lógica.

### 3. Coloración de Grafos
Asignar colores a vértices sin que vecinos compartan color.

### 4. Suma de Subconjunto
Encontrar subconjuntos que sumen un valor objetivo.

### 5. Generación de Permutaciones
Generar todas las permutaciones de un conjunto.

## 📂 Estructura de Este Módulo

```
05_Backtracking/
├── README.md
├── ejemplos/
│   ├── n_reinas.py
│   ├── sudoku.py
│   ├── coloracion_grafos.py
│   ├── suma_subconjunto.py
│   └── permutaciones.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Problema de las N-Reinas

```python
def resolver_n_reinas(n):
    """
    Encuentra todas las formas de colocar n reinas en un tablero n×n.
    
    Complejidad: O(n!) en el peor caso
    """
    def es_seguro(tablero, fila, col):
        # Verificar columna
        for i in range(fila):
            if tablero[i] == col:
                return False
        
        # Verificar diagonal superior izquierda
        i, j = fila - 1, col - 1
        while i >= 0 and j >= 0:
            if tablero[i] == j:
                return False
            i -= 1
            j -= 1
        
        # Verificar diagonal superior derecha
        i, j = fila - 1, col + 1
        while i >= 0 and j < n:
            if tablero[i] == j:
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(fila, tablero, soluciones):
        # Caso base: todas las reinas colocadas
        if fila == n:
            soluciones.append(tablero[:])
            return
        
        # Probar cada columna en esta fila
        for col in range(n):
            if es_seguro(tablero, fila, col):
                # Hacer elección
                tablero[fila] = col
                
                # Recursión
                backtrack(fila + 1, tablero, soluciones)
                
                # Deshacer (implícito al probar siguiente columna)
                tablero[fila] = -1
    
    soluciones = []
    tablero = [-1] * n  # tablero[i] = columna de la reina en fila i
    backtrack(0, tablero, soluciones)
    
    return soluciones

def imprimir_tablero(tablero):
    """Imprime una solución del problema de N-reinas."""
    n = len(tablero)
    for i in range(n):
        fila = ['Q' if tablero[i] == j else '.' for j in range(n)]
        print(' '.join(fila))
    print()

# Uso
n = 4
soluciones = resolver_n_reinas(n)
print(f"Número de soluciones para {n}-reinas: {len(soluciones)}\n")
print("Primera solución:")
imprimir_tablero(soluciones[0])
```

### Ejemplo 2: Resolver Sudoku

```python
def resolver_sudoku(tablero):
    """
    Resuelve un Sudoku usando backtracking.
    
    Args:
        tablero: Matriz 9×9 con números 1-9 y 0 para celdas vacías
    
    Returns:
        True si se encontró solución, False en caso contrario
    """
    def es_valido(tablero, fila, col, num):
        # Verificar fila
        if num in tablero[fila]:
            return False
        
        # Verificar columna
        for i in range(9):
            if tablero[i][col] == num:
                return False
        
        # Verificar subcuadrícula 3×3
        inicio_fila = (fila // 3) * 3
        inicio_col = (col // 3) * 3
        for i in range(inicio_fila, inicio_fila + 3):
            for j in range(inicio_col, inicio_col + 3):
                if tablero[i][j] == num:
                    return False
        
        return True
    
    def encontrar_vacia(tablero):
        for i in range(9):
            for j in range(9):
                if tablero[i][j] == 0:
                    return (i, j)
        return None
    
    def backtrack(tablero):
        # Encontrar celda vacía
        vacia = encontrar_vacia(tablero)
        
        # Caso base: no hay celdas vacías
        if vacia is None:
            return True
        
        fila, col = vacia
        
        # Probar números del 1 al 9
        for num in range(1, 10):
            if es_valido(tablero, fila, col, num):
                # Hacer elección
                tablero[fila][col] = num
                
                # Recursión
                if backtrack(tablero):
                    return True
                
                # Deshacer elección
                tablero[fila][col] = 0
        
        return False
    
    return backtrack(tablero)

# Uso
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if resolver_sudoku(sudoku):
    print("Sudoku resuelto:")
    for fila in sudoku:
        print(fila)
else:
    print("No tiene solución")
```

### Ejemplo 3: Coloración de Grafos

```python
def colorear_grafo(grafo, num_colores):
    """
    Asigna colores a vértices de un grafo tal que
    vértices adyacentes tengan colores diferentes.
    
    Args:
        grafo: Diccionario {vértice: [vecinos]}
        num_colores: Número de colores disponibles
    
    Returns:
        Diccionario con asignación de colores o None
    """
    vertices = list(grafo.keys())
    colores = {}
    
    def es_seguro(vertice, color):
        for vecino in grafo[vertice]:
            if vecino in colores and colores[vecino] == color:
                return False
        return True
    
    def backtrack(indice):
        # Caso base: todos los vértices coloreados
        if indice == len(vertices):
            return True
        
        vertice = vertices[indice]
        
        # Probar cada color
        for color in range(num_colores):
            if es_seguro(vertice, color):
                # Hacer elección
                colores[vertice] = color
                
                # Recursión
                if backtrack(indice + 1):
                    return True
                
                # Deshacer elección
                del colores[vertice]
        
        return False
    
    if backtrack(0):
        return colores
    return None

# Uso
grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

colores = colorear_grafo(grafo, 3)
if colores:
    print("Coloración encontrada:")
    for vertice, color in sorted(colores.items()):
        print(f"{vertice}: Color {color}")
else:
    print("No es posible colorear con ese número de colores")
```

### Ejemplo 4: Suma de Subconjunto

```python
def suma_subconjunto_todas(numeros, objetivo):
    """
    Encuentra todos los subconjuntos que suman el objetivo.
    
    Complejidad: O(2^n) en el peor caso
    """
    soluciones = []
    
    def backtrack(indice, subconjunto_actual, suma_actual):
        # Caso base: alcanzamos el objetivo
        if suma_actual == objetivo:
            soluciones.append(subconjunto_actual[:])
            return
        
        # Poda: si la suma excede o no hay más elementos
        if suma_actual > objetivo or indice >= len(numeros):
            return
        
        # Decisión 1: incluir el elemento actual
        subconjunto_actual.append(numeros[indice])
        backtrack(indice + 1, subconjunto_actual, suma_actual + numeros[indice])
        subconjunto_actual.pop()  # Backtrack
        
        # Decisión 2: no incluir el elemento actual
        backtrack(indice + 1, subconjunto_actual, suma_actual)
    
    backtrack(0, [], 0)
    return soluciones

# Uso
numeros = [1, 2, 3, 4, 5]
objetivo = 7

soluciones = suma_subconjunto_todas(numeros, objetivo)
print(f"Subconjuntos que suman {objetivo}:")
for sol in soluciones:
    print(sol)
```

### Ejemplo 5: Generar Permutaciones

```python
def generar_permutaciones(elementos):
    """
    Genera todas las permutaciones de un conjunto.
    
    Complejidad: O(n!)
    """
    resultado = []
    
    def backtrack(permutacion, restantes):
        # Caso base: no hay elementos restantes
        if not restantes:
            resultado.append(permutacion[:])
            return
        
        # Probar cada elemento restante
        for i in range(len(restantes)):
            # Hacer elección
            permutacion.append(restantes[i])
            nuevos_restantes = restantes[:i] + restantes[i+1:]
            
            # Recursión
            backtrack(permutacion, nuevos_restantes)
            
            # Deshacer elección
            permutacion.pop()
    
    backtrack([], elementos)
    return resultado

# Versión alternativa con swap
def generar_permutaciones_swap(elementos):
    """Genera permutaciones usando intercambio in-place."""
    resultado = []
    elementos = list(elementos)
    
    def backtrack(inicio):
        if inicio == len(elementos):
            resultado.append(elementos[:])
            return
        
        for i in range(inicio, len(elementos)):
            # Intercambiar
            elementos[inicio], elementos[i] = elementos[i], elementos[inicio]
            
            # Recursión
            backtrack(inicio + 1)
            
            # Deshacer intercambio
            elementos[inicio], elementos[i] = elementos[i], elementos[inicio]
    
    backtrack(0)
    return resultado

# Uso
elementos = [1, 2, 3]
perms = generar_permutaciones(elementos)
print(f"Permutaciones de {elementos}:")
for perm in perms:
    print(perm)
```

## 🎓 Técnicas de Optimización

### 1. Ordenamiento Previo
Ordenar candidatos para encontrar soluciones más rápido.

### 2. Poda Agresiva
Eliminar ramas lo antes posible.

### 3. Heurísticas
Probar candidatos más prometedores primero.

### 4. Memorización
Recordar estados ya explorados (híbrido con DP).

## 🎓 Ejercicios Propuestos

1. **Laberinto:** Encontrar todos los caminos de salida en un laberinto

2. **Palabra en Matriz:** Buscar si una palabra existe en una matriz de letras

3. **Partición Igual:** Dividir un conjunto en dos subconjuntos de igual suma

4. **Generación de Paréntesis:** Generar todas las combinaciones válidas de n pares de paréntesis

5. **Expresiones Aritméticas:** Insertar operadores entre dígitos para obtener un objetivo

## ⚡ Backtracking vs Fuerza Bruta

| Aspecto | Backtracking | Fuerza Bruta |
|---------|-------------|--------------|
| Exploración | Con poda | Exhaustiva |
| Eficiencia | Mejor | Peor |
| Retroceso | Sí | No |
| Espacio | O(profundidad) | O(2^n) o O(n!) |

## 🔗 Recursos Adicionales

- [Backtracking Patterns](https://leetcode.com/problems/permutations/solutions/18239/A-general-approach-to-backtracking-questions/)
- [Visualización de N-Reinas](https://visualgo.net/en/recursion)

## ⏭️ Siguiente Módulo

Continúa con [Ramificación y Acotación](../06_Ramificacion_y_Acotacion/README.md) para aprender optimización con cotas.

---

[⬅️ Volver al índice principal](../README.md)
