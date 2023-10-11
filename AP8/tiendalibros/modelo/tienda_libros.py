from libro import Libro
from carro_compra import CarroCompras
from libro_agotado_error import LibroAgotadoError
from libro_existente_error import LibroExistenteError
from existencias_insuficientes_error import ExistenciasInsuficientesError
class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo = {}  # Diccionario para almacenar libros por ISBN
        self.carrito = CarroCompras()  # Instancia de la clase CarroCompras

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        # Verificar si el libro ya existe en el catálogo
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro
    
    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito(self, libro: Libro, cantidad: int):
        if libro.isbn not in self.catalogo:
            raise ValueError("El libro no está en el catálogo.")

        libro_existente = self.catalogo[libro.isbn]

        if libro_existente.existencias == 0:
            raise LibroAgotadoError(libro.isbn)

        if libro_existente.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro.isbn, cantidad, libro_existente.existencias)
        try:
            self.carrito.agregar_item(libro, cantidad)
            print("Libro agregado al carrito con éxito.")
        except Exception as e:
            print("Ocurrió un error al agregar el libro al carrito:", str(e))
    # Defina metodo retirar_item_de_carrito
    def retirar_item_de_carrito(self, isbn):
        try:
            self.carrito.quitar_item(isbn)
            print("Libro retirado del carrito con éxito.")
        except Exception as e:
            print("Ocurrió un error al retirar el libro del carrito:", str(e))
