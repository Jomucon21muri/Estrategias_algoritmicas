# 7️⃣ Algoritmos Probabilísticos (Randomized Algorithms)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/07_Algoritmos_Probabilisticos/algoritmos_probabilisticos_ejemplo.ipynb)

## 📖 Introducción

Los **Algoritmos Probabilísticos** o **Aleatorios** utilizan números aleatorios como parte de su lógica para tomar decisiones. Estos algoritmos sacrifican determinismo por eficiencia o simplicidad.

## 🎯 Características Principales

- 🎲 **Aleatoriedad:** Usan generación de números aleatorios
- ⚡ **Eficiencia:** A menudo más rápidos que alternativas deterministas
- 📊 **Garantías probabilísticas:** Corrección o tiempo esperado
- 🔄 **No determinista:** Diferentes ejecuciones pueden dar resultados distintos

## 📊 Clasificación

### 1. Algoritmos Las Vegas
- **Siempre correctos**
- Tiempo de ejecución variable (esperado)
- Ejemplos: QuickSort aleatorio, RP (Randomized Polynomial)

### 2. Algoritmos Monte Carlo
- **Tiempo fijo**
- Posibilidad de error controlada
- Ejemplos: Test de primalidad, estimación de π

## 💡 Ventajas de la Aleatoriedad

| Ventaja | Descripción |
|---------|-------------|
| Simplicidad | Algoritmos más simples que versiones deterministas |
| Eficiencia | Mejor complejidad esperada |
| Evitar peor caso | Aleatoriedad previene inputs adversarios |
| Aproximación | Buenos resultados rápidamente |

## 🎲 Problemas Clásicos

### 1. QuickSort Aleatorio
Versión aleatoria de QuickSort que evita el peor caso.

### 2. Test de Primalidad de Miller-Rabin
Determinar si un número es primo probabilísticamente.

### 3. Algoritmo de Karger para Min-Cut
Encontrar el corte mínimo en un grafo.

### 4. Estimación de π (Monte Carlo)
Estimar π usando puntos aleatorios.

### 5. Algoritmo de Bloom Filter
Estructura de datos probabilística para pertenencia a conjuntos.

## 📂 Estructura de Este Módulo

```
07_Algoritmos_Probabilisticos/
├── README.md
├── ejemplos/
│   ├── quicksort_aleatorio.py
│   ├── miller_rabin.py
│   ├── monte_carlo_pi.py
│   ├── karger_min_cut.py
│   └── bloom_filter.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: QuickSort Aleatorio (Las Vegas)

```python
import random

def quicksort_aleatorio(arr):
    """
    QuickSort con pivote aleatorio.
    
    Tipo: Las Vegas (siempre correcto)
    Complejidad esperada: O(n log n)
    Complejidad peor caso: O(n²) pero muy improbable
    """
    if len(arr) <= 1:
        return arr
    
    # Elegir pivote aleatorio
    pivote_idx = random.randint(0, len(arr) - 1)
    pivote = arr[pivote_idx]
    
    # Particionar
    menores = [x for x in arr if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr if x > pivote]
    
    # Recursión
    return quicksort_aleatorio(menores) + iguales + quicksort_aleatorio(mayores)

# Versión in-place
def quicksort_aleatorio_inplace(arr, inicio=0, fin=None):
    """Versión in-place de QuickSort aleatorio."""
    if fin is None:
        fin = len(arr) - 1
    
    if inicio >= fin:
        return
    
    # Particionar con pivote aleatorio
    pivote_idx = partition_aleatorio(arr, inicio, fin)
    
    # Recursión
    quicksort_aleatorio_inplace(arr, inicio, pivote_idx - 1)
    quicksort_aleatorio_inplace(arr, pivote_idx + 1, fin)

def partition_aleatorio(arr, inicio, fin):
    """Particiona con pivote aleatorio."""
    # Elegir pivote aleatorio y moverlo al final
    pivote_idx = random.randint(inicio, fin)
    arr[pivote_idx], arr[fin] = arr[fin], arr[pivote_idx]
    
    # Particionar estándar
    pivote = arr[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    return i + 1

# Uso
numeros = [3, 7, 8, 5, 2, 1, 9, 5, 4]
ordenados = quicksort_aleatorio(numeros)
print(f"Array ordenado: {ordenados}")
```

### Ejemplo 2: Test de Primalidad Miller-Rabin (Monte Carlo)

```python
import random

def miller_rabin(n, k=5):
    """
    Test de primalidad probabilístico de Miller-Rabin.
    
    Tipo: Monte Carlo
    Args:
        n: Número a verificar
        k: Número de iteraciones (más iteraciones = mayor certeza)
    
    Returns:
        True si n es probablemente primo
        False si n es definitivamente compuesto
    
    Probabilidad de error: ≤ (1/4)^k
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Escribir n-1 como 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Realizar k iteraciones
    for _ in range(k):
        # Elegir testigo aleatorio
        a = random.randint(2, n - 2)
        
        # Calcular a^d mod n
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        # Elevar al cuadrado r-1 veces
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # n es compuesto
    
    return True  # n es probablemente primo

# Función auxiliar para verificar
def es_primo(n, iteraciones=10):
    """Wrapper con más iteraciones para mayor certeza."""
    return miller_rabin(n, iteraciones)

# Uso
numeros_prueba = [17, 19, 20, 97, 100, 561, 1009]
for num in numeros_prueba:
    resultado = es_primo(num)
    print(f"{num}: {'Probablemente primo' if resultado else 'Compuesto'}")
```

### Ejemplo 3: Estimación de π (Monte Carlo)

```python
import random
import math

def estimar_pi(num_puntos):
    """
    Estima π usando el método de Monte Carlo.
    
    Principio: Relación entre área de círculo y cuadrado
    π ≈ 4 * (puntos dentro del círculo / puntos totales)
    
    Tipo: Monte Carlo
    Complejidad: O(n)
    Error: O(1/√n)
    """
    puntos_dentro = 0
    
    for _ in range(num_puntos):
        # Generar punto aleatorio en [0,1] × [0,1]
        x = random.random()
        y = random.random()
        
        # Verificar si está dentro del círculo unitario
        if x**2 + y**2 <= 1:
            puntos_dentro += 1
    
    # Estimar π
    pi_estimado = 4 * puntos_dentro / num_puntos
    return pi_estimado

def estimar_pi_con_varianza(num_puntos, num_experimentos=10):
    """Realiza múltiples experimentos y calcula estadísticas."""
    estimaciones = [estimar_pi(num_puntos) for _ in range(num_experimentos)]
    
    promedio = sum(estimaciones) / num_experimentos
    varianza = sum((x - promedio)**2 for x in estimaciones) / num_experimentos
    desv_std = math.sqrt(varianza)
    
    return promedio, desv_std, estimaciones

# Uso
print("Estimación de π usando Monte Carlo:")
for n in [100, 1000, 10000, 100000]:
    pi_est = estimar_pi(n)
    error = abs(pi_est - math.pi)
    print(f"n={n:6d}: π ≈ {pi_est:.6f}, error = {error:.6f}")

print("\nCon múltiples experimentos:")
promedio, desv, _ = estimar_pi_con_varianza(10000, 20)
print(f"Promedio: {promedio:.6f}")
print(f"Desv. estándar: {desv:.6f}")
print(f"π real: {math.pi:.6f}")
```

### Ejemplo 4: Algoritmo de Karger (Min-Cut)

```python
import random
from copy import deepcopy

class Grafo:
    def __init__(self):
        self.vertices = {}
    
    def agregar_arista(self, u, v):
        if u not in self.vertices:
            self.vertices[u] = []
        if v not in self.vertices:
            self.vertices[v] = []
        self.vertices[u].append(v)
        self.vertices[v].append(u)
    
    def contraer_arista(self, u, v):
        """Contrae la arista u-v, fusionando v en u."""
        # Reemplazar todas las ocurrencias de v por u
        for vecino in self.vertices[v]:
            if vecino != u:
                self.vertices[vecino] = [u if x == v else x 
                                        for x in self.vertices[vecino]]
                self.vertices[u].append(vecino)
        
        # Eliminar auto-loops
        self.vertices[u] = [x for x in self.vertices[u] if x != u]
        
        # Eliminar v
        del self.vertices[v]
    
    def num_aristas_entre(self, u, v):
        """Cuenta aristas entre dos super-nodos."""
        if v not in self.vertices:
            return 0
        return self.vertices[u].count(v)

def karger_min_cut(grafo_original):
    """
    Encuentra un corte mínimo usando el algoritmo de Karger.
    
    Tipo: Monte Carlo (Las Vegas con repeticiones)
    Probabilidad de éxito por iteración: ≥ 1/n²
    
    Args:
        grafo_original: Grafo representado como objeto Grafo
    
    Returns:
        Tamaño del corte mínimo encontrado
    """
    grafo = deepcopy(grafo_original)
    
    # Mientras haya más de 2 vértices
    while len(grafo.vertices) > 2:
        # Elegir arista aleatoria
        u = random.choice(list(grafo.vertices.keys()))
        if not grafo.vertices[u]:
            continue
        v = random.choice(grafo.vertices[u])
        
        # Contraer la arista
        grafo.contraer_arista(u, v)
    
    # Contar aristas entre los dos super-nodos restantes
    vertices_finales = list(grafo.vertices.keys())
    if len(vertices_finales) >= 2:
        return len(grafo.vertices[vertices_finales[0]])
    return 0

def karger_min_cut_repetido(grafo, num_iteraciones=None):
    """
    Ejecuta Karger múltiples veces para aumentar probabilidad de éxito.
    
    Con O(n² log n) iteraciones, probabilidad de éxito > 1 - 1/n
    """
    n = len(grafo.vertices)
    if num_iteraciones is None:
        num_iteraciones = n * n * 2  # O(n²) iteraciones
    
    min_corte = float('inf')
    
    for _ in range(num_iteraciones):
        corte = karger_min_cut(grafo)
        min_corte = min(min_corte, corte)
    
    return min_corte

# Uso
g = Grafo()
aristas = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4)]
for u, v in aristas:
    g.agregar_arista(u, v)

corte_min = karger_min_cut_repetido(g)
print(f"Corte mínimo: {corte_min}")
```

### Ejemplo 5: Bloom Filter

```python
import hashlib

class BloomFilter:
    """
    Filtro de Bloom: estructura probabilística para test de pertenencia.
    
    Tipo: Monte Carlo
    - Nunca falsos negativos (si dice "no", es definitivo)
    - Posibles falsos positivos (si dice "sí", es probable)
    """
    
    def __init__(self, tamano, num_hashes):
        """
        Args:
            tamano: Tamaño del array de bits
            num_hashes: Número de funciones hash
        """
        self.tamano = tamano
        self.num_hashes = num_hashes
        self.bits = [0] * tamano
    
    def _hashes(self, item):
        """Genera múltiples valores hash."""
        hashes = []
        for i in range(self.num_hashes):
            # Usar diferentes seeds para cada función hash
            h = hashlib.sha256(f"{item}{i}".encode())
            hash_val = int(h.hexdigest(), 16) % self.tamano
            hashes.append(hash_val)
        return hashes
    
    def agregar(self, item):
        """Agrega un elemento al filtro."""
        for h in self._hashes(item):
            self.bits[h] = 1
    
    def contiene(self, item):
        """
        Verifica si un elemento posiblemente está en el conjunto.
        
        Returns:
            True: elemento posiblemente está (puede ser falso positivo)
            False: elemento definitivamente NO está
        """
        return all(self.bits[h] == 1 for h in self._hashes(item))
    
    def tasa_falsos_positivos(self):
        """Estima la tasa de falsos positivos actual."""
        bits_activos = sum(self.bits)
        return (bits_activos / self.tamano) ** self.num_hashes

# Uso
bf = BloomFilter(tamano=1000, num_hashes=3)

# Agregar elementos
palabras = ["hola", "mundo", "python", "algoritmo"]
for palabra in palabras:
    bf.agregar(palabra)

# Verificar pertenencia
pruebas = ["hola", "adios", "python", "java", "algoritmo"]
print("Resultados del Bloom Filter:")
for palabra in pruebas:
    resultado = bf.contiene(palabra)
    real = palabra in palabras
    print(f"{palabra:10s}: {'Posiblemente está' if resultado else 'No está':20s} (real: {real})")

print(f"\nTasa estimada de falsos positivos: {bf.tasa_falsos_positivos():.4f}")
```

## 🎓 Análisis de Complejidad Esperada

Para algoritmos probabilísticos, analizamos:

1. **Tiempo esperado:** E[T(n)]
2. **Probabilidad de error:** Pr[error]
3. **Número de iteraciones:** Para reducir error

### Ejemplo: Miller-Rabin

- Una iteración: Pr[error] ≤ 1/4
- k iteraciones: Pr[error] ≤ (1/4)^k
- Para error < 10^-9: k ≥ 15 iteraciones

## 🎓 Ejercicios Propuestos

1. **Skip List:** Implementar lista enlazada probabilística

2. **Algoritmo de Freivalds:** Verificación probabilística de multiplicación de matrices

3. **Reservorio Sampling:** Selección aleatoria de k elementos de stream

4. **Algoritmo de Las Vegas para SAT:** Resolver 2-SAT probabilísticamente

5. **Count-Min Sketch:** Estructura para estimar frecuencias

## ⚡ Amplificación de Probabilidad

Para reducir probabilidad de error:

```python
def amplificar(algoritmo_monte_carlo, input, k):
    """Ejecuta algoritmo k veces y toma mayoría."""
    votos = []
    for _ in range(k):
        resultado = algoritmo_monte_carlo(input)
        votos.append(resultado)
    
    # Retornar el resultado más común
    return max(set(votos), key=votos.count)
```

## 📊 Comparación

| Aspecto | Determinista | Las Vegas | Monte Carlo |
|---------|-------------|-----------|-------------|
| Corrección | 100% | 100% | Probabilística |
| Tiempo | Fijo/Peor caso | Esperado | Fijo |
| Uso | General | Optimización | Verificación |

## 🔗 Recursos Adicionales

- [Randomized Algorithms](https://en.wikipedia.org/wiki/Randomized_algorithm)
- [Probabilistic Data Structures](https://www.enjoyalgorithms.com/blog/bloom-filter)

## ⏭️ Siguiente Módulo

Finaliza con [Algoritmos Heurísticos](../08_Algoritmos_Heuristicos/README.md) para explorar técnicas de aproximación.

---

[⬅️ Volver al índice principal](../README.md)
