#Ejercicio uno
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print("Su Índice de Masa Corporal (IMC) es: {:.2f}".format(imc))


if imc < 18.5:
    print("Usted está bajo de peso.")
elif imc >= 18.5 and imc < 24.9:
    print("Usted tiene un peso saludable.")
elif imc >= 25 and imc < 29.9:
    print("Usted tiene sobrepeso.")
elif imc >= 30 and imc < 34.9:
    print("Usted tiene obesidad clase 1 (Moderada).")
elif imc >= 35 and imc < 39.9:
    print("Usted tiene obesidad clase 2 (Severa).")
else:
    print("Usted tiene obesidad clase 3 (Muy severa o mórbida).")

#Ejercicio dos

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad de productos: "))
precio = float(input("Ingrese el precio unitario del producto: "))

subtotal = cantidad * precio

descuento = 0
if cantidad > 10:
    descuento = subtotal * 0.07


total = subtotal - descuento

print("----- COLILLA DE VENTA -----")
print("Producto: {}".format(producto))
print("Cantidad: {}".format(cantidad))
print("Precio unitario: ${:.2f}".format(precio))
print("Subtotal: ${:.2f}".format(subtotal))
print("Descuento: ${:.2f}".format(descuento))
print("Total a pagar: ${:.2f}".format(total))
print("-----------------------------")


