# Una función para calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=17):
    descuento = (monto_total * porcentaje_descuento) / 100  # Calculamos el descuento
    return descuento

# Llamada 1: Solo monto total, se usa el descuento del 17%
monto_total1 = 500
descuento1 = calcular_descuento(monto_total1)  # Descuento de 17%
monto_final1 = monto_total1 - descuento1  # Monto final después del descuento
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}")

# Llamada 2: Monto total y un porcentaje de descuento (15%)
monto_total2 = 500
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)  # Descuento de 15%
monto_final2 = monto_total2 - descuento2  # Monto final después del descuento
print(f"\nDescuento aplicado: ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")