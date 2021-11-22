import csv
import os
from src.trabajador import Empleado, AdminGlobal, AdminLocal

class Sistema:
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
            Carga los datos iniciales de todos los trabajadores del sistema.
            Se almacenan los objetos de los trabajadores en un dict, en la variable self.usuarios.
        """
        usuarios = {}

        """
            El absolute_path deberia cambiar dependiendo como esté ordenado el proyecto.
        """
        path = os.getcwd()
        print(path)
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

    def ingresar(self, usuario: str, contraseña: str) -> object:
        """
            Recibe un usuario y contraseña, los cuáles verifica que coincidan con algún usuario del sistema.
            Retorna la referencia al usuario en caso de que los datos sean válidos, y None en caso contrario. 
        """
        usuario = self.usuarios.get(usuario)

        if usuario is not None:
            login_valido = usuario.verificar_contraseña(contraseña)

            if login_valido:
                self.sesion_activa = usuario
                return usuario
        else:
            return None

