class Libro:
    def __init__(self, titulo: int, autor, categoria):
        self.categoria = categoria
        self.autor = autor
        self.titulo = titulo

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_categoria(self):
        return self.categoria

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_categoria(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return "Titulo: {} | Autor: {} | Categoria: {}".format(self.titulo, self.autor, self.categoria)


# clase libreria, que contiene una lista de libros
class Libreria:
    def __init__(self):
        self.libros = []

    def get_libros(self):
        return self.libros

    def set_libros(self, libros):
        self.libros = libros

    def agregar_libro(self):
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")

        if self.buscar_libro_titulo(titulo) is None:
            self.libros.append(Libro(titulo, autor, categoria))
            return True
        return False

    def eliminar_libro(self, titulo):
        try:
            self.libros.remove(self.buscar_libro_titulo(titulo))
            return True
        except ValueError:
            return False

    def buscar_libro_titulo(self, titulo):
        for libro_busc_titulo in self.libros:
            if libro_busc_titulo.titulo == titulo:
                return libro_busc_titulo

    def buscar_libro_autor(self, autor):
        libros_autor = []
        for libro_busc_autor in self.libros:
            if libro_busc_autor.autor == autor:
                libros_autor.append(libro_busc_autor)
        return libros_autor

    def buscar_libro_categoria(self, categoria):
        libros_categoria = []
        for libro_busc_categoria in self.libros:
            if libro_busc_categoria.categoria == categoria:
                libros_categoria.append(libro_busc_categoria)
        return libros_categoria

    def mostrar_libro(self, libro):
        if type(libro) == Libro:
            print(libro)
        elif type(libro) == list:
            for libro_item in libro:
                print(libro_item)

    # cargar los libros desde un archivo en formato csv separados por ;
    # gestionando las excepciones
    def cargar_libros(self):
        archivo = None
        hay_repetidos = False
        titulos_aux = []
        libros_aux = []  # Con esta lista si hay algún error no guardamos ningún libro en la librería
        try:
            archivo = open("libros.txt")
            lineas = archivo.readlines()

            for linea in lineas:
                info = linea.replace("\n", "").split(";")
                if info[0] in titulos_aux:
                    hay_repetidos = True  # Este filtro controla que no se introduzcan libros con titulos repetidos
                    break
                else:
                    titulos_aux.append(info[0])
                    libros_aux.append(Libro(info[0], info[1], info[2]))
        except (FileNotFoundError, LookupError, UnicodeDecodeError):
            return False
        finally:
            archivo.close()

        if not hay_repetidos:
            self.set_libros(libros_aux)
            return True
        else:
            return False

    # grabar los libros desde un archivo en formato csv separados por ;
    # gestionando las excepciones
    def grabar_libros(self):
        archivo = None
        grabado = True

        try:
            archivo = open("libros.txt", "w")
            for libro_a_grabar in self.libros:
                archivo.write(libro_a_grabar.titulo + ";"
                              + libro_a_grabar.autor + ";"
                              + libro_a_grabar.categoria + "\n")
        except (FileNotFoundError, LookupError, UnicodeDecodeError):
            grabado = False
        finally:
            archivo.close()

        return grabado

    # introduciendo el titulo original lo cambia por el titulo modificado
    def modificar_titulo(self, titulo_original, titulo_nuevo):
        libro_mod_titulo = self.buscar_libro_titulo(titulo_original)
        libro_titulo = self.buscar_libro_titulo(titulo_nuevo)

        if libro_mod_titulo is not None and libro_titulo is None:
            libro_mod_titulo.set_titulo(titulo_nuevo)
            return True
        return False

    def modificar_categoria(self, categoria_original, categoria_nuevo):
        libro_mod_categoria = self.buscar_libro_categoria(categoria_original)

        if libro_mod_categoria is not None and libro_mod_categoria != []:
            if type(libro_mod_categoria) == Libro:
                libro_mod_categoria.set_categoria(categoria_nuevo)
            elif type(libro_mod_categoria) == list:
                for libro_item in libro_mod_categoria:
                    libro_item.set_categoria(categoria_nuevo)
            return True
        return False

    def modificar_autor(self, autor_original, autor_nuevo):
        libro_mod_autor = self.buscar_libro_autor(autor_original)

        if libro_mod_autor is not None and libro_mod_autor != []:
            if type(libro_mod_autor) == Libro:
                libro_mod_autor.set_autor(autor_nuevo)
            elif type(libro_mod_autor) == list:
                for libro_item in libro_mod_autor:
                    libro_item.set_autor(autor_nuevo)
            return True
        return False

    # Devuelve la cantidad de libros totales
    def cantidad_libros(self):
        return len(self.libros)


# si este es el main se ejecuta el siguiente codigo
if __name__ == "__main__":
    l1 = Libreria()
    opcion = 0
    while opcion != 8:
        print("1. Cargar Libros")
        print("2. Grabar Libros")
        print("3. Introducir Libros")
        print("4. Modificar Libros")
        print("5. Eliminar Libro")
        print("6. Cantidad de libros registrados")
        print("7. Mostrar libros")
        print("8. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error. Introduce un valor numérico.")

        if opcion == 1:
            if l1.cargar_libros():
                print("Libros cargados correctamente.")
            else:
                print("Error. No se han podido cargar los libros.")

        elif opcion == 2:
            if l1.grabar_libros():
                print("Libros grabados correctamente.")
            else:
                print("Error.No se han podido cargar los libros.")

        elif opcion == 3:
            if l1.agregar_libro():
                print("Libro introducido correctamente.")
            else:
                print("Error. No se ha podido introducir el libro.")

        elif opcion == 4:  # modificar libro

            opcion_modificar = 0
            while opcion_modificar != 4:
                print("1. Modificar Titulo")
                print("2. Modificar Autor")
                print("3. Modificar Categoria")
                print("4. Salir")

                try:
                    opcion_modificar = int(input("Ingrese una opción: "))
                except ValueError:
                    print("Error. Introduce un valor numérico.")

                if opcion_modificar == 1:
                    if l1.modificar_titulo(input("Titulo original: "), input("Titulo nuevo: ")):
                        print("Modificación realizada correctamente.")
                    else:
                        print("Error. No se ha podido realizar la modificación.")
                elif opcion_modificar == 2:
                    if l1.modificar_autor(input("Autor original: "), input("Autor nuevo: ")):
                        print("Modificación realizada correctamente.")
                    else:
                        print("Error. No se ha podido realizar la modificación.")
                elif opcion_modificar == 3:
                    if l1.modificar_categoria(input("Categoria original: "), input("Categoria nueva: ")):
                        print("Modificación realizada correctamente.")
                    else:
                        print("Error. No se ha podido realizar la modificación.")

        elif opcion == 5:  # eliminar libro
            titulo = input("Ingrese el titulo del libro a eliminar: ")
            if l1.eliminar_libro(titulo):
                print("El libro se ha eliminado correctamente.")
            else:
                print("Error. El libro no se pudo eliminar")

        elif opcion == 6:  # cantidad de libros
            print("La cantidad de libros es: " + str(l1.cantidad_libros()))

        elif opcion == 7:  # mostrar libros
            opcion_mostrar = 0
            while opcion_mostrar != 7:
                print("1. Todos los titulos")
                print("2. Todas las categorías")
                print("3. Todos los autores")
                print("4. Un título")
                print("5. Una categoría")
                print("6. Un autor")
                print("7. Salir")

                try:
                    opcion_mostrar = int(input("Ingrese una opcion: "))
                except ValueError:
                    print("Error. Introduce un valor numérico.")
                if opcion_mostrar == 1:
                    libros = l1.get_libros()
                    if libros is not None:
                        for libro in libros:
                            print(libro.titulo)
                    else:
                        print("Error. No se han encontrado resultados.")

                elif opcion_mostrar == 2:
                    categorias = []
                    for x in l1.get_libros():
                        if x.categoria not in categorias:
                            categorias.append(x.categoria)
                            print(x.categoria)

                    if not categorias:
                        print("Error. No se han encontrado resultados.")

                elif opcion_mostrar == 3:
                    autores = []
                    for x in l1.get_libros():
                        if x.autor not in autores:
                            autores.append(x.autor)
                            print(x.autor)

                    if not autores:
                        print("Error. No se han encontrado resultados.")

                elif opcion_mostrar == 4:
                    titulo = input("Buscar titulo: ")
                    libro = l1.buscar_libro_titulo(titulo)

                    if libro is not None:
                        print(libro)
                    else:
                        print("No se han encontrado resultados.")

                elif opcion_mostrar == 5:
                    libros = l1.buscar_libro_categoria(input("Buscar categoria: "))
                    if libros is not None and libros != []:
                        for libro in libros:
                            print(libro)
                    else:
                        print("No se han encontrado ningún libro compatible.")

                elif opcion_mostrar == 6:
                    libros = l1.buscar_libro_autor(input("Buscar autor: "))
                    if libros is not None and libros != []:
                        for libro in libros:
                            print(libro)
                    else:
                        print("No se han encontrado ningún libro compatible.")

        elif opcion == 8:
            print("Saliendo del programa")
        else:
            print("Opcion incorrecta")
