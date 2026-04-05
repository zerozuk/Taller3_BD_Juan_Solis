def main():
    print("===Carrito de compras===")

    prices = []
    option = ""

    while option != "3":
        print("1. agregar precio")
        print("2. total a pagar")
        print("3. salir")

        option = input("Selecciona una opción: ")

        if option == "1":
            price = float(input("Introduce el precio del producto: "))
            prices.append(price)
        elif option == "2":

            def calculate_total(prices):
                total = sum(prices)
                return total

            total = calculate_total(prices)
            print(f"---el total a pagar es: {total}")

            calculate_total(prices)


main()
