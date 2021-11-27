class Funcion:
    def __init__(self, horario, sala, pelicula, entradas_vendidas):
        self.horario = horario
        self.sala = sala
        self.pelicula = pelicula
        self.entradas_vendidas = entradas_vendidas

    def get_horario_inicio(self):
        return self.horario.inicio