from src.treemap import TreeMap

class Pelicula:
    def __init__(self, nombre, id, duracion, año, dob_sub, precio, generos):
        self.nombre = nombre
        self.id = id
        self.duracion = duracion
        self.año = año
        self.dob_sub = dob_sub
        self.precio = precio
        self.generos = generos
        self.funciones = TreeMap()

    def get_funcion(self, inicio):
        pair_aux = self.funciones.first()

        while pair_aux:
            if pair_aux.value.get_horario_inicio() == inicio:
                return pair_aux.value

            pair_aux = self.funciones.next()
        
        return None