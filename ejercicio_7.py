"""7. Escribir un programa que pregunte el nombre del usuario en la consola y después de
que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
<NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que
tienen el nombre.
"""

nombre = str(input("ingrese su nombre: "))

letras_nombre = len(nombre)

print(f"{nombre.upper()} tiene {letras_nombre} letras")