# 6️⃣ Ramificación y Acotación (Branch and Bound)

## 📖 Introducción

**Ramificación y Acotación** (Branch and Bound) es una técnica algorítmica para problemas de optimización que explora sistemáticamente el espacio de soluciones mediante un árbol de decisión, podando ramas que no pueden conducir a soluciones óptimas.

## 🎯 Características Principales

- 🌳 **Árbol de decisión:** Representa el espacio de soluciones
- ✂️ **Poda por cotas:** Elimina ramas usando límites superiores/inferiores
- 🎯 **Optimización:** Busca la mejor solución, no solo una válida
- 📊 **Sistemático:** Explora de forma ordenada (BFS o DFS)

## 📊 Componentes Clave

### 1. Ramificación (Branching)
División del problema en subproblemas más pequeños.

### 2. Acotación (Bounding)
Cálculo de cotas (límites) para determinar si una rama puede dar la solución óptima.

### 3. Poda (Pruning)
Eliminación de ramas que no pueden mejorar la mejor solución conocida.

### 4. Estrategia de Búsqueda
- **BFS (Best-First Search):** Explora nodos más prometedores primero
- **DFS (Depth-First Search):** Explora en profundidad
- **LC (Least Cost):** Selecciona nodo de menor cota

## 📊 Comparación con Otras Técnicas

| Aspecto | Branch & Bound | Backtracking | Programación Dinámica |
|---------|---------------|--------------|----------------------|
| Objetivo | Optimización | Todas las soluciones | Optimización |
| Poda | Por cotas | Por validez | No poda |
| Orden | Mejor primero | Sistemático | Bottom-up |
| Garantía | Óptimo global | Completo | Óptimo |

## 💡 Problemas Clásicos

### 1. Problema del Viajante (TSP)
Encontrar el tour más corto que visite todas las ciudades.

### 2. Mochila 0/1
Maximizar valor en mochila con capacidad limitada.

### 3. Asignación de Tareas
Asignar n trabajos a n trabajadores minimizando costo.

### 4. Problema del Conjunto Independiente
Encontrar el conjunto independiente más grande en un grafo.

### 5. Corte de Grafo
Particionar un grafo minimizando aristas cortadas.

## 📂 Estructura de Este Módulo

```
06_Ramificacion_y_Acotacion/
├── README.md
├── ejemplos/
│   ├── tsp_branch_bound.py
│   ├── mochila_01.py
│   ├── asignacion_tareas.py
│   └── conjunto_independiente.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Problema del Viajante (TSP)

```python
import heapq
from typing import List, Tuple

def tsp_branch_bound(distancias):
    """
    Resuelve TSP usando Branch and Bound.
    
    Args:
        distancias: Matriz de distancias entre ciudades
    
    Returns:
        Mejor tour y su costo
    
    Complejidad: O(n!) pero con poda efectiva
    """
    n = len(distancias)
    
    # Calcular cota inferior usando MST
    def calcular_cota_inferior(visitados, nivel):
        cota = 0
        
        # Costo del camino actual
        for i in range(nivel):
            cota += distancias[visitados[i]][visitados[i + 1]]
        
        # Estimar costo restante con aristas mínimas
        for i in range(n):
            if i not in visitados[:nivel + 1]:
                min_arista = float('inf')
                for j in range(n):
                    if i != j and j not in visitados[:nivel + 1]:
                        min_arista = min(min_arista, distancias[i][j])
                if min_arista != float('inf'):
                    cota += min_arista
        
        return cota
    
    # Inicializar
    mejor_costo = float('inf')
    mejor_tour = None
    
    # Cola de prioridad: (cota, nivel, tour, visitados_set)
    pq = [(0, 0, [0], {0})]
    
    while pq:
        cota, nivel, tour, visitados_set = heapq.heappop(pq)
        
        # Poda: si la cota es peor que la mejor solución, descartar
        if cota >= mejor_costo:
            continue
        
        # Si visitamos todas las ciudades
        if nivel == n - 1:
            # Completar el tour volviendo al inicio
            costo_total = cota + distancias[tour[-1]][0]
            if costo_total < mejor_costo:
                mejor_costo = costo_total
                mejor_tour = tour + [0]
            continue
        
        # Ramificar: probar cada ciudad no visitada
        ciudad_actual = tour[-1]
        for siguiente in range(n):
            if siguiente not in visitados_set:
                nuevo_tour = tour + [siguiente]
                nuevo_visitados = visitados_set | {siguiente}
                nuevo_costo = cota + distancias[ciudad_actual][siguiente]
                nueva_cota = calcular_cota_inferior(nuevo_tour, nivel + 1)
                
                # Solo agregar si la cota es prometedora
                if nueva_cota < mejor_costo:
                    heapq.heappush(pq, 
                                  (nueva_cota, nivel + 1, nuevo_tour, nuevo_visitados))
    
    return mejor_tour, mejor_costo

# Uso
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour, costo = tsp_branch_bound(distancias)
print(f"Mejor tour: {tour}")
print(f"Costo: {costo}")
```

### Ejemplo 2: Mochila 0/1

```python
def mochila_branch_bound(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila 0/1 con B&B.
    
    Complejidad: O(2^n) con poda efectiva
    """
    n = len(pesos)
    
    # Calcular relación valor/peso
    items = [(valores[i]/pesos[i], pesos[i], valores[i], i) 
             for i in range(n)]
    items.sort(reverse=True)
    
    class Nodo:
        def __init__(self, nivel, peso, valor, incluidos):
            self.nivel = nivel
            self.peso = peso
            self.valor = valor
            self.incluidos = incluidos
            self.cota = 0
    
    def calcular_cota_superior(nodo):
        """Calcula cota superior usando enfoque voraz fraccionario."""
        if nodo.peso >= capacidad:
            return 0
        
        cota = nodo.valor
        nivel = nodo.nivel + 1
        peso_total = nodo.peso
        
        # Agregar items completos mientras quepan
        while nivel < n and peso_total + items[nivel][1] <= capacidad:
            peso_total += items[nivel][1]
            cota += items[nivel][2]
            nivel += 1
        
        # Agregar fracción del siguiente item
        if nivel < n:
            cota += (capacidad - peso_total) * items[nivel][0]
        
        return cota
    
    # Inicializar
    mejor_valor = 0
    mejor_solucion = []
    
    # Cola de prioridad: (-cota, nodo)
    raiz = Nodo(-1, 0, 0, [])
    raiz.cota = calcular_cota_superior(raiz)
    pq = [(-raiz.cota, raiz)]
    
    while pq:
        _, nodo = heapq.heappop(pq)
        
        # Poda: si la cota no mejora la mejor solución
        if nodo.cota <= mejor_valor:
            continue
        
        # Si llegamos al final
        if nodo.nivel == n - 1:
            if nodo.valor > mejor_valor:
                mejor_valor = nodo.valor
                mejor_solucion = nodo.incluidos[:]
            continue
        
        nivel = nodo.nivel + 1
        
        # Ramificar: incluir el item
        if nodo.peso + items[nivel][1] <= capacidad:
            incluir = Nodo(
                nivel,
                nodo.peso + items[nivel][1],
                nodo.valor + items[nivel][2],
                nodo.incluidos + [items[nivel][3]]
            )
            incluir.cota = calcular_cota_superior(incluir)
            
            if incluir.cota > mejor_valor:
                if incluir.valor > mejor_valor:
                    mejor_valor = incluir.valor
                    mejor_solucion = incluir.incluidos[:]
                heapq.heappush(pq, (-incluir.cota, incluir))
        
        # Ramificar: no incluir el item
        no_incluir = Nodo(
            nivel,
            nodo.peso,
            nodo.valor,
            nodo.incluidos[:]
        )
        no_incluir.cota = calcular_cota_superior(no_incluir)
        
        if no_incluir.cota > mejor_valor:
            heapq.heappush(pq, (-no_incluir.cota, no_incluir))
    
    return mejor_valor, mejor_solucion

# Uso
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 8]
capacidad = 8

valor_max, items_sel = mochila_branch_bound(pesos, valores, capacidad)
print(f"Valor máximo: {valor_max}")
print(f"Items seleccionados (índices): {sorted(items_sel)}")
```

### Ejemplo 3: Asignación de Tareas

```python
def asignacion_tareas(costos):
    """
    Asigna n tareas a n trabajadores minimizando costo total.
    
    Args:
        costos: Matriz donde costos[i][j] = costo de asignar 
                trabajador i a tarea j
    
    Returns:
        Asignación óptima y costo mínimo
    """
    n = len(costos)
    
    class Nodo:
        def __init__(self, nivel, asignacion, costo, disponibles):
            self.nivel = nivel
            self.asignacion = asignacion
            self.costo = costo
            self.disponibles = disponibles
            self.cota = 0
    
    def calcular_cota_inferior(nodo):
        """Calcula cota inferior sumando mínimos de filas restantes."""
        cota = nodo.costo
        
        # Para cada trabajador no asignado
        for trabajador in range(nodo.nivel + 1, n):
            # Agregar costo mínimo de tareas disponibles
            min_costo = float('inf')
            for tarea in nodo.disponibles:
                min_costo = min(min_costo, costos[trabajador][tarea])
            cota += min_costo
        
        return cota
    
    # Inicializar
    mejor_costo = float('inf')
    mejor_asignacion = None
    
    # Cola de prioridad
    raiz = Nodo(-1, [], 0, set(range(n)))
    raiz.cota = calcular_cota_inferior(raiz)
    pq = [(raiz.cota, raiz)]
    
    while pq:
        _, nodo = heapq.heappop(pq)
        
        # Poda
        if nodo.cota >= mejor_costo:
            continue
        
        # Solución completa
        if nodo.nivel == n - 1:
            if nodo.costo < mejor_costo:
                mejor_costo = nodo.costo
                mejor_asignacion = nodo.asignacion[:]
            continue
        
        # Ramificar: asignar siguiente trabajador a cada tarea disponible
        trabajador = nodo.nivel + 1
        for tarea in nodo.disponibles:
            nuevo_nodo = Nodo(
                trabajador,
                nodo.asignacion + [(trabajador, tarea)],
                nodo.costo + costos[trabajador][tarea],
                nodo.disponibles - {tarea}
            )
            nuevo_nodo.cota = calcular_cota_inferior(nuevo_nodo)
            
            if nuevo_nodo.cota < mejor_costo:
                heapq.heappush(pq, (nuevo_nodo.cota, nuevo_nodo))
    
    return mejor_asignacion, mejor_costo

# Uso
costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

asignacion, costo = asignacion_tareas(costos)
print(f"Asignación óptima:")
for trabajador, tarea in asignacion:
    print(f"  Trabajador {trabajador} → Tarea {tarea}")
print(f"Costo total: {costo}")
```

### Ejemplo 4: Conjunto Independiente Máximo

```python
def conjunto_independiente_maximo(grafo):
    """
    Encuentra el conjunto independiente más grande en un grafo.
    Un conjunto independiente es un conjunto de vértices
    donde ningún par está conectado.
    
    Args:
        grafo: Diccionario {vértice: [vecinos]}
    
    Returns:
        Conjunto independiente máximo
    """
    vertices = list(grafo.keys())
    n = len(vertices)
    
    def calcular_cota_superior(nivel, conjunto_actual, excluidos):
        """Cota superior: incluir todos los vértices posibles."""
        # Vértices que aún podemos considerar
        candidatos = set(vertices[nivel:]) - excluidos
        
        # Construir vorazmente
        voraz = set(conjunto_actual)
        excluidos_voraz = set(excluidos)
        
        for v in candidatos:
            if v not in excluidos_voraz:
                voraz.add(v)
                excluidos_voraz.update(grafo[v])
        
        return len(voraz)
    
    mejor_conjunto = set()
    mejor_tamano = 0
    
    def branch_bound(nivel, conjunto_actual, excluidos):
        nonlocal mejor_conjunto, mejor_tamano
        
        # Caso base
        if nivel == n:
            if len(conjunto_actual) > mejor_tamano:
                mejor_tamano = len(conjunto_actual)
                mejor_conjunto = set(conjunto_actual)
            return
        
        # Poda: cota superior
        cota = calcular_cota_superior(nivel, conjunto_actual, excluidos)
        if cota <= mejor_tamano:
            return
        
        vertice = vertices[nivel]
        
        # Opción 1: incluir el vértice (si no está excluido)
        if vertice not in excluidos:
            conjunto_actual.add(vertice)
            nuevos_excluidos = excluidos | set(grafo[vertice])
            branch_bound(nivel + 1, conjunto_actual, nuevos_excluidos)
            conjunto_actual.remove(vertice)
        
        # Opción 2: no incluir el vértice
        branch_bound(nivel + 1, conjunto_actual, excluidos)
    
    branch_bound(0, set(), set())
    return mejor_conjunto

# Uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

conjunto = conjunto_independiente_maximo(grafo)
print(f"Conjunto independiente máximo: {conjunto}")
print(f"Tamaño: {len(conjunto)}")
```

## 🎓 Estrategias de Búsqueda

### Best-First Search (Mejor Primero)
```python
# Usar heap con prioridad por mejor cota
pq = []
heapq.heappush(pq, (cota, nodo))
```

### LIFO (Pila - DFS)
```python
# Usar pila para búsqueda en profundidad
stack = [nodo_raiz]
```

### FIFO (Cola - BFS)
```python
# Usar cola para búsqueda en anchura
from collections import deque
queue = deque([nodo_raiz])
```

## 🎓 Ejercicios Propuestos

1. **Set Cover:** Encontrar el mínimo número de conjuntos que cubran todos los elementos

2. **Bin Packing:** Empacar items en el mínimo número de contenedores

3. **Coloración de Grafos Óptima:** Encontrar el número cromático de un grafo

4. **Job Scheduling con Deadlines:** Maximizar beneficio programando trabajos

5. **Max Clique:** Encontrar la clique más grande en un grafo

## ⚡ Técnicas de Mejora

### 1. Mejores Funciones de Cota
Cotas más ajustadas resultan en mejor poda.

### 2. Ordenamiento Inteligente
Explorar nodos más prometedores primero.

### 3. Preprocesamiento
Reducir el problema antes de aplicar B&B.

### 4. Soluciones Iniciales
Usar heurísticas para obtener una buena solución inicial.

## 📊 Complejidad

- **Peor caso:** Igual que fuerza bruta (exponencial)
- **Caso promedio:** Mucho mejor gracias a la poda
- **Espacio:** O(profundidad del árbol)

## 🔗 Recursos Adicionales

- [Branch and Bound Tutorial](https://www.geeksforgeeks.org/branch-and-bound-algorithm/)
- [Optimización Combinatoria](https://en.wikipedia.org/wiki/Combinatorial_optimization)

## ⏭️ Siguiente Módulo

Continúa con [Algoritmos Probabilísticos](../07_Algoritmos_Probabilisticos/README.md) para explorar técnicas con aleatoriedad.

---

[⬅️ Volver al índice principal](../README.md)
