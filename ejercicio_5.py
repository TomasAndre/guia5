"""5. Calcule la distancia entre dos puntos en un plano cartesiano.
Usa la siguiente fórmula raiz-Cuadrada((x2-x1)^2+ (y2-y1)^2 ) Punto1 = x1,y1, Punto2
= x2,y2"""

x1, y1 = 1, 2
x2, y2 = 4, 6

distancia_entre_puntos = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia_entre_puntos}")
