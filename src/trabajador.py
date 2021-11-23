from abc import ABC, abstractmethod


class Trabajador(ABC):
    def __init__(self, rut, contraseña, cargo, cine):
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

    def verificar_contraseña(self, contraseña: str) -> bool:
        """ Recibe un string y verifica si coincide con la contraseña correspondiente. """
        if self.contraseña == contraseña:
            return True
        return False

class Empleado(Trabajador):
    def mostrar_cargo(self):
        return self.cargo

class AdminLocal(Trabajador):
    def mostrar_cargo(self):
        return self.cargo

class AdminGlobal(Trabajador):
    def mostrar_cargo(self):
        return self.cargo
