def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: no es posible dividir entre0 cero"


print("===Función de división===")
a = int(input("Ingresa el primer número para la división: "))
b = int(input("Ingresa el segundo número: "))

result = division(a, b)
print("El resultado de la división es:", result)
