class Pelicula:
    def __init__(self, nombre, id, duracion, año, dob_sub, precio, generos):
        self.nombre = nombre
        self.id = id
        self.duracion = duracion
        self.año = año
        self.dob_sub = dob_sub
        self.precio = precio
        self.generos = None # Deberia ser lista
        self.funciones = [] # Deberia ser treemap

    def get_funcion(self, inicio):
        for funcion in self.funciones:
            if funcion.horario.inicio == inicio:
                return funcion

        return None