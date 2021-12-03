from abc import ABC, abstractmethod
from src.modelos.empleado_model import EmpleadoModel
from src.modelos.admin_local_model import AdminLocalModel
from src.modelos.admin_global_model import AdminGlobalModel

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
        cupones = kwargs.get("cupones")

        if usuario is None or cine is None or cupones is None:
            return None

        return EmpleadoModel(usuario, cine, cupones)

    def get_horario_semana(self):
        """
            Retorna una lista con los horarios del empleado que correspondan
        """
        horarios = []

        for horario in self.horarios:
            if horario.same_week():
                horarios.append(horario)
            else:
                print(f"{horario.inicio} no corresponde a un horario en la misma semana")

        return horarios

    def get_horario_actual(self):
        """
            Verifica si la hora actual corresponde a un horario de trabajo válido (según horarios en self.horarios)
            Retorna la hora de inicio del horario si es un horario válido y None en caso contrario.
        """
        for horario in self.horarios:
            if horario.is_horario_actual():
                return horario.inicio

        return None

class AdminLocal(Trabajador):
    def crear_modelo(self, **kwargs):
        usuario = kwargs.get("usuario")
        cine = kwargs.get("cine")

        if usuario is None or cine is None:
            return None

        return AdminLocalModel(usuario, cine)

class AdminGlobal(Trabajador):
    def crear_modelo(self, **kwargs):
        usuario = kwargs.get("usuario")
        cines = kwargs.get("cines")

        if usuario is None or cines is None:
            return None

        return AdminGlobalModel(usuario, cines)