from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    # Defina metodo inicializador
    def __init__(self, isbn):
        super().__init__("El libro con ISBN {} está agotado".format(isbn))
    # Defina metodo especial
    def __str__(self):
        return "El libro con título {} y ISBN {} está agotado".format(self.titulo, self.isbn)