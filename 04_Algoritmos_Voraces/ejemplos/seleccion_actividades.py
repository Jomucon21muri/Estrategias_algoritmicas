"""
Ejemplo: Selección de Actividades (Algoritmo Voraz)

Problema: Dada una lista de actividades con tiempos de inicio y fin,
seleccionar el máximo número de actividades que no se superpongan.

Estrategia Voraz: Ordenar por tiempo de finalización y
siempre seleccionar la actividad que termine primero.

Complejidad: O(n log n) debido al ordenamiento
"""

def seleccion_actividades(actividades):
    """
    Selecciona el máximo número de actividades no superpuestas.
    
    Args:
        actividades: Lista de tuplas (inicio, fin, nombre)
    
    Returns:
        Lista de actividades seleccionadas
    
    Estrategia Voraz:
    1. Ordenar por tiempo de finalización
    2. Seleccionar siempre la actividad que termina primero
    3. Solo aceptar actividades que no se superpongan con la última
    """
    if not actividades:
        return []
    
    # Ordenar por tiempo de finalización (decisión voraz clave)
    actividades_ordenadas = sorted(actividades, key=lambda x: x[1])
    
    seleccionadas = []
    tiempo_fin_actual = 0
    
    for inicio, fin, nombre in actividades_ordenadas:
        # Si la actividad no se superpone con la anterior
        if inicio >= tiempo_fin_actual:
            seleccionadas.append((inicio, fin, nombre))
            tiempo_fin_actual = fin
            print(f"  ✓ Seleccionada: {nombre} [{inicio}, {fin}]")
        else:
            print(f"  ✗ Rechazada:    {nombre} [{inicio}, {fin}] (conflicto)")
    
    return seleccionadas


def seleccion_actividades_ponderadas(actividades_con_valor):
    """
    Variante: cuando las actividades tienen valores diferentes.
    NOTA: Este problema requiere Programación Dinámica, no voraz.
    
    Este es un ejemplo de cuándo NO usar algoritmo voraz.
    """
    # Ordenar por tiempo de fin
    actividades = sorted(actividades_con_valor, key=lambda x: x[1])
    n = len(actividades)
    
    # DP: dp[i] = máximo valor usando actividades 0..i
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        inicio, fin, nombre, valor = actividades[i - 1]
        
        # Opción 1: no tomar esta actividad
        no_tomar = dp[i - 1]
        
        # Opción 2: tomar esta actividad
        # Encontrar última actividad compatible
        j = i - 1
        while j > 0 and actividades[j - 1][1] > inicio:
            j -= 1
        
        tomar = valor + dp[j]
        
        dp[i] = max(no_tomar, tomar)
    
    return dp[n]


def visualizar_cronograma(actividades, seleccionadas):
    """Visualiza el cronograma de actividades."""
    print("\n" + "="*60)
    print("CRONOGRAMA DE ACTIVIDADES")
    print("="*60)
    
    # Encontrar el rango de tiempo
    max_tiempo = max(act[1] for act in actividades)
    
    print("\nTiempo: ", end="")
    for t in range(0, max_tiempo + 1):
        print(f"{t:2d}", end=" ")
    print()
    print("-" * (max_tiempo * 3 + 10))
    
    for inicio, fin, nombre in sorted(actividades):
        seleccionada = (inicio, fin, nombre) in seleccionadas
        simbolo = "█" if seleccionada else "░"
        
        print(f"{nombre:6s}: ", end="")
        for t in range(0, max_tiempo + 1):
            if inicio <= t < fin:
                print(f"{simbolo:>2s}", end=" ")
            else:
                print("  ", end=" ")
        
        estado = " ✓ SELECCIONADA" if seleccionada else ""
        print(estado)
    
    print("="*60)


def main():
    # Conjunto de actividades: (inicio, fin, nombre)
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
    
    print("PROBLEMA: Selección de Actividades")
    print("="*60)
    print("Objetivo: Seleccionar el máximo número de actividades")
    print("          que no se superpongan\n")
    
    print("Actividades disponibles:")
    for inicio, fin, nombre in sorted(actividades):
        print(f"  {nombre}: [{inicio:2d}, {fin:2d}]")
    
    print("\n" + "="*60)
    print("APLICANDO ALGORITMO VORAZ")
    print("="*60)
    print("Estrategia: Ordenar por tiempo de fin, seleccionar la que")
    print("           termina primero entre las compatibles\n")
    
    resultado = seleccion_actividades(actividades)
    
    print(f"\n{'='*60}")
    print(f"RESULTADO: {len(resultado)} actividades seleccionadas")
    print(f"{'='*60}")
    for inicio, fin, nombre in resultado:
        print(f"  {nombre}: [{inicio}, {fin}]")
    
    # Visualizar
    visualizar_cronograma(actividades, resultado)
    
    # Ejemplo de caso no voraz
    print("\n" + "="*60)
    print("NOTA: Actividades Ponderadas NO se resuelve con voraz")
    print("="*60)
    actividades_valor = [
        (0, 3, "A1", 5),
        (1, 4, "A2", 10),
        (3, 6, "A3", 7)
    ]
    print("Si las actividades tienen valores diferentes,")
    print("la estrategia voraz NO garantiza solución óptima.")
    print("\nEjemplo:")
    for inicio, fin, nombre, valor in actividades_valor:
        print(f"  {nombre}: [{inicio}, {fin}] valor={valor}")
    print("\nVoraz elegiría A1 (termina primero)")
    print("Óptimo sería A2 (valor 10 > 5)")


if __name__ == "__main__":
    main()
