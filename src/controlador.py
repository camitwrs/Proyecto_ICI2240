from src.modelos.login import LoginModel
from src.vistas.application import Aplicacion
from src.vistas.empleado import PageEmpleado
from src.vistas.admin_local import PageAdminLocal
from src.vistas.admin_global import PageAdminGlobal


class Controller:
    def __init__(self):
        self.model = LoginModel()
        
        self.view = Aplicacion(self)
        self.view.mainloop()

    def _switch_context(self, model, view):
        """
            Función que modifica tanto la vista como el modelo lógico de la aplicación.
            El modelo y la vista se asignan según el tipo de usuario que inicie sesión.
        """
        self.model = model
        self.view.switch_frame(view)

    def ingresar(self, usuario: str, contraseña: str):
        """ 
            Función que recibe las credenciales de inicio de sesión desde la GUI y verifica en el model.
            Si las credenciales son correctas, se despliega el menú correspondiente según el cargo.
        """
        usuario, model = self.model.ingresar(usuario, contraseña)

        if usuario is None or model is None:
            self.view.throw_messagebox("LOGIN", "Error. Inténtelo nuevamente")
        elif usuario.cargo == "empleado":
            self._switch_context(model, PageEmpleado)
        elif usuario.cargo == "administrador_local":
            self._switch_context(model, PageAdminLocal)
        elif usuario.cargo == "administrador_global":
            self._switch_context(model, PageAdminGlobal)
            
    def mostrar_horario(self):
        self.model.mostrar_horario_mod()
        
    def marcar_asistencia(self):
        self.model.marcar_asistencia_mod()