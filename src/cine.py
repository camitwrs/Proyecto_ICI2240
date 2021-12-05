from src.trabajador import Empleado, AdminLocal


class Cine:
    def __init__(self, nombre, total_ventas, trabajadores, peliculas, salas):
        self.nombre = nombre
        self.total_ventas = total_ventas
        self.trabajadores = trabajadores
        self.peliculas = peliculas
        self.salas = salas

    def get_opciones_peliculas(self) -> dict:
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

    def existe_empleado(self, rut: str):
        if self.trabajadores.get(rut) is None:
            return False

        return True

    def eliminar_empleado(self, rut):
        try:
            self.trabajadores.pop(rut)
            return True
        except:
            return False

    def añadir_empleado(self, rut: str, contraseña: str, nombre: str, sueldo: str):
        empleado = Empleado(rut, contraseña, "empleado", self.nombre)
        empleado.nombre = nombre
        empleado.sueldo = int(sueldo)

        self.trabajadores[empleado.rut] = empleado

        return empleado

    def añadir_admin_local(self, rut: str, contraseña: str, nombre: str, sueldo: str):
        admin_local = AdminLocal(rut, contraseña, "administrador_local", self.nombre)
        admin_local.nombre = nombre
        admin_local.sueldo = int(sueldo)

        self.trabajadores[admin_local.rut] = admin_local

        return admin_local

    def get_salas(self):
        opciones_salas = {}
        for sala in self.salas.values():
            if sala.estado:
                estado = "Habilitada"
            else:
                estado = "Deshabilitada"

            opciones_salas[sala.numero] = (sala.numero, sala.asientos_totales, estado)

        return opciones_salas

    def habilitar_sala(self, id):
        sala = self.salas.get(int(id))

        if sala is not None:
            sala.estado = True

    def deshabilitar_sala(self, id):
        sala = self.salas.get(int(id))

        if sala is not None:
            sala.estado = False

    def get_precios_peliculas(self):
        return self.peliculas.values()

    def modificar_precio(self, id_pelicula, precio):
        pelicula = self.peliculas.get(id_pelicula)

        pelicula.precio = precio

    def get_local_admins(self):
        local_admins = []
        for empleado in self.trabajadores.values():
            if empleado.cargo == "administrador_local":
                local_admins.append( (empleado.rut, empleado.nombre, empleado.cine) )

        return local_admins
