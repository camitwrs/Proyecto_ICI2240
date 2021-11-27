import os
import csv
from datetime import datetime
from src.horario import Horario

class EmpleadoModel:
    """
        Clase que contiene la parte lógica del menú de un empleado.
        Si desea, por ejemplo, implementar la opción de menú de mostrar_horario, se debería
        crear una función con nombre similar en esta clase que retorne los datos que la vista
        necesita desplegar.
    """
    def __init__(self, empleado, cine):
        self.empleado = empleado
        self.cine = cine

        self.venta = None

    def get_peliculas(self):
        return self.cine.get_peliculas()

    def get_funciones(self, id_pelicula):
        return self.cine.get_funciones(id_pelicula)
    
    def guardar_venta(self, id_pelicula, inicio):
        pelicula = self.cine.get_pelicula(id_pelicula)
        funcion = pelicula.get_funcion(inicio)

        if self.venta is None:
            self.venta = Venta(funcion)
        else:
            self.venta.funcion = funcion

        print(f"Pelicula almacenada: {self.venta.funcion.pelicula.nombre} Inicio: {self.venta.funcion.horario.inicio} Sala: {self.venta.funcion.sala.numero}")

    def mostrar_horario_mod(self):
        path = os.getcwd()
        absolute_path = f"{path}\data\quilpue\empleados\\20272418\horarios.csv"
        horario = []
        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            
            for row in csv_reader:
                inicio = datetime.fromtimestamp(int(row[0]))
                final = datetime.fromtimestamp(int(row[1]))
                horario = Horario(inicio.strftime("%H:%M"), final.strftime("%H:%M"))
                print("Fecha:", inicio.strftime("%d/%m"), "Hora ingreso:", horario.inicio, "Hora salida:", horario.final)
                
    def marcar_asistencia_mod(self):
        nombre_usuario = "javier_peralta"
        hora_entrada = datetime.now()
        data = [nombre_usuario, hora_entrada.strftime("%H:%M")]
        path = os.getcwd()
        absolute_path = f"{path}\data\quilpue\empleados\\20272418\\asistencia.csv"
        with open(absolute_path, 'w') as csv_file:
            csv_file.seek(len(csv_file.read()))
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)


class Venta:
    def __init__(self, funcion, descuento = None):
        self.funcion = funcion
        self.descuento = descuento