def main():
    print("===Lista de compras inteligente===")

    option = ""
    shoppinglist = []

    while option != "4":
        print("1. Agregar")
        print("2. Mostrar lista de compras")
        print("3. Buscar producto")
        print("4. Salir")
        option = input("Selecciona una opción: ")

        if option == "1":
            producto = input("producto: ")
            shoppinglist.append(producto)
        elif option == "2":
            print("Tu lista de compras incluye lo siguiente: ")
            print(shoppinglist)
        elif option == "3":
            producto = input("Introduce el nombre del producto a buscar: ")
            if producto in shoppinglist:
                print(f"El producto {producto} está en la lista.")
            else:
                print(f"El producto {producto} no está en la lista.")


main()
