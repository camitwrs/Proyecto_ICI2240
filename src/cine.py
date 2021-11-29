class Cine:
    def __init__(self, nombre, total_ventas, trabajadores, peliculas, salas):
        self.nombre = nombre
        self.total_ventas = total_ventas
        self.trabajadores = trabajadores
        self.peliculas = peliculas
        self.salas = salas

    def get_peliculas(self) -> dict:
        opciones_pelis = {}
        peliculas = self.peliculas.values()

        if len(peliculas) > 0:
            for pelicula in peliculas:
                opciones_pelis[f"{pelicula.nombre}. {pelicula.dob_sub}"] = pelicula.id

            return opciones_pelis
        else:
            return None

    def get_funciones(self, id_pelicula):
        opciones_funciones = {}
        pelicula = self.peliculas[id_pelicula]

        for funcion in pelicula.funciones:
            inicio = funcion.get_horario_inicio()
            opciones_funciones[inicio.strftime("%d-%m %H:%M")] = (pelicula.id, inicio)
        
        return opciones_funciones


    def get_pelicula(self, id_pelicula):
        return self.peliculas[id_pelicula]

    def get_empleados(self):
        return self.trabajadores.items()

    def eliminar_empleado(self, rut):
        try:
            self.trabajadores.pop(rut)
            return True
        except:
            return False