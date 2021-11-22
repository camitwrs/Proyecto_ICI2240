from tkinter import Tk
from src.modelos.sistema import Sistema
from src.vistas.application import Aplicacion
from src.vistas.empleado import PageEmpleado
from src.vistas.admin_local import PageAdminLocal
from src.vistas.admin_global import PageAdminGlobal


class Controller:
    def __init__(self):
        self.model = Sistema()
        
        self.view = Aplicacion(self)
        self.view.mainloop()

    def ingresar(self, usuario: str, contraseña: str):
        """ 
            Función que recibe las credenciales de inicio de sesión desde la GUI y verifica en el model.
            Si las credenciales son correctas, se despliega el menú correspondiente según el cargo.
        """
        usuario = self.model.ingresar(usuario, contraseña)

        if usuario is None:
            self.view.throw_messagebox("LOGIN", "Error. Inténtelo nuevamente")
        elif usuario.cargo == "empleado":
            self.view.switch_frame(PageEmpleado)
        elif usuario.cargo == "administrador_local":
            self.view.switch_frame(PageAdminLocal)
        elif usuario.cargo == "administrador_global":
            self.view.switch_frame(PageAdminGlobal)