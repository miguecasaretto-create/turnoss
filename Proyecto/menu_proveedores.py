# Proveedores/menu_proveedores.py

from proveedores import (
    agregar_proveedor,
    listar_proveedores,
    buscar_proveedor,
    actualizar_proveedor,
    eliminar_proveedor
)


def menu():
    while True:
        print("\n--- MENU PROVEEDORES ---")
        print("1. Agregar proveedor")
        print("2. Listar proveedores")
        print("3. Buscar proveedor")
        print("4. Actualizar proveedor")
        print("5. Eliminar proveedor")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del proveedor: ")
            telefono = input("Telefono: ")
            producto = input("Producto que provee: ")

            agregar_proveedor(nombre, telefono, producto)

            print("Proveedor agregado correctamente")

        elif opcion == "2":
            lista = listar_proveedores()

            if len(lista) == 0:
                print("No hay proveedores registrados")

            else:
                for p in lista:
                    print(
                        f"Nombre: {p['nombre']} | "
                        f"Telefono: {p['telefono']} | "
                        f"Producto: {p['producto']}"
                    )

        elif opcion == "3":
            nombre = input("Ingrese nombre a buscar: ")

            proveedor = buscar_proveedor(nombre)

            if proveedor:
                print(proveedor)

            else:
                print("Proveedor no encontrado")

        elif opcion == "4":
            nombre = input("Proveedor a actualizar: ")

            telefono = input("Nuevo telefono: ")
            producto = input("Nuevo producto: ")

            if actualizar_proveedor(nombre, telefono, producto):
                print("Proveedor actualizado")

            else:
                print("Proveedor no encontrado")

        elif opcion == "5":
            nombre = input("Proveedor a eliminar: ")

            if eliminar_proveedor(nombre):
                print("Proveedor eliminado")

            else:
                print("Proveedor no encontrado")

        elif opcion == "6":
            print("Saliendo...")
            break

        else:
            print("Opcion invalida")


menu()