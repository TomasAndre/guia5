"""8. Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo
+34-913724710-56). Escribir un programa que pregunte por un número de teléfono con
este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

numero_telefono = input("Ingrese el número de teléfono con formato +34-XXXXXXXXX-XX: ")

partes = numero_telefono.split("-")

numero_principal = partes[1]

print(f"El número de teléfono sin prefijo y extensión es: {numero_principal}")
