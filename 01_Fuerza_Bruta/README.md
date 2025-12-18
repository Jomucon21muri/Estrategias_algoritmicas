# 1️⃣ Fuerza Bruta (Brute Force)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Jomucon21muri/Estrategias_algoritmicas/blob/main/01_Fuerza_Bruta/fuerza_bruta_ejemplo.ipynb)

## 📖 Introducción 

La **Fuerza Bruta** es la estrategia algorítmica más simple e intuitiva. Consiste en explorar todas las posibles soluciones de un problema de manera exhaustiva hasta encontrar la solución correcta o la solución óptima.

## 🎯 Características Principales

- ✅ **Garantía de solución:** Si existe una solución, la fuerza bruta la encontrará
- ⚠️ **Ineficiencia:** Generalmente tiene complejidad temporal muy alta
- 📝 **Simplicidad:** Fácil de implementar y entender
- 🔍 **Exhaustiva:** Explora todo el espacio de soluciones

## 📊 Análisis de complejidad

| Tipo de Problema | Complejidad Temporal | Complejidad Espacial |
|-----------------|---------------------|---------------------|
| Búsqueda lineal | O(n) | O(1) |
| Generación de subconjuntos | O(2ⁿ) | O(n) |
| Generación de permutaciones | O(n!) | O(n) |
| Búsqueda en matriz | O(n²) | O(1) |

## 🔑 Cuándo Usar Fuerza Bruta

1. **Espacios de búsqueda pequeños:** Cuando el número de posibilidades es manejable
2. **Prototipos y validación:** Para verificar la corrección de algoritmos más complejos
3. **Sin alternativa conocida:** Cuando no existe un algoritmo más eficiente
4. **Problemas únicos:** Para problemas que se resuelven una sola vez

## 💡 Ejemplos Clásicos

### 1. Búsqueda Lineal
Buscar un elemento en una lista no ordenada recorriendo todos los elementos.

### 2. Generación de Contraseñas
Probar todas las combinaciones posibles de caracteres.

### 3. Problema del Viajante (TSP)
Generar todas las permutaciones de rutas y elegir la más corta.

### 4. Subconjuntos y Combinaciones
Generar todos los subconjuntos posibles de un conjunto.

## 📂 Estructura de Este Módulo

```
01_Fuerza_Bruta/
├── README.md (este archivo)
├── ejemplos/
│   ├── busqueda_lineal.py
│   ├── generacion_subconjuntos.py
│   ├── generacion_permutaciones.py
│   └── suma_subconjunto.py
├── ejercicios/
│   ├── ejercicio_01.md
│   ├── ejercicio_02.md
│   └── ejercicio_03.md
└── soluciones/
    ├── solucion_01.py
    ├── solucion_02.py
    └── solucion_03.py
```

## 🚀 Ejemplos de Código

### Ejemplo 1: Búsqueda Lineal

```python
def busqueda_lineal(lista, objetivo):
    """
    Busca un elemento en una lista de forma secuencial.
    Complejidad: O(n)
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Retorna el índice donde se encuentra
    return -1  # No encontrado

# Uso
numeros = [4, 2, 7, 1, 9, 5]
resultado = busqueda_lineal(numeros, 7)
print(f"Elemento encontrado en índice: {resultado}")
```

### Ejemplo 2: Generación de Subconjuntos

```python
def generar_subconjuntos(conjunto):
    """
    Genera todos los subconjuntos de un conjunto.
    Complejidad: O(2^n)
    """
    n = len(conjunto)
    subconjuntos = []
    
    # Hay 2^n subconjuntos posibles
    for i in range(2**n):
        subconjunto = []
        for j in range(n):
            # Verificar si el j-ésimo bit está activado
            if (i >> j) & 1:
                subconjunto.append(conjunto[j])
        subconjuntos.append(subconjunto)
    
    return subconjuntos

# Uso
conjunto = [1, 2, 3]
subconjuntos = generar_subconjuntos(conjunto)
print(f"Subconjuntos: {subconjuntos}")
# Resultado: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```

### Ejemplo 3: Problema de la Suma de Subconjunto

```python
def suma_subconjunto(numeros, objetivo):
    """
    Encuentra todos los subconjuntos cuya suma es igual al objetivo.
    Complejidad: O(2^n)
    """
    n = len(numeros)
    soluciones = []
    
    for i in range(2**n):
        subconjunto = []
        suma = 0
        for j in range(n):
            if (i >> j) & 1:
                subconjunto.append(numeros[j])
                suma += numeros[j]
        
        if suma == objetivo:
            soluciones.append(subconjunto)
    
    return soluciones

# Uso
numeros = [1, 2, 3, 4, 5]
objetivo = 7
soluciones = suma_subconjunto(numeros, objetivo)
print(f"Subconjuntos que suman {objetivo}: {soluciones}")
```

## ⚡ Optimizaciones Posibles

Aunque la fuerza bruta es inherentemente ineficiente, se puede mejorar con:

1. **Poda temprana:** Detener la búsqueda cuando se encuentra una solución
2. **Ordenamiento previo:** Ordenar los datos puede permitir terminación temprana
3. **Paralelización:** Dividir el espacio de búsqueda entre múltiples procesadores
4. **Caché de resultados:** Almacenar resultados parciales (transición a DP)

## 🎓 Ejercicios Propuestos

1. **Búsqueda de Máximo:** Implementar un algoritmo de fuerza bruta para encontrar el elemento máximo en una lista.

2. **Par con Suma Objetivo:** Encontrar todos los pares de números en un array que sumen un valor objetivo.

3. **Producto Máximo:** Encontrar el producto máximo de k elementos en un array.

4. **Palíndromo más Largo:** Encontrar el palíndromo más largo en una cadena usando fuerza bruta.

5. **Coloración de Grafos:** Determinar si un grafo puede ser coloreado con k colores (versión fuerza bruta).

## 🔗 Recursos Adicionales

- [Visualización de Algoritmos de Búsqueda](https://visualgo.net)
- [Complejidad Computacional](https://en.wikipedia.org/wiki/Time_complexity)

## ⏭️ Siguiente Módulo

Una vez domines la fuerza bruta, continúa con [Dividir y Conquistar](../02_Dividir_y_Conquistar/README.md), donde aprenderás a descomponer problemas de manera más eficiente.

---

[⬅️ Volver al índice principal](../README.md)
