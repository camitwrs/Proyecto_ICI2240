from abc import ABC, abstractmethod


class Trabajador(ABC):
    def __init__(self, rut, contraseña, cargo, cine):
        self.rut = rut
        self.contraseña = contraseña
        self.cargo = cargo
        self.cine = cine

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
