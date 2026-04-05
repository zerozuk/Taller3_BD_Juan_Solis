def main():
    print("===Calculadora de Notas===")

    option = ""
    grades = []

    while option != "4":
        print("1. Agregar notas")
        print("2. Mostrar lista de notas")
        print("3. Sacar promedio")
        print("4. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            grade = float(input("Ingresa la nota: "))
            grades.append(grade)
        elif option == "2":
            print("--- Estas son tus notas: ")
            print(grades)
        elif option == "3":

            def calculate_average(grades):
                if grades:
                    average = sum(grades) / len(grades)
                    print(f"--- El promedio de tus notas es: {average}===")
                else:
                    print("No hay notas para calcular el promedio.")

            calculate_average(grades)


main()
