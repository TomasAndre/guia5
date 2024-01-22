"""12. Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado
por la suma de los precios de costos, los porcentajes de ganancia del vendedor y un
21% de IVA. Supóngase una ganancia del vendedor del 12% por la PC y 7% por la
impresora. Se leen los costos y se imprimen el precio total de ventas"""

costo_pc = float(input("Ingrese el costo de la PC: "))
costo_impresora = float(input("Ingrese el costo de la impresora: "))

ganancia_pc = 0.12  # 12% de ganancia para la PC
ganancia_impresora = 0.07  # 7% de ganancia para la impresora

precio_pc = costo_pc * (1 + ganancia_pc)
precio_impresora = costo_impresora * (1 + ganancia_impresora)

precio_total = precio_pc + precio_impresora + 0.21 * (precio_pc + precio_impresora)

print(f"El precio total de venta es: {precio_total}")
