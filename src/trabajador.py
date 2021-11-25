from abc import ABC, abstractmethod
from .cine import Cine
from src.modelos.empleado_model import EmpleadoModel
from src.modelos.admin_local_model import AdminLocalModel

class Trabajador(ABC):
    def __init__(self, rut, contraseña, cargo, cine):
        super().__init__()

        self.rut = rut
        self.contraseña = contraseña
        self.cargo = cargo
        self.cine = cine

        """ Variables que se cargan solo una vez que se carga un cine y la información de los empleados. """
        self.nombre = ""
        self.sueldo = 0
        self.ventas = 0
        self.horarios = None # Debería ser un treemap
        self.asistencia = None # Deberia ser una lista

    @abstractmethod
    def crear_modelo(self, **kwargs):
        pass

    def verificar_contraseña(self, contraseña: str) -> bool:
        """ Recibe un string y verifica si coincide con la contraseña correspondiente. """
        if self.contraseña == contraseña:
            return True
        return False

class Empleado(Trabajador):
    def crear_modelo(self, **kwargs):
        usuario = kwargs.get("usuario")
        cine = kwargs.get("cine")

        if usuario is None or not isinstance(usuario, Empleado):
            return None
        if cine is None or not isinstance(cine, Cine):
            return None

        return AdminLocalModel(usuario, cine)

class AdminLocal(Trabajador):
    def crear_modelo(self, **kwargs):
        usuario = kwargs.get("usuario")
        cine = kwargs.get("cine")

        if usuario is None or not isinstance(usuario, AdminLocal):
            return None
        if cine is None or not isinstance(cine, Cine):
            return None

        return EmpleadoModel(usuario, cine)

class AdminGlobal(Trabajador):
    def crear_modelo(self, **kwargs):
        usuario = kwargs.get("usuario")
        cines = kwargs.get("cines")

        if usuario is None or not isinstance(usuario, AdminGlobal):
            return None
        if cines is None:
            return None

        return EmpleadoModel(usuario, cines)