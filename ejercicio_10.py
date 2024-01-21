"""10. Halle el interés simple ganado de un capital C durante cierto tiempo,usando la
siguiente fórmula: Interés = (C*i*t). Donde C es el capital,i es el porcentaje de interés
ganado mensualmente y t es la cantidad de años que el capital está aumentando
"""
capital = float(input("Ingrese el capital (C): "))
tasa_interes = float(input("Ingrese la tasa de interés mensual (en decimal): "))
tiempo_anios = int(input("Ingrese la cantidad de años (t): "))

interes_simple = capital * tasa_interes * tiempo_anios


print(f"El interés simple ganado es: {interes_simple}")
