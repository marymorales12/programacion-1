#Tarea en clase
#Fahrenheit = (9/5)(grad_cent*32)
#kelvin=273.15 * grad cent

def conversion (tem_grad_cent):
    Fahrenheit= (9/5)*tem_grad_cent + 32
    kelvin=273.15 * grad_cent
    return Fahrenheit, kelvin

grad_cent=int(input("Ingrese temperatura en grados centigrados"))

Fahren, kelv =conversion(grad_cent)
print(Fahren,kelv)
