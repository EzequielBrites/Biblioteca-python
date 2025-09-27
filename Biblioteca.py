# ============================================================================================

# Autor = Cristian Ezequiel Brites

# ============================================================================================

opcion = ""
titulos = []
ejemplares = []

# Ciclo repetitivo del menú
while opcion != "8":
    # MENÚ
    print("\n====== MENÚ BIBLIOTECA ======")
    print("1) Ingresar títulos")
    print("2) Ingresar ejemplares")
    print("3) Mostrar catálogo")
    print("4) Consultar disponibilidad")
    print("5) Listar agotados")
    print("6) Agregar título")
    print("7) Actualizar ejemplares (préstamo/devolución)")
    print("8) Salir")

    opcion = input("Opción: ").strip() # Guarda opcion elegida y en caso que tenga espacios en blanco los elimina
    # Según la opción elegida ejecuta el caso correspondiente
    match opcion:
        case "1":
            print("Opción ingresar títulos seleccionada")
            cantidad = input("¿Cuantos títulos desea ingresar (1, 2, ...)?: ")
            # Verifica que la cantidad es un numero y no es negativo o 0
            while not cantidad.isdigit() or int(cantidad) <= 0:
                print("Cantidad inválida. Intente nuevamente")
                cantidad = input("¿Cuantos títulos desea ingresar (1, 2, ...)?: ")
            # Permite ingresar la cantidad de titulos elegida por el usuario
            for i in range (1, int(cantidad) + 1 ):
                titulo = input(f"Ingresar titulo N°{i}: ").strip().title() # Borra espacios en blanco y guarda los titulos en formato primera letra mayuscula
                # Verifica que el titulo no exista o que este vacio
                while titulo in titulos or titulo == "":
                    print("Titulo repetido o en blanco. Intente nuevamente")
                    titulo = input(f"Ingrese nuevamente el titulo N°{i}: ").strip().title()
                # Agrega el titulo a la lista 
                titulos.append(titulo)
                ejemplares.append(0)
                print(f"Titulo ingresado {titulo}")
        case "2":
            # Verifica que existan titulos 
            if not titulos:
                print("Error: No hay títulos ingresados (deben existir títulos para poder ingresar la cantidad de ejemplares).")
            else:
                # Imprime por pantalla los titulos disponibles con i + 1 para que sea mas interactivo
                for i, titulo in enumerate(titulos): 
                    print(f"{i+1}. {titulo}")
            # Guarda la posicion del libro seleccionado
            posicion = int(input("Seleccione el número de titulo para ingresar ejemplares: ")) -1
            # Verifica que la posicion no sea número negativo y que no sea mayor a la cantidad de titulos disponibles
            while posicion < 0 or posicion >= len(titulos):
                print("Posición inválida, intente nuevamente")
                posicion = int(input("Seleccione el número de titulo para ingresar ejemplares: ")) -1
            # Guarda la cantidad de ejemplares
            cantidad = int(input("Ingrese la cantidad de ejemplares: "))
            # Suma la cantidad de ejemplares a la existente en la posicion del libro seleccionado
            ejemplares[posicion] += cantidad
            # Muestra los cambios echos en pantalla
            print(f"Ejemplares disponibles actualmente para {titulos[posicion]}: {ejemplares[posicion]}")
        case "3":
            print("Opción mostrar catálogo seleccionada")
            # Verifica que existan titulos 
            if not titulos:
                print("Error: No hay títulos ingresados (deben existir títulos para poder consultar el catálogo disponible).")
            else:
                # Imprime por pantalla el catálogo de libros con el stock disponible 
                print("\n====== CATÁLOGO DE LIBROS ======")
                for i, titulo in enumerate(titulos):
                    print(f"{i+1}. '{titulo}' Cantidad de ejemplares: {ejemplares[i]}")
        case "4":
            print("Opción consultar disponibilidad seleccionada")
            # Verifica que existan titulos 
            if not titulos:
                print("Error: No hay títulos ingresados (debe existir al menos un título para poder consultar la cantidad de ejemplares disponibles).")
            else:
                titulo_consulta = input("Ingresar título a consultar: ").strip().title()
                while True:
                # Verifica que el titulo realmente exista en la lista titulos y consulta cantidad ejemplares disponibles
                    if titulo_consulta in titulos:
                        posicion = titulos.index(titulo_consulta)
                        print(f"Ejemplares disponibles para {titulo_consulta}: {ejemplares[posicion]}")
                        break
                    else:
                        print(f"El titulo: {titulo_consulta} no se encuentra en el catálogo.")
                # En caso que no exista permite ingresar nuevamente el titulo
                    print("Desea ingresarlo nuevamente? (s: vuelve a ingresar / n: vuelve al menú principal)")
                    eleccion = input().lower()
                    if eleccion == "s":
                        titulo_consulta = input("Ingresar título a consultar: ").strip().title()
                    else:
                        break
        case "5":
            print("Opción listar agotados seleccionada")
            # Verifica que existan titulos 
            if not titulos:
                print("Error: No hay títulos ingresados (deben existir títulos disponibles).")
            else:
                agotados = False 
                # Verifica si existe al menos un libro agotado
                for i  in ejemplares:
                    if i == 0:
                        agotados = True # Bandera se convierte a true en caso que exista al menos un libro sin stock
                        break
                if agotados:
                    print("\n====== LIBROS AGOTADOS ======")
                    # Imprime todos los libros con stock agotado
                    for titulo in titulos:
                        posicion = titulos.index(titulo)
                        if ejemplares[posicion] == 0:
                            print(titulo)
                else:
                    print("No hay libros agotados. Todos los títulos tienen ejemplares disponibles.")
        case "6":
            print("Opción agregar título seleccionada")
            nuevo_titulo = input("Ingrese el nuevo título: ").strip().title()
            # Verifica que el titulo no exista o que este vacio
            while nuevo_titulo in titulos or nuevo_titulo == "":
                print("Titulo repetido o en blanco. Intente nuevamente")
                nuevo_titulo = input(f"Ingrese nuevamente el titulo: ").strip().title()
            # Agrega nuevo titulo a la lista
            titulos.append(nuevo_titulo)
            # Almacena cantidad de ejemplares
            cantidad = int(input(f"Ingrese la cantidad de ejemplares para '{nuevo_titulo}': "))
            # Almacena la posicion del nuevo titulo
            posicion = titulos.index(nuevo_titulo)
            # Inserta en la posición del nuevo titulo la cantidad de ejemplares
            ejemplares.insert(posicion,cantidad)
            print(f"Titulo: {nuevo_titulo} agregado al catálogo con {cantidad} ejemplares disponibles") # Muestra en pantalla los cambios aplicados
        case "7":
            print("Opción actualizar ejemplares seleccionada")
            # Verifica que existan titulos 
            if not titulos:
                print("Error: No hay títulos ingresados (deben existir títulos disponibles).")
            else:
                # Imprime por pantalla los titulos disponibles con i + 1 para que sea mas interactivo
                for i, titulo in enumerate(titulos): 
                    print(f"{i+1}. {titulo}")
                posicion = int(input("Seleccione el número de titulo para actualizar ejemplares: ")) -1
                # Verifica que la posicion no sea número negativo y que no sea mayor a la cantidad de titulos disponibles
                while posicion < 0 or posicion >= len(titulos):
                    print("Posición inválida, intente nuevamente")
                    posicion = int(input("Seleccione el número de titulo para ingresar ejemplares: ")) -1

                accion = input(f"Ingrese 'p' para prestamo o 'd' para devolución: ").lower().strip()
                if accion == "p":
                    if ejemplares[posicion] > 0:
                        ejemplares[posicion] -= 1
                        print(f"Prestamo realizado. Ejemplares disponibles para {titulos[posicion]}: {ejemplares[posicion]}")
                    else:
                        print(f"No hay ejemplares disponibles para {titulos[posicion]}")
                        
                elif accion == "d":
                    ejemplares[posicion] += 1
                    print(f"Devolución realizada. Ejemplares disponibles para {titulos[posicion]}: {ejemplares[posicion]}")
                else:
                    print("La acción es inválida. Use 'p' (Préstamo) o 'd' (Devolución)")
        case "8":
            print("Saliendo...")
        case _:
            print("Opción invalida. Elegi 1-8")
