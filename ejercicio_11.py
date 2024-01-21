"""11. Escribir un programa que permita calcular el precio de un artículo para un año dado,
considerando que la inflación es del 4 por 100 anual.
La fórmula del precio es: P = C * (1+R) ^ (N - A)
C - Precio actual. R - Tasa de Inflación.
N - Año futuro.    A - Año actual."""

precio_actual = float(input("Ingrese el precio actual del artículo: "))
ano_actual = int(input("Ingrese el año actual: "))
ano_futuro = int(input("Ingrese el año futuro para calcular el precio: "))

tasa_inflacion = 0.04  # 4% de inflación anual

precio_futuro = precio_actual * (1 + tasa_inflacion) ** (ano_futuro - ano_actual)

print(f"El precio estimado del artículo en el año {ano_futuro} es: {precio_futuro}")
