productos = {
    "M001": ["Alimento Premium", "Comida", "DogPlus", "10", True, False],
    "M002": ["Arena Aglomerante", "Higiene", "CatClean", "8", False, False],
    "M003": ["Snack Dental", "Snack", "BiteJoy", "1", True, True],
    "M004": ["Shampoo Suave", "Higiene", "PetCare", "0.5", False, True],
    "M005": ["Correa Nylon", "Accesorio", "Walkpro", "0.3", True, False],
    "M006": ["Cama Mediana", "Accesorio", "CozyPet", "2", False, False]
}

stock = {
    "M001": [32990, 12],
    "M002": [9990, 0],
    "M003": [5490, 25],
    "M004": [7990, 5],
    "M005": [11990, 7],
    "M006": [24990, 3]
}


def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")


def unidades_categoria(categoria):
    total = 0

    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total = total + stock[codigo][1]

    print("El total de unidades disponibles es:", total)


def busqueda_precio(p_min, p_max):
    resultados = []

    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]

        if precio >= p_min and precio <= p_max and unidades != 0:
            nombre = productos[codigo][0]
            resultados.append(nombre + "--" + codigo)

    resultados.sort()

    if len(resultados) > 0:
        print("Las productos encontradas son:", resultados)
    else:
        print("No hay productos en ese rango de precios.")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper()

    if codigo in stock:
        stock[codigo][0] = nuevo_precio
        return True
    else:
        return False


def validar_codigo(codigo):
    if codigo.strip() == "":
        return False

    if codigo.upper() in productos or codigo.upper() in stock:
        return False

    return True


def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False


def validar_categoria(categoria):
    if categoria.strip() != "":
        return True
    else:
        return False


def validar_marca(marca):
    if marca.strip() != "":
        return True
    else:
        return False


def validar_peso_kg(peso_kg):
    try:
        valor = float(peso_kg)
        return valor > 0
    except ValueError:       
        return False



def validar_es_importado(es_importado):
    if es_importado.strip() != "":
        return True
    else:
        return False


def validar_es_para_cachorro(es_para_cachorro):
    if es_para_cachorro.lower() == "s" or es_para_cachorro.lower() == "n":
        return True
    else:
        return False


def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False


def validar_unidades(unidades):
    if unidades >= 0:
        return True
    else:
        return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    marca,
    peso_kg,
    es_importado,
    es_para_cachorro,
    precio,
    unidades
):
    codigo = codigo.upper()

    if codigo in productos or codigo in stock:
        return False

    productos[codigo] = [
        nombre,
        categoria,
        marca,
        peso_kg,
        es_importado,
        es_para_cachorro
    ]

    stock[codigo] = [
        precio,
        unidades
    ]

    return True


def eliminar_producto(codigo):
    codigo = codigo.upper()

    if codigo in productos and codigo in stock:
        del productos[codigo]
        del stock[codigo]
        return True
    else:
        return False


while True:

    mostrar_menu()

    try:
        opcion = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe seleccionar una opción válida")
        continue

    if opcion == 1:

        categoria = input("Ingrese categoría a consultar: ")

        unidades_categoria(categoria)

    elif opcion == 2:

        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break
                else:
                    print("Debe ingresar un rango de precios válido")

            except ValueError:
                print("Debe ingresar valores enteros")

        busqueda_precio(p_min, p_max)

    elif opcion == 3:

        while True:

            codigo = input("Ingrese código de la producto: ")

            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))

                if nuevo_precio <= 0:
                    print("El precio debe ser mayor que cero")
                else:
                    resultado = actualizar_precio(codigo, nuevo_precio)

                    if resultado == True:
                        print("Precio actualizado")
                    else:
                        print("El código no existe")

            except ValueError:
                print("Debe ingresar un precio entero")

            continuar = input(
                "¿Desea actualizar otro precio (s/n)?: "
            ).lower()

            if continuar == "n":
                break

    elif opcion == 4:

        codigo = input("Ingrese código de la producto: ")
        nombre = input("Ingrese nombre: ")
        categoria = input("Ingrese categoría: ")
        marca = input("Ingrese marca: ")
        peso_kg = input("Ingrese peso_kg: ")
        es_importado = input("Ingrese es_importado: ")
        es_para_cachorro = input("¿Es para cachorro? (s/n): ")

        try:
            precio = int(input("Ingrese precio: "))
            unidades = int(input("Ingrese unidades: "))

        except ValueError:
            print("Precio y unidades deben ser valores enteros")
            continue

        if validar_codigo(codigo) == False:
            print("El código no es válido o ya existe")

        elif validar_nombre(nombre) == False:
            print("El nombre no puede estar vacío")

        elif validar_categoria(categoria) == False:
            print("La categoría no puede estar vacía")

        elif validar_marca(marca) == False:
            print("La marca no puede estar vacía")

        elif validar_peso_kg(peso_kg) == False:
            print("El peso_kg debe ser un número mayor que cero")

        elif validar_es_importado(es_importado) == False:
            print("El es_importado no puede estar vacío")

        elif validar_es_para_cachorro(es_para_cachorro) == False:
            print("Debe ingresar s o n")

        elif validar_precio(precio) == False:
            print("El precio debe ser mayor que cero")

        elif validar_unidades(unidades) == False:
            print("Las unidades deben ser mayores o iguales a cero")

        else:

            if es_para_cachorro.lower() == "s":
                valor_para_cachorro = True
            else:
                valor_para_cachorro = False

            resultado = agregar_producto(
                codigo,
                nombre,
                categoria,
                marca,
                peso_kg,
                es_importado,
                valor_para_cachorro,
                precio,
                unidades
            )

            if resultado == True:
                print("producto agregada")
            else:
                print("El código ya existe")

    elif opcion == 5:

        codigo = input("Ingrese código de la producto a eliminar: ")

        resultado = eliminar_producto(codigo)

        if resultado == True:
            print("producto eliminada")
        else:
            print("El código no existe")

    elif opcion == 6:

        print("Programa finalizado.")
        break

    else:

        print("Debe seleccionar una opción válida")