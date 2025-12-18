# 📚 Estrategias Algorítmicas

Repositorio dedicado a la implementación y estudio de los principales modelos de estrategia algorítmica para la resolución de problemas computacionales. Incluye ejemplos en código y pseudocódigo de estrategias como fuerza bruta, divide y vencerás, voraces, programación dinámica, vuelta atrás y ramificación y poda; análisis básicos de complejidad.

## 🎯 Objetivo

Este repositorio proporciona una guía completa para aprender y dominar las estrategias algorítmicas más importantes en ciencias de la computación. Cada módulo incluye:
- 📖 Teoría y conceptos fundamentales
- 💻 Ejemplos de código en Python
- 🧩 Problemas resueltos
- 📊 Análisis de complejidad
- 🔍 Casos de uso prácticos

---

## 📑 Contenido del Curso

> 💡 **Cada módulo incluye un notebook interactivo de Google Colab** - ¡Haz clic en el badge para ejecutar ejemplos en tu navegador!

### [1️⃣ Fuerza Bruta](01_Fuerza_Bruta/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/01_Fuerza_Bruta/fuerza_bruta_ejemplo.ipynb)

Estrategia que explora todas las posibles soluciones de forma exhaustiva.
- Búsqueda exhaustiva
- Generación de combinaciones y permutaciones
- Problemas de optimización
- **Complejidad:** Generalmente exponencial O(2ⁿ), O(n!)

### [2️⃣ Dividir y Conquistar](02_Dividir_y_Conquistar/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/02_Dividir_y_Conquistar/dividir_conquistar_ejemplo.ipynb)

Descompone un problema en subproblemas más pequeños, los resuelve recursivamente y combina sus soluciones.
- MergeSort y QuickSort
- Búsqueda binaria
- Multiplicación de matrices de Strassen
- **Complejidad:** Frecuentemente O(n log n)

### [3️⃣ Programación Dinámica](03_Programacion_Dinamica/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/03_Programacion_Dinamica/programacion_dinamica_ejemplo.ipynb)

Resuelve problemas complejos dividiéndolos en subproblemas superpuestos y almacenando sus soluciones.
- Memoización (top-down)
- Tabulación (bottom-up)
- Problemas clásicos: Fibonacci, mochila, subsecuencia común más larga
- **Complejidad:** Mejora exponencial a polinomial

### [4️⃣ Algoritmos Voraces (Greedy)](04_Algoritmos_Voraces/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/04_Algoritmos_Voraces/algoritmos_voraces_ejemplo.ipynb)

Toma la mejor decisión local en cada paso con la esperanza de encontrar un óptimo global.
- Selección de actividades
- Algoritmo de Dijkstra
- Códigos de Huffman
- Problema del cambio de monedas
- **Complejidad:** Generalmente O(n log n) o mejor

### [5️⃣ Backtracking (Vuelta Atrás)](05_Backtracking/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/05_Backtracking/backtracking_ejemplo.ipynb)

Explora sistemáticamente todas las posibilidades mediante búsqueda con retroceso.
- Problema de las N reinas
- Sudoku
- Coloración de grafos
- Generación de soluciones
- **Complejidad:** Exponencial pero con poda

### [6️⃣ Ramificación y Acotación (Branch and Bound)](06_Ramificacion_y_Acotacion/README.md)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/06_Ramificacion_y_Acotacion/ramificacion_acotacion_ejemplo.ipynb)

Explora el espacio de soluciones mediante un árbol y poda ramas que no pueden dar soluciones óptimas.
- Problema del viajante (TSP)
- Problema de la mochila 0/1
- Asignación de tareas
- **Complejidad:** Exponencial optimizado con cotas
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/07_Algoritmos_Probabilisticos/algoritmos_probabilisticos_ejemplo.ipynb)


### [7️⃣ Algoritmos Probabilísticos](07_Algoritmos_Probabilisticos/README.md)
Utilizan aleatoriedad para resolver problemas de manera eficiente.
- Algoritmos Las Vegas
- Algoritmos Monte Carlo
- QuickSort aleatorio
- Test de primalidad
- **Complejidad:** Variable, a menudo con garantías probabilísticas
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/08_Algoritmos_Heuristicos/algoritmos_heuristicos_ejemplo.ipynb)


### [8️⃣ Algoritmos Heurísticos](08_Algoritmos_Heuristicos/README.md)
Estrategias que encuentran soluciones aproximadas de buena calidad en tiempo razonable.
- Algoritmos genéticos
- Recocido simulado (Simulated Annealing)
- Búsqueda tabú
- Colonia de hormigas
- **Complejidad:** Polinomial con soluciones aproximadas

---

## 🚀 Cómo Usar Este Repositorio

1. **Orden Sugerido:** Se recomienda seguir el orden numérico de los módulos, ya que cada uno construye sobre conceptos anteriores.

2. **Estructura de Cada Módulo:**
   - `README.md`: Teoría y explicaciones
   - `ejemplos/`: Código de ejemplo comentado
   - `ejercicios/`: Problemas para practicar
   - `soluciones/`: Soluciones a los ejercicios

3. **Requisitos:**
   - Python 3.8 o superior
   - Conocimientos básicos de estructuras de datos
   - Comprensión de análisis de complejidad

---

## 📖 Recursos Adicionales

- **Libros Recomendados:**
  - "Introduction to Algorithms" - Cormen, Leiserson, Rivest, Stein
  - "Algorithm Design" - Kleinberg, Tardos
  - "The Algorithm Design Manual" - Steven Skiena

- **Plataformas de Práctica:**
  - LeetCode
  - HackerRank
  - Codeforces
  - AtCoder

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas agregar ejemplos, corregir errores o mejorar las explicaciones, por favor:
1. Haz un fork del repositorio
2. Crea una rama para tu característica
3. Realiza un pull request

---

## 📝 Licencia

Este repositorio está bajo licencia MIT. Siéntete libre de usar el material para aprendizaje personal o educativo.

---

## 📧 Contacto

Para preguntas o sugerencias, abre un issue en este repositorio.

**¡Feliz aprendizaje! 🎓**
