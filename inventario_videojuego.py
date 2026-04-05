def main():
    print("===inventario de videojuegos===")

    inventory = []
    option = ""

    while option != "5":
        print("1. Agregar objeto")
        print("2. Mostrar inventario")
        print("3. Buscar objeto")
        print("4. Eliminar objeto")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            item = input("Introduce el objeto para agregar: ")
            inventory.append(item)
        elif option == "2":
            print("Tu inventario incluye lo siguiente: ")
            print(inventory)
        elif option == "3":

            def show_inventory(inventory):
                item = input("Introduce el nombre del objeto a buscar: ")
                if item in inventory:
                    print(f"El objeto {item} está en el inventario.")
                else:
                    print(f"El objeto {item} no se encuentra en el inventario.")

            show_inventory(inventory)

        elif option == "4":
            item = input("Introduce el nombre del objeto a eliminar: ")
            if item in inventory:
                inventory.remove(item)
                print(f"---El objeto {item} ha sido eliminado del inventario.")
            else:
                print(f"---El objeto {item} no se encuentra en el inventario.")


main()
