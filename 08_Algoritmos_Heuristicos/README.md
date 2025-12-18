# 8️⃣ Algoritmos Heurísticos (Heuristic Algorithms)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/08_Algoritmos_Heuristicos/algoritmos_heuristicos_ejemplo.ipynb)

## 📖 Introducción

Los **Algoritmos Heurísticos** son técnicas de resolución de problemas que buscan soluciones de buena calidad en tiempo razonable, sin garantizar la optimalidad. Son especialmente útiles para problemas NP-difíciles donde encontrar la solución óptima es computacionalmente intratable.

## 🎯 Características Principales

- 🎯 **Aproximación:** Buscan soluciones "suficientemente buenas"
- ⚡ **Eficiencia:** Tiempo polinomial o razonable
- 🚫 **Sin garantía de optimalidad:** Pueden no encontrar el óptimo global
- 🔍 **Metaheurísticas:** Estrategias generales aplicables a múltiples problemas

## 📊 Clasificación de Heurísticas

### 1. Heurísticas Constructivas
Construyen soluciones desde cero de manera incremental.

### 2. Heurísticas de Búsqueda Local
Mejoran iterativamente una solución inicial.

### 3. Metaheurísticas
Estrategias de alto nivel que guían otras heurísticas:
- Algoritmos Genéticos
- Recocido Simulado
- Búsqueda Tabú
- Algoritmos de Colonia de Hormigas
- Particle Swarm Optimization

## 💡 Problemas Clásicos

### 1. Problema del Viajante (TSP)
Encontrar tour aproximado de mínima distancia.

### 2. Problema de la Mochila
Selección aproximada de items.

### 3. Scheduling
Programación de tareas con restricciones.

### 4. Coloración de Grafos
Colorear con mínimo número de colores.

### 5. Bin Packing
Empacar items en mínimo número de contenedores.

## 📂 Estructura de Este Módulo

```
08_Algoritmos_Heuristicos/
├── README.md
├── ejemplos/
│   ├── algoritmo_genetico.py
│   ├── recocido_simulado.py
│   ├── busqueda_tabu.py
│   ├── colonia_hormigas.py
│   └── busqueda_local.py
├── ejercicios/
└── soluciones/
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Algoritmo Genético

```python
import random
from typing import List, Callable

class AlgoritmoGenetico:
    """
    Algoritmo Genético para optimización.
    
    Inspirado en la evolución biológica:
    - Selección natural
    - Cruce (crossover)
    - Mutación
    """
    
    def __init__(self, 
                 tamano_poblacion: int,
                 tasa_mutacion: float,
                 tasa_cruce: float,
                 generaciones: int):
        self.tamano_poblacion = tamano_poblacion
        self.tasa_mutacion = tasa_mutacion
        self.tasa_cruce = tasa_cruce
        self.generaciones = generaciones
    
    def inicializar_poblacion(self, crear_individuo: Callable) -> List:
        """Crea población inicial aleatoria."""
        return [crear_individuo() for _ in range(self.tamano_poblacion)]
    
    def seleccion_torneo(self, poblacion: List, fitness: Callable, k=3) -> any:
        """Selecciona individuo mediante torneo."""
        torneo = random.sample(poblacion, k)
        return max(torneo, key=fitness)
    
    def cruce_un_punto(self, padre1: List, padre2: List) -> tuple:
        """Cruce de un punto entre dos padres."""
        if random.random() > self.tasa_cruce:
            return padre1[:], padre2[:]
        
        punto = random.randint(1, len(padre1) - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2
    
    def mutar(self, individuo: List, mutar_gen: Callable):
        """Aplica mutación a un individuo."""
        for i in range(len(individuo)):
            if random.random() < self.tasa_mutacion:
                individuo[i] = mutar_gen(individuo[i])
        return individuo
    
    def evolucionar(self, 
                   crear_individuo: Callable,
                   fitness: Callable,
                   mutar_gen: Callable) -> tuple:
        """
        Ejecuta el algoritmo genético.
        
        Returns:
            Mejor individuo encontrado y su fitness
        """
        # Inicializar población
        poblacion = self.inicializar_poblacion(crear_individuo)
        mejor_historico = None
        mejor_fitness = float('-inf')
        
        # Evolucionar generaciones
        for gen in range(self.generaciones):
            # Evaluar fitness
            fitness_scores = [(ind, fitness(ind)) for ind in poblacion]
            fitness_scores.sort(key=lambda x: x[1], reverse=True)
            
            # Actualizar mejor
            if fitness_scores[0][1] > mejor_fitness:
                mejor_fitness = fitness_scores[0][1]
                mejor_historico = fitness_scores[0][0][:]
            
            # Crear nueva generación
            nueva_poblacion = []
            
            # Elitismo: mantener mejores individuos
            elite_size = self.tamano_poblacion // 10
            nueva_poblacion.extend([ind for ind, _ in fitness_scores[:elite_size]])
            
            # Generar resto por selección, cruce y mutación
            while len(nueva_poblacion) < self.tamano_poblacion:
                padre1 = self.seleccion_torneo(poblacion, fitness)
                padre2 = self.seleccion_torneo(poblacion, fitness)
                
                hijo1, hijo2 = self.cruce_un_punto(padre1, padre2)
                
                hijo1 = self.mutar(hijo1, mutar_gen)
                hijo2 = self.mutar(hijo2, mutar_gen)
                
                nueva_poblacion.extend([hijo1, hijo2])
            
            poblacion = nueva_poblacion[:self.tamano_poblacion]
        
        return mejor_historico, mejor_fitness

# Ejemplo: Problema de la Mochila
def resolver_mochila_genetico(pesos, valores, capacidad):
    """Resuelve problema de la mochila con AG."""
    n = len(pesos)
    
    def crear_individuo():
        return [random.randint(0, 1) for _ in range(n)]
    
    def fitness(individuo):
        peso_total = sum(p * g for p, g in zip(pesos, individuo))
        valor_total = sum(v * g for v, g in zip(valores, individuo))
        
        # Penalizar si excede capacidad
        if peso_total > capacidad:
            return 0
        return valor_total
    
    def mutar_gen(gen):
        return 1 - gen  # Flip bit
    
    ag = AlgoritmoGenetico(
        tamano_poblacion=100,
        tasa_mutacion=0.01,
        tasa_cruce=0.8,
        generaciones=100
    )
    
    mejor, fitness_val = ag.evolucionar(crear_individuo, fitness, mutar_gen)
    return mejor, fitness_val

# Uso
pesos = [10, 20, 30, 40, 50]
valores = [20, 30, 50, 60, 70]
capacidad = 100

solucion, valor = resolver_mochila_genetico(pesos, valores, capacidad)
print(f"Mejor solución: {solucion}")
print(f"Valor: {valor}")
print(f"Peso: {sum(p*s for p, s in zip(pesos, solucion))}")
```

### Ejemplo 2: Recocido Simulado (Simulated Annealing)

```python
import math
import random

def recocido_simulado(solucion_inicial,
                      vecino,
                      costo,
                      temp_inicial=1000,
                      temp_final=1,
                      alpha=0.95,
                      iteraciones_por_temp=100):
    """
    Algoritmo de Recocido Simulado.
    
    Inspirado en el proceso de recocido en metalurgia.
    Acepta soluciones peores con probabilidad que decrece con la temperatura.
    
    Args:
        solucion_inicial: Solución de partida
        vecino: Función que genera vecino de una solución
        costo: Función de costo (minimizar)
        temp_inicial: Temperatura inicial
        temp_final: Temperatura final
        alpha: Factor de enfriamiento (0 < alpha < 1)
        iteraciones_por_temp: Iteraciones en cada temperatura
    
    Returns:
        Mejor solución encontrada
    """
    solucion_actual = solucion_inicial
    costo_actual = costo(solucion_actual)
    
    mejor_solucion = solucion_actual
    mejor_costo = costo_actual
    
    temperatura = temp_inicial
    
    while temperatura > temp_final:
        for _ in range(iteraciones_por_temp):
            # Generar vecino
            solucion_vecina = vecino(solucion_actual)
            costo_vecino = costo(solucion_vecina)
            
            # Calcular diferencia de costo
            delta = costo_vecino - costo_actual
            
            # Decidir si aceptar el vecino
            if delta < 0:
                # Mejor solución, siempre aceptar
                solucion_actual = solucion_vecina
                costo_actual = costo_vecino
                
                # Actualizar mejor global
                if costo_actual < mejor_costo:
                    mejor_solucion = solucion_actual
                    mejor_costo = costo_actual
            else:
                # Peor solución, aceptar con probabilidad
                probabilidad = math.exp(-delta / temperatura)
                if random.random() < probabilidad:
                    solucion_actual = solucion_vecina
                    costo_actual = costo_vecino
        
        # Enfriar
        temperatura *= alpha
    
    return mejor_solucion, mejor_costo

# Ejemplo: TSP con Recocido Simulado
def tsp_recocido_simulado(distancias):
    """Resuelve TSP aproximadamente con recocido simulado."""
    n = len(distancias)
    
    # Solución inicial: tour aleatorio
    solucion_inicial = list(range(n))
    random.shuffle(solucion_inicial)
    
    def costo_tour(tour):
        """Calcula longitud total del tour."""
        costo = 0
        for i in range(len(tour)):
            costo += distancias[tour[i]][tour[(i + 1) % len(tour)]]
        return costo
    
    def vecino_2opt(tour):
        """Genera vecino usando 2-opt swap."""
        nuevo_tour = tour[:]
        i, j = sorted(random.sample(range(n), 2))
        # Revertir segmento entre i y j
        nuevo_tour[i:j+1] = reversed(nuevo_tour[i:j+1])
        return nuevo_tour
    
    mejor_tour, mejor_costo = recocido_simulado(
        solucion_inicial,
        vecino_2opt,
        costo_tour,
        temp_inicial=100,
        temp_final=0.1,
        alpha=0.99,
        iteraciones_por_temp=100
    )
    
    return mejor_tour, mejor_costo

# Uso
distancias = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tour, costo = tsp_recocido_simulado(distancias)
print(f"Tour aproximado: {tour}")
print(f"Costo: {costo}")
```

### Ejemplo 3: Búsqueda Tabú

```python
from collections import deque

def busqueda_tabu(solucion_inicial,
                 vecinos,
                 costo,
                 tamano_tabu=10,
                 max_iteraciones=1000,
                 max_sin_mejora=100):
    """
    Algoritmo de Búsqueda Tabú.
    
    Mantiene una lista de movimientos prohibidos (tabú)
    para evitar ciclos y explorar mejor el espacio de soluciones.
    
    Args:
        solucion_inicial: Solución de partida
        vecinos: Función que genera todos los vecinos
        costo: Función de costo
        tamano_tabu: Tamaño de la lista tabú
        max_iteraciones: Máximo número de iteraciones
        max_sin_mejora: Máximo iteraciones sin mejora antes de terminar
    
    Returns:
        Mejor solución encontrada
    """
    solucion_actual = solucion_inicial
    costo_actual = costo(solucion_actual)
    
    mejor_solucion = solucion_actual
    mejor_costo = costo_actual
    
    lista_tabu = deque(maxlen=tamano_tabu)
    iteraciones_sin_mejora = 0
    
    for iteracion in range(max_iteraciones):
        # Generar vecinos
        vecinos_candidatos = vecinos(solucion_actual)
        
        # Filtrar vecinos tabú y encontrar el mejor
        mejor_vecino = None
        mejor_costo_vecino = float('inf')
        mejor_movimiento = None
        
        for vecino, movimiento in vecinos_candidatos:
            # Permitir movimiento tabú si mejora el mejor global (criterio de aspiración)
            if movimiento not in lista_tabu or costo(vecino) < mejor_costo:
                costo_vecino = costo(vecino)
                if costo_vecino < mejor_costo_vecino:
                    mejor_vecino = vecino
                    mejor_costo_vecino = costo_vecino
                    mejor_movimiento = movimiento
        
        if mejor_vecino is None:
            break
        
        # Moverse al mejor vecino
        solucion_actual = mejor_vecino
        costo_actual = mejor_costo_vecino
        lista_tabu.append(mejor_movimiento)
        
        # Actualizar mejor solución
        if costo_actual < mejor_costo:
            mejor_solucion = solucion_actual
            mejor_costo = costo_actual
            iteraciones_sin_mejora = 0
        else:
            iteraciones_sin_mejora += 1
        
        # Criterio de parada por estancamiento
        if iteraciones_sin_mejora >= max_sin_mejora:
            break
    
    return mejor_solucion, mejor_costo

# Ejemplo: Problema de Asignación
def asignacion_busqueda_tabu(costos):
    """Resuelve problema de asignación con búsqueda tabú."""
    n = len(costos)
    
    # Solución inicial: asignación aleatoria
    solucion_inicial = list(range(n))
    random.shuffle(solucion_inicial)
    
    def costo_asignacion(asignacion):
        return sum(costos[i][asignacion[i]] for i in range(n))
    
    def generar_vecinos(asignacion):
        """Genera vecinos intercambiando dos posiciones."""
        vecinos = []
        for i in range(n):
            for j in range(i + 1, n):
                vecino = asignacion[:]
                vecino[i], vecino[j] = vecino[j], vecino[i]
                movimiento = (i, j)  # Identificador del movimiento
                vecinos.append((vecino, movimiento))
        return vecinos
    
    mejor, costo_mejor = busqueda_tabu(
        solucion_inicial,
        generar_vecinos,
        costo_asignacion,
        tamano_tabu=20,
        max_iteraciones=500
    )
    
    return mejor, costo_mejor

# Uso
costos_asignacion = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

asignacion, costo_total = asignacion_busqueda_tabu(costos_asignacion)
print(f"Asignación: {asignacion}")
print(f"Costo total: {costo_total}")
```

### Ejemplo 4: Colonia de Hormigas (Ant Colony Optimization)

```python
import random

class ACO_TSP:
    """
    Algoritmo de Colonia de Hormigas para TSP.
    
    Inspirado en el comportamiento de hormigas reales
    que encuentran caminos usando feromonas.
    """
    
    def __init__(self, distancias, num_hormigas, num_iteraciones,
                 alpha=1.0, beta=2.0, evaporacion=0.5, Q=100):
        """
        Args:
            distancias: Matriz de distancias
            num_hormigas: Número de hormigas
            num_iteraciones: Número de iteraciones
            alpha: Importancia de feromonas
            beta: Importancia de visibilidad (heurística)
            evaporacion: Tasa de evaporación de feromonas
            Q: Constante para depositar feromonas
        """
        self.distancias = distancias
        self.n = len(distancias)
        self.num_hormigas = num_hormigas
        self.num_iteraciones = num_iteraciones
        self.alpha = alpha
        self.beta = beta
        self.evaporacion = evaporacion
        self.Q = Q
        
        # Inicializar feromonas
        self.feromonas = [[1.0 for _ in range(self.n)] 
                         for _ in range(self.n)]
    
    def resolver(self):
        """Ejecuta el algoritmo ACO."""
        mejor_tour = None
        mejor_longitud = float('inf')
        
        for iteracion in range(self.num_iteraciones):
            # Construir tours para todas las hormigas
            tours = []
            for _ in range(self.num_hormigas):
                tour = self.construir_tour()
                longitud = self.calcular_longitud(tour)
                tours.append((tour, longitud))
                
                if longitud < mejor_longitud:
                    mejor_longitud = longitud
                    mejor_tour = tour
            
            # Actualizar feromonas
            self.actualizar_feromonas(tours)
        
        return mejor_tour, mejor_longitud
    
    def construir_tour(self):
        """Una hormiga construye un tour."""
        tour = [random.randint(0, self.n - 1)]
        visitados = set(tour)
        
        while len(tour) < self.n:
            actual = tour[-1]
            siguiente = self.seleccionar_siguiente(actual, visitados)
            tour.append(siguiente)
            visitados.add(siguiente)
        
        return tour
    
    def seleccionar_siguiente(self, actual, visitados):
        """Selecciona la siguiente ciudad usando probabilidades."""
        no_visitados = [i for i in range(self.n) if i not in visitados]
        
        # Calcular probabilidades
        probabilidades = []
        for ciudad in no_visitados:
            feromona = self.feromonas[actual][ciudad] ** self.alpha
            visibilidad = (1.0 / self.distancias[actual][ciudad]) ** self.beta
            probabilidades.append(feromona * visibilidad)
        
        # Normalizar
        total = sum(probabilidades)
        probabilidades = [p / total for p in probabilidades]
        
        # Selección por ruleta
        r = random.random()
        acumulado = 0
        for i, prob in enumerate(probabilidades):
            acumulado += prob
            if r <= acumulado:
                return no_visitados[i]
        
        return no_visitados[-1]
    
    def calcular_longitud(self, tour):
        """Calcula la longitud de un tour."""
        longitud = 0
        for i in range(len(tour)):
            longitud += self.distancias[tour[i]][tour[(i + 1) % len(tour)]]
        return longitud
    
    def actualizar_feromonas(self, tours):
        """Actualiza la matriz de feromonas."""
        # Evaporación
        for i in range(self.n):
            for j in range(self.n):
                self.feromonas[i][j] *= (1 - self.evaporacion)
        
        # Depositar nuevas feromonas
        for tour, longitud in tours:
            deposito = self.Q / longitud
            for i in range(len(tour)):
                ciudad1 = tour[i]
                ciudad2 = tour[(i + 1) % len(tour)]
                self.feromonas[ciudad1][ciudad2] += deposito
                self.feromonas[ciudad2][ciudad1] += deposito

# Uso
distancias_tsp = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

aco = ACO_TSP(
    distancias=distancias_tsp,
    num_hormigas=10,
    num_iteraciones=100,
    alpha=1.0,
    beta=2.0,
    evaporacion=0.5
)

tour_optimo, longitud = aco.resolver()
print(f"Tour encontrado: {tour_optimo}")
print(f"Longitud: {longitud}")
```

## 🎓 Comparación de Metaheurísticas

| Algoritmo | Inspiración | Exploración | Explotación | Mejor Para |
|-----------|-------------|-------------|-------------|------------|
| AG | Evolución | Alta | Media | Espacios discretos grandes |
| Recocido Simulado | Física | Alta inicial | Alta final | Optimización continua |
| Búsqueda Tabú | Memoria | Media | Alta | Problemas combinatorios |
| Colonia Hormigas | Naturaleza | Media | Alta | TSP, routing |

## 🎓 Ejercicios Propuestos

1. **Hill Climbing:** Implementar búsqueda local simple

2. **Particle Swarm Optimization:** Optimización inspirada en aves

3. **VNS (Variable Neighborhood Search):** Búsqueda en vecindades variables

4. **GRASP:** Greedy Randomized Adaptive Search Procedure

5. **Evolución Diferencial:** Variante de algoritmo evolutivo

## ⚡ Consejos de Diseño

### 1. Balance Exploración-Explotación
- Exploración: buscar nuevas regiones
- Explotación: refinar soluciones conocidas

### 2. Representación Adecuada
Elegir representación que facilite operadores.

### 3. Parámetros
Ajustar parámetros experimentalmente.

### 4. Criterios de Parada
- Número de iteraciones
- Tiempo límite
- Convergencia
- Calidad de solución

## 📊 Garantías de Aproximación

Algunos algoritmos heurísticos tienen **garantías de aproximación**:

$$\frac{Solución\ Heurística}{Solución\ Óptima} \leq \rho$$

Ejemplo: El algoritmo voraz para Vertex Cover tiene $\rho = 2$.

## 🔗 Recursos Adicionales

- [Metaheuristics Network](http://www.metaheuristics.org/)
- [ACO Bibliography](http://www.aco-metaheuristic.org/)
- [Genetic Algorithms Tutorial](https://en.wikipedia.org/wiki/Genetic_algorithm)

## 🎯 Conclusión del Curso

¡Felicitaciones por completar el curso de Estrategias Algorítmicas! Has aprendido:

1. ✅ Fuerza Bruta - Base conceptual
2. ✅ Dividir y Conquistar - Divide y vencerás
3. ✅ Programación Dinámica - Optimización con memoria
4. ✅ Algoritmos Voraces - Decisiones locales óptimas
5. ✅ Backtracking - Búsqueda exhaustiva inteligente
6. ✅ Ramificación y Acotación - Optimización con podas
7. ✅ Algoritmos Probabilísticos - Poder de la aleatoriedad
8. ✅ Algoritmos Heurísticos - Soluciones prácticas

### Próximos Pasos

- Practicar en plataformas como LeetCode, Codeforces
- Participar en competencias de programación
- Aplicar estos conocimientos a problemas reales
- Estudiar algoritmos avanzados específicos de tu dominio

---

[⬅️ Volver al índice principal](../README.md)
