import csv
import os
from datetime import datetime

from src.trabajador import Empleado, AdminGlobal, AdminLocal
from src.modelos import *
from src.cupon import Cupon

DOB_SUB = {
    0: "Subtitulada",
    1: "Doblada"
}

class LoginModel:
    """
        Clase que contiene la parte lógica del login y la carga de datos al programa.
    """
    def __init__(self):
        self.usuarios = self._cargar_credenciales()

    def _determinar_cargo(self, cargo: str):
        cargos = {
            "empleado": Empleado,
            "administrador_local": AdminLocal,
            "administrador_global": AdminGlobal
        }

        return cargos.get(cargo)

    def _cargar_credenciales(self) -> None:
        """
            Carga los datos iniciales de todos los trabajadores del LoginModel.
            Se almacenan los objetos de los trabajadores en un dict, en la variable self.usuarios.
        """
        usuarios = {}

        path = os.getcwd()
        absolute_path = f"{path}\data\credenciales.csv"
    
        with open(absolute_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Se salta la línea que contiene el nombre de los campos

            for row in csv_reader:
                rut = row[0]
                contraseña = row[1]
                cargo = row[2]
                cine = row[3]

                _class = self._determinar_cargo(cargo)

                if _class is not None:
                    _class_objeto = _class(rut, contraseña, cargo, cine)
                    usuarios[rut] = _class_objeto
            
        return usuarios

    def _cargar_ventas(self, cine_folder: str):
        total_ventas = 0

        with open(f"{cine_folder}\\ventas.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Se salta la línea que contiene el nombre de los campos

            for row in csv_reader:
                #empleado = row[0]
                #fecha = row[1]
                precio = row[2]
                #cine = row[3]
                
                total_ventas += int(precio)

        print(total_ventas)
        return total_ventas

    def _cargar_horarios(self, cine_folder: str, rut: str):
        horarios = []

        with open(f"{cine_folder}\empleados\{rut}\horarios.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)

            for row in csv_reader:
                inicio = row[0]
                final = row[1]

                horario = Horario(
                    datetime.fromtimestamp(int(inicio)), datetime.fromtimestamp(int(final)))
                horarios.append(horario)

        return horarios

    def _cargar_asistencia(self, cine_folder: str, rut: str):
        asistencia_list = []

        with open(f"{cine_folder}\empleados\{rut}\horarios.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)

            for row in csv_reader:
                horario_inicio = int(row[0])
                asistencia_bool = bool(row[1])

                asistencia = Asistencia(
                    datetime.fromtimestamp(horario_inicio), asistencia_bool
                )
                asistencia_list.append(asistencia)

        return asistencia_list

    def _cargar_trabajadores(self, cine_folder: str):
        trabajadores_cine = {}
        
        with open(f"{cine_folder}\\empleados.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Se salta la línea que contiene el nombre de los campos

            for row in csv_reader:
                nombre = row[0]
                rut = row[1]
                sueldo = row[2]
                ventas = row[3]

                empleado = self.usuarios[rut]
                empleado.nombre = nombre
                empleado.sueldo = sueldo
                empleado.ventas = ventas
                empleado.horarios = self._cargar_horarios(cine_folder, rut)
                empleado.asistencia = self._cargar_asistencia(cine_folder, rut)

                trabajadores_cine[empleado.rut] = empleado

                print(empleado.nombre, empleado.sueldo, empleado.ventas)

                for horario in empleado.horarios:
                    print(horario.inicio, horario.final)

                for asistencia in empleado.asistencia:
                    print(asistencia.inicio, asistencia.asistencia)

        return trabajadores_cine

    def _cargar_salas(self, cine_folder: str) -> dict:
        salas = {}
        with open(f"{cine_folder}\\salas.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                numero = int(row[0])
                asientos_totales = int(row[1])
                estado = bool(row[2])
                funciones = []

                sala = Sala(numero, asientos_totales, estado, funciones=funciones)
                salas[numero] = sala

                print(numero, asientos_totales, estado)
        return salas

    def _cargar_funciones(self, cine_folder: str, peliculas: dict, salas: dict): 
        funciones = []
        with open(f"{cine_folder}\\funciones.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                inicio = int(row[0])
                sala = int(row[1])
                nombre = row[2]
                id_ = int(row[3])
                entradas_vendidas = int(row[4])
                
                pelicula = peliculas[id_]
                horario = Horario(
                    datetime.fromtimestamp(inicio), 
                    datetime.fromtimestamp(inicio + (pelicula.duracion) * 60)
                )
                sala = salas[sala]

                funcion = Funcion(horario, sala, pelicula, entradas_vendidas)
                funciones.append(funcion)
                pelicula.funciones.append(funcion)
                sala.funciones.append(funcion)

                print(funcion.horario.inicio, funcion.horario.final, funcion.sala.numero, funcion.sala.asientos_totales,
                        funcion.sala.estado, funcion.pelicula.nombre, funcion.entradas_vendidas)

        return funciones


    def _cargar_peliculas(self, cine_folder: str, salas):
        peliculas = {}
        with open(f"{cine_folder}\\peliculas.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                nombre = row[0]
                id_ = int(row[1])
                duracion = int(row[2])
                año = int(row[3])
                generos = row[4].split(",")
                precio = int(row[5])
                dob_sub = int(row[6])

                pelicula = Pelicula(nombre, id_, duracion, año, DOB_SUB[dob_sub], precio, generos)

                peliculas[id_] = pelicula

                print(pelicula.nombre, pelicula.id, pelicula.duracion, pelicula.año, pelicula.generos, pelicula.precio, pelicula.dob_sub)

        
        self._cargar_funciones(cine_folder, peliculas, salas)
        return peliculas

    def _cargar_cine(self, cine: str):
        cine_folder = f"{os.getcwd()}\data\{cine}\\"

        total_ventas = self._cargar_ventas(cine_folder)
        trabajadores = self._cargar_trabajadores(cine_folder)
        salas = self._cargar_salas(cine_folder)
        peliculas = self._cargar_peliculas(cine_folder, salas)

        cine = Cine(cine, total_ventas, trabajadores, peliculas, salas)

        return cine

    def _cargar_cines(self):
        """
            Obtiene el nombre de todas las carpetas de cines en la carpeta data y las carga al programa. 
        """
        cines_names = []
        cines_dict = {}
        for item in os.scandir("./data"):
            if item.is_dir():
                cines_names.append(item.name)
        
        for cine in cines_names:
            cines_dict[cine] = self._cargar_cine(cine)

        return cines_dict

    def _cargar_cupones(self):
        cupones = {}
        with open(f"data\cupones.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)

            for row in csv_reader:
                codigo = row[0]
                porcentaje = int(row[1])
                utilizado = bool(int(row[2]))

                cupon = Cupon(codigo, porcentaje, utilizado)
                cupones[cupon.codigo] = cupon

        return cupones

    def ingresar(self, usuario: str, contraseña: str) -> object:
        """
            Recibe un usuario y contraseña, los cuáles verifica que coincidan con algún usuario del LoginModel.
            Retorna la referencia al usuario y el modelo a utilizar por el controlador en caso de que los datos sean válidos, 
            y None en caso contrario. 
        """
        usuario = self.usuarios.get(usuario)

        if usuario is not None:
            login_valido = usuario.verificar_contraseña(contraseña)

            if login_valido:
                if usuario.cargo == "administrador_global":
                    cines = self._cargar_cines()
                    modelo = usuario.crear_modelo(
                        usuario = usuario,
                        cines = cines
                    )
                else:
                    cine = self._cargar_cine(usuario.cine)
                    cupones = self._cargar_cupones()
                    modelo = usuario.crear_modelo(
                        usuario = usuario,
                        cine = cine,
                        cupones = cupones
                    )
                
                return usuario, modelo
        else:
            return None, None

