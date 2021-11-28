from src.modelos.login import LoginModel
from src.vistas.application import Aplicacion
from src.vistas.empleado import PageDescuento, PageEmpleado, PageVentaEntrada
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

    """ FUNCIONES DE LOGIN """
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

    
    """ FUNCIONES DE EMPLEADO """
    def boton_vender_entrada(self):
        opciones_pelis = self.model.get_peliculas()
        
        if opciones_pelis is None:
            self.view.throw_messagebox("VENTA", "Error. No hay películas disponibles")
        else:
            self.view.switch_frame(PageVentaEntrada)
            self.view._frame.set_peliculas(opciones_pelis)

    def boton_aplicar_descuento(self):
        self.view.switch_frame(PageDescuento)
    
    def boton_concretar_venta(self):
        """
        aquí debería haber código juasjuasjuas
        """
    
    def boton_cancelar_venta(self):
        """
        aquí debería haber código juasjuasjuas
        """
        self.view.switch_frame(PageEmpleado)
        
    def get_funciones(self, id_pelicula: id):
        opciones_funciones = self.model.get_funciones(id_pelicula)
        
        if len(opciones_funciones) == 0:
            self.view.throw_messagebox("VENTA", "Error. No hay funciones disponibles")
        else:
            self.view._frame.set_funciones(opciones_funciones)

    def guardar_venta(self, id_pelicula, inicio):
        self.model.guardar_venta(id_pelicula, inicio)

    def mostrar_horario(self):
        self.model.mostrar_horario_mod()
        
    def marcar_asistencia(self):
        self.model.marcar_asistencia_mod()