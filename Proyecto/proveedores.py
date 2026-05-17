# Proveedores/proveedores.py

proveedores = []


def agregar_proveedor(nombre, telefono, producto):
    proveedor = {
        "nombre": nombre,
        "telefono": telefono,
        "producto": producto
    }

    proveedores.append(proveedor)


def listar_proveedores():
    return proveedores


def buscar_proveedor(nombre):
    for proveedor in proveedores:
        if proveedor["nombre"].lower() == nombre.lower():
            return proveedor

    return None


def actualizar_proveedor(nombre, nuevo_telefono, nuevo_producto):
    proveedor = buscar_proveedor(nombre)

    if proveedor:
        proveedor["telefono"] = nuevo_telefono
        proveedor["producto"] = nuevo_producto
        return True

    return False


def eliminar_proveedor(nombre):
    proveedor = buscar_proveedor(nombre)

    if proveedor:
        proveedores.remove(proveedor)
        return True

    return False