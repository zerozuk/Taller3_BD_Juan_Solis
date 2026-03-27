def resta(a, b):
    return a - b


print("===Función de resta===")
a = int(input("Ingresa el primer número para la resta: "))
b = int(input("Ingresa el segundo número para la resta: "))
result = resta(a, b)
print("El resultado de la resta es:", result)

if __name__ == "__main__":
    resta(a, b)
