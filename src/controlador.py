from src.modelos.login import LoginModel
from src.vistas.application import Aplicacion
from src.vistas.empleado import PageEmpleado, SubPageEmpleado, PageDescuento, PageVentaEntrada
from src.vistas.admin_local import PageAdminLocal, PageModificarEmpleados
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
        output = self.model.ingresar(usuario, contraseña)

        if output is None:
            self.view.throw_error("LOGIN", "Error. Inténtelo nuevamente")
            return
        else:
            usuario, model = output
        
        if usuario.cargo == "empleado":
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

    def boton_aplicar_descuento(self) -> None:
        self.view.switch_frame(PageDescuento)
    
    def boton_concretar_venta(self):
        boleta = self.model.concretar_venta()

        if boleta is None:
            self.view.throw_error("VENTA", "Ha ocurrido un error al procesar la venta.")
            return

        boleta_concatenada = f"Película {boleta['nombre_pelicula']}\nSala: {boleta['sala']}\nHora inicio: {boleta['hora_inicio']}\nPrecio: {int(boleta['precio'])}"
        result = self.view.throw_question("BOLETA", boleta_concatenada)
        
        if result:
            self.model.concretar_venta_confirmacion(boleta)
            self.view.throw_messagebox("VENTA", "La venta ha sido realizada con éxito.")
            self.view.switch_frame(PageEmpleado)
    
    def boton_cancelar_venta(self):
        self.model.cancelar_venta()
        self.view.throw_messagebox("VENTA", "La venta ha sido cancelada.")
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
        horarios_concatenados = self.model.mostrar_horario_mod()

        if len(horarios_concatenados) > 0:
            self.view.throw_messagebox("HORARIOS", horarios_concatenados)
        
    def marcar_asistencia(self):
        result = self.model.marcar_asistencia_mod()

        if result[0]:
            self.view.throw_messagebox("ASISTENCIA", result[1])
        else:
            self.view.throw_error("ASISTENCIA", result[1])

    def verificar_cupon(self, codigo: str) -> None:
        cupon_valido = self.model.verificar_cupon(codigo)

        if cupon_valido:
            self.view.throw_messagebox("DESCUENTO", "El cupón de descuento ha sido aplicado con éxito")
            self.view.switch_frame(SubPageEmpleado)
        else:
            self.view.throw_messagebox("DESCUENTO", "El código de cupón de descuento ingresado no es válido")



    """ FUNCIONES DE ADMIN LOCAL """
    def boton_modificar_empleados(self):
        empleados = self.model.get_empleados()
        
        self.view.switch_frame(PageModificarEmpleados)
        self.view._frame.set_empleados(empleados)

    def eliminar_empleado(self):
        selected_empleado = self.view._frame.selected_empleado
        result = self.model.eliminar_empleado(selected_empleado[1])

        if result:
            self.view._frame.eliminar_empleado(selected_empleado[0])