class Funcion:
    def __init__(self, horario, sala, pelicula, entradas_vendidas):
        self.horario = horario
        self.sala = sala
        self.pelicula = pelicula
        self.entradas_vendidas = entradas_vendidas

    def get_horario_inicio(self):
        return self.horario.inicio

    def get_nombre_pelicula(self):
        return self.pelicula.nombre

    def get_numero_sala(self):
        return self.sala.numero

    def get_tamaño_sala(self):
        return self.sala.asientos_totales
        
    def get_precio(self):
        return self.pelicula.precio