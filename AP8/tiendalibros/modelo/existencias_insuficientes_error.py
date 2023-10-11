from tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, isbn, cantidad_a_comprar, existencias):
        super().__init__("El libro con ISBN {} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {}, existencias: {}".format(isbn, cantidad_a_comprar, existencias))
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias = existencias

    def __str__(self):
        return "El libro con título {} y ISBN {} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {}, existencias: {}".format(self.titulo, self.isbn, self.cantidad_a_comprar, self.existencias)
