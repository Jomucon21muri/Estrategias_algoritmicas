# 4️⃣ Algoritmos Voraces (Greedy Algorithms)

## 📖 Introducción

Los **Algoritmos Voraces** (Greedy) toman decisiones óptimas locales en cada paso con la esperanza de encontrar un óptimo global. A diferencia de la programación dinámica, no reconsideran decisiones previas.

## 🎯 Características Principales

- 🎯 **Elección voraz:** Selecciona la mejor opción en cada momento
- ⚡ **Eficiencia:** Generalmente más rápidos que DP
- 🚫 **Irrevocable:** Las decisiones no se revierten
- ⚠️ **No siempre óptimo:** Solo funciona en problemas específicos

## 🔑 Propiedades Necesarias

### 1. Propiedad de Elección Voraz
Una solución óptima global se puede construir haciendo elecciones locales óptimas.

### 2. Subestructura Óptima
Una solución óptima contiene soluciones óptimas de subproblemas.

## 📊 Comparación con Otras Estrategias

| Aspecto | Voraz | Programación Dinámica | Fuerza Bruta |
|---------|-------|---------------------|--------------|
| Decisiones | Irrevocables | Reversibles | Todas |
| Optimalidad | A veces | Siempre (si aplica) | Siempre |
| Complejidad | Menor | Media | Mayor |
| Ejemplo | Dijkstra | Mochila 0/1 | TSP exhaustivo |

## 💡 Problemas Clásicos

### 1. Selección de Actividades
Seleccionar el máximo número de actividades compatibles.

### 2. Algoritmo de Dijkstra
Encontrar el camino más corto desde un nodo origen.

### 3. Algoritmo de Kruskal
Encontrar el árbol de expansión mínimo.

### 4. Códigos de Huffman
Compresión de datos mediante codificación óptima.

### 5. Problema del Cambio (casos específicos)
Dar cambio con el mínimo número de monedas.

## 📂 Estructura de Este Módulo

```
04_Algoritmos_Voraces/
├── README.md
├── ejemplos/
│   ├── seleccion_actividades.py
│   ├── dijkstra.py
│   ├── kruskal.py
│   ├── huffman.py
│   └── cambio_monedas.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Selección de Actividades

```python
def seleccion_actividades(actividades):
    """
    Selecciona el máximo número de actividades que no se superponen.
    
    Args:
        actividades: Lista de tuplas (inicio, fin, nombre)
    
    Returns:
        Lista de actividades seleccionadas
    
    Complejidad: O(n log n) por el ordenamiento
    """
    # Ordenar por tiempo de finalización
    actividades_ordenadas = sorted(actividades, key=lambda x: x[1])
    
    seleccionadas = []
    tiempo_fin_actual = 0
    
    for inicio, fin, nombre in actividades_ordenadas:
        # Si la actividad no se superpone con la anterior
        if inicio >= tiempo_fin_actual:
            seleccionadas.append((inicio, fin, nombre))
            tiempo_fin_actual = fin
    
    return seleccionadas

# Uso
actividades = [
    (1, 4, "A1"),
    (3, 5, "A2"),
    (0, 6, "A3"),
    (5, 7, "A4"),
    (3, 9, "A5"),
    (5, 9, "A6"),
    (6, 10, "A7"),
    (8, 11, "A8"),
    (8, 12, "A9"),
    (2, 14, "A10"),
    (12, 16, "A11")
]

resultado = seleccion_actividades(actividades)
print("Actividades seleccionadas:")
for inicio, fin, nombre in resultado:
    print(f"{nombre}: [{inicio}, {fin}]")
```

### Ejemplo 2: Algoritmo de Dijkstra

```python
import heapq

def dijkstra(grafo, inicio):
    """
    Encuentra los caminos más cortos desde un nodo inicial.
    
    Args:
        grafo: Diccionario {nodo: [(vecino, peso), ...]}
        inicio: Nodo inicial
    
    Returns:
        Diccionario con distancias mínimas a cada nodo
    
    Complejidad: O((V + E) log V) con heap
    """
    # Inicializar distancias
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    
    # Cola de prioridad: (distancia, nodo)
    pq = [(0, inicio)]
    visitados = set()
    
    while pq:
        dist_actual, nodo_actual = heapq.heappop(pq)
        
        if nodo_actual in visitados:
            continue
        
        visitados.add(nodo_actual)
        
        # Explorar vecinos
        for vecino, peso in grafo.get(nodo_actual, []):
            distancia_nueva = dist_actual + peso
            
            # Si encontramos un camino más corto
            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                heapq.heappush(pq, (distancia_nueva, vecino))
    
    return distancias

# Uso
grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}

distancias = dijkstra(grafo, 'A')
print("Distancias desde A:")
for nodo, dist in sorted(distancias.items()):
    print(f"{nodo}: {dist}")
```

### Ejemplo 3: Algoritmo de Kruskal (MST)

```python
class UnionFind:
    """Estructura de datos Union-Find para detectar ciclos."""
    
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n
    
    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]
    
    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)
        
        if raiz_x == raiz_y:
            return False
        
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1
        
        return True

def kruskal(num_nodos, aristas):
    """
    Encuentra el árbol de expansión mínimo.
    
    Args:
        num_nodos: Número de nodos en el grafo
        aristas: Lista de tuplas (peso, nodo1, nodo2)
    
    Returns:
        Lista de aristas en el MST y peso total
    
    Complejidad: O(E log E)
    """
    # Ordenar aristas por peso
    aristas_ordenadas = sorted(aristas, key=lambda x: x[0])
    
    uf = UnionFind(num_nodos)
    mst = []
    peso_total = 0
    
    for peso, u, v in aristas_ordenadas:
        # Si no forma ciclo, agregar la arista
        if uf.union(u, v):
            mst.append((peso, u, v))
            peso_total += peso
            
            # Si ya tenemos n-1 aristas, terminamos
            if len(mst) == num_nodos - 1:
                break
    
    return mst, peso_total

# Uso
aristas = [
    (1, 0, 1),
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]

mst, peso = kruskal(4, aristas)
print(f"Árbol de Expansión Mínimo (peso total: {peso}):")
for p, u, v in mst:
    print(f"Arista {u}-{v}: peso {p}")
```

### Ejemplo 4: Códigos de Huffman

```python
import heapq
from collections import defaultdict, Counter

class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierdo = None
        self.derecho = None
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(texto):
    """
    Construye el árbol de Huffman para un texto.
    
    Complejidad: O(n log n)
    """
    # Contar frecuencias
    frecuencias = Counter(texto)
    
    # Crear heap con nodos hoja
    heap = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(heap)
    
    # Construir árbol
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        
        padre = NodoHuffman(None, izq.frecuencia + der.frecuencia)
        padre.izquierdo = izq
        padre.derecho = der
        
        heapq.heappush(heap, padre)
    
    return heap[0]

def generar_codigos(raiz, codigo_actual="", codigos=None):
    """Genera los códigos de Huffman para cada carácter."""
    if codigos is None:
        codigos = {}
    
    if raiz is None:
        return codigos
    
    # Nodo hoja
    if raiz.caracter is not None:
        codigos[raiz.caracter] = codigo_actual or "0"
        return codigos
    
    # Recursión
    generar_codigos(raiz.izquierdo, codigo_actual + "0", codigos)
    generar_codigos(raiz.derecho, codigo_actual + "1", codigos)
    
    return codigos

def codificar_huffman(texto):
    """Codifica un texto usando Huffman."""
    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos(arbol)
    
    texto_codificado = ''.join(codigos[char] for char in texto)
    
    return texto_codificado, codigos, arbol

# Uso
texto = "ABRACADABRA"
codificado, codigos, arbol = codificar_huffman(texto)

print("Códigos de Huffman:")
for char, codigo in sorted(codigos.items()):
    print(f"{char}: {codigo}")
print(f"\nTexto original: {texto}")
print(f"Texto codificado: {codificado}")
print(f"Compresión: {len(texto)*8} bits → {len(codificado)} bits")
```

### Ejemplo 5: Cambio de Monedas (Voraz)

```python
def cambio_voraz(monedas, cantidad):
    """
    Devuelve el cambio usando estrategia voraz.
    
    NOTA: Solo garantiza solución óptima para sistemas
    de monedas canónicos (como USD, EUR).
    
    Complejidad: O(n) donde n = len(monedas)
    """
    # Ordenar monedas en orden descendente
    monedas_ordenadas = sorted(monedas, reverse=True)
    
    cambio = []
    cantidad_restante = cantidad
    
    for moneda in monedas_ordenadas:
        # Usar tantas monedas de este valor como sea posible
        while cantidad_restante >= moneda:
            cambio.append(moneda)
            cantidad_restante -= moneda
    
    if cantidad_restante > 0:
        return None  # No se puede dar cambio exacto
    
    return cambio

# Uso - Sistema canónico (funciona)
monedas = [25, 10, 5, 1]
cantidad = 63
cambio = cambio_voraz(monedas, cantidad)
print(f"Cambio para {cantidad}: {cambio}")
print(f"Número de monedas: {len(cambio)}")

# Contraejemplo - Sistema no canónico (no óptimo)
monedas_nc = [10, 7, 1]
cantidad_nc = 14
cambio_nc = cambio_voraz(monedas_nc, cantidad_nc)
print(f"\nCambio voraz para {cantidad_nc}: {cambio_nc} ({len(cambio_nc)} monedas)")
print("Solución óptima sería: [7, 7] (2 monedas)")
```

## 🎓 Ejercicios Propuestos

1. **Problema de la Mochila Fraccionaria:** Variante donde se pueden tomar fracciones de items

2. **Problema de Intervalos Ponderados:** Selección de actividades con beneficios diferentes

3. **Minimizar Latencia:** Programar tareas para minimizar latencia máxima

4. **Algoritmo de Prim:** Otra forma de encontrar MST

5. **Asignación de Salones:** Asignar el mínimo número de salones para conferencias

## ⚡ Cuándo NO Usar Algoritmos Voraces

Los algoritmos voraces NO funcionan en:

```python
# Problema de la mochila 0/1
# Voraz (por valor/peso) no es óptimo
pesos = [10, 20, 30]
valores = [60, 100, 120]
capacidad = 50
# Voraz elegiría item 3 (120/30), no óptimo
# Óptimo: items 1 y 2 (160 total)

# Sistema de monedas no canónico
monedas = [10, 7, 1]
cantidad = 14
# Voraz: 10+1+1+1+1 = 5 monedas
# Óptimo: 7+7 = 2 monedas
```

## 🔍 Cómo Verificar Corrección

Para demostrar que un algoritmo voraz es correcto:

1. **Elección voraz:** Demostrar que la elección local óptima lleva a solución global óptima
2. **Subestructura óptima:** Demostrar que después de la elección voraz, el subproblema resultante tiene la misma forma
3. **Inducción/contradicción:** Probar formalmente la corrección

## 🔗 Recursos Adicionales

- [Greedy Algorithms - CP-Algorithms](https://cp-algorithms.com/schedules/greedy.html)
- [Visualización de Dijkstra](https://visualgo.net/en/sssp)

## ⏭️ Siguiente Módulo

Continúa con [Backtracking](../05_Backtracking/README.md) para aprender búsqueda exhaustiva con poda.

---

[⬅️ Volver al índice principal](../README.md)
