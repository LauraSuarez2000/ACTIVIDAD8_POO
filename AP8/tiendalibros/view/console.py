import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError
from tiendalibros.modelo.libro_existente_error import LibroExistenteError


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    # Defina el metodo retirar_libro_de_carrito_de_compras
    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("Libro retirado del carrito con éxito.")
        except Exception as e:
            print("Ocurrió un error al retirar el libro del carrito:", str(e))
    # Defina el metodo agregar_libro_a_carrito_de_compras
    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a agregar: ")
        cantidad = int(input("Ingrese la cantidad de unidades: "))
        try:
            libro = self.tienda_libros.catalogo.get(isbn)
            if libro:
                self.tienda_libros.agregar_libro_a_carrito(libro, cantidad)
                print("Libro agregado al carrito con éxito.")
            else:
                print("No se encontró un libro con ese ISBN en el catálogo.")
        except LibroAgotadoError as e:
            print("El libro está agotado:", str(e))
        except ExistenciasInsuficientesError as e:
            print("Existencias insuficientes para el libro:", str(e))
        except Exception as e:
            print("Ocurrió un error al agregar el libro al carrito:", str(e))

    # Defina el metodo adicionar_un_libro_a_catalogo
    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            precio = float(input("Ingrese el precio del libro: "))
            existencias = int(input("Ingrese las existencias del libro: "))
            
            libro = self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro agregado al catálogo con éxito:", libro)
        except LibroExistenteError as e:
            print("Error al adicionar el libro al catálogo:", str(e))
        except Exception as e:
            print("Ocurrió un error al adicionar el libro al catálogo:", str(e))