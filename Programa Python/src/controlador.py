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
        print("busca al usuario")

        if usuario is None:
            print("primer if")
            self.view.throw_messagebox("LOGIN", "Error. Inténtelo nuevamente")
        elif usuario.cargo == "empleado":
            print("segundo if")
            self.view.switch_frame(PageEmpleado)
        elif usuario.cargo == "administrador_local":
            print("tercer if")
            self.view.switch_frame(PageAdminLocal)
        elif usuario.cargo == "administrador_global":
            print("cuarto if")
            self.view.switch_frame(PageAdminGlobal)