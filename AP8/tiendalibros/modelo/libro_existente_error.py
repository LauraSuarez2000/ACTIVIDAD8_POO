from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    # Defina metodo inicializador
    def __init__(self, isbn):
        super().__init__("El libro con ISBN {} ya existe en el catálogo".format(isbn))
    # Defina metodo especial
    def __str__(self):
        return f"El libro con título {self.titulo} y ISBN: {self.isbn} ya existe en el catálogo"