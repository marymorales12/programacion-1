#Tarea semana 13
#Mary Morales
def calcular_descuento(monto_total_compra, porcentaje_descuento =15):
    valor_descuento = (monto_total_compra* porcentaje_descuento)/100
    return valor_descuento

monto_total_compra=float(input("Ingrese monto: "))
porcentaje_descuento=float(input("Ingrese descuento: "))
descuento=calcular_descuento(monto_total_compra,porcentaje_descuento)
total_con_descuento=monto_total_compra-descuento
print("\n monto del descuento", descuento)
print("monto final de pagar despues del descuento", total_con_descuento)