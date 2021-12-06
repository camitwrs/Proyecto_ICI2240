from src.modelos.login import LoginModel
from src.vistas.application import Aplicacion
from src.vistas.empleado import PageEmpleado, SubPageEmpleado, PageDescuento, PageVentaEntrada
from src.vistas.admin_local import PageAdminLocal, PageModificarEmpleados, PageModificarSalas
from src.vistas.admin_global import PageAdminGlobal, PageModificarPrecio, PageEliminarAdmin, PageAgregarAdmin


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

    def informe_ventas(self):
        nombre, rut, ventas = self.model.informe_ventas()

        self.view.throw_messagebox("Ventas", f"{nombre} - {rut}\n\nHas realizado un total de {ventas}.")

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
    def añadir_pelicula(self, nombre: str, año: str, duracion: str, precio: str, generos: str, dob_sub: str):
        if len(nombre) == 0 or len(año) == 0 or len(duracion) == 0 or len(precio) == 0 or len(generos) == 0 or len(dob_sub) == 0:
            self.view.throw_error("Error", "Por favor rellena todos los campos que se solicitan.")
        elif not año.isdigit() or not duracion.isdigit() or not precio.isdigit():
            self.view.throw_error("Error", "Asegura de ingresar numeros enteros en los campos que lo requieran.")
        else:
            self.model.añadir_pelicula(nombre, año, duracion, precio, generos, dob_sub)

    def boton_modificar_empleados(self):
        empleados = self.model.get_empleados()
        
        self.view.switch_frame(PageModificarEmpleados)
        self.view._frame.set_empleados(empleados)

    def eliminar_empleado(self):
        selected_empleado = self.view._frame.selected_empleado
        if selected_empleado is None:
            self.view.throw_error("Error", "Por favor selecciona uno de los empleados en la lista de abajo antes de hacer click en el botón.")
            return

        result = self.model.eliminar_empleado(selected_empleado[1])

        if result:
            self.view._frame.eliminar_empleado(selected_empleado[0])

    def añadir_empleado(self, rut, contraseña, nombre_completo, sueldo):
        if len(rut) == 0 or len(contraseña) == 0 or len(nombre_completo) == 0 or len(sueldo) == 0:
            self.view.throw_error("Error", "Al menos uno de los campos de información necesarios para agregar al empleado está vacio.")
            return

        if not rut.isdigit() or not sueldo.isdigit():
            self.view.throw_error("Error", "El valor ingresado para el rut o el sueldo no es válido. Asegurate que corresponde a un número entero.")
            return

        empleado = self.model.añadir_empleado(rut, contraseña, nombre_completo, sueldo)
        
        if empleado is not None:
            self.view._frame.añadir_empleado(empleado)
        else:
            self.view.throw_error("Error", "El empleado a agregar ya tiene una cuenta creada en el sistema.")

    def boton_modificar_salas(self):
        salas = self.model.get_salas()
        
        self.view.switch_frame(PageModificarSalas)
        self.view._frame.set_salas(salas)

    def habilitar_sala(self):
        selected_sala = self.view._frame.selected_sala
        if selected_sala is None:
            self.view.throw_error("Error", "Por favor selecciona alguna de las salas antes de presionar el botón.")
            return
        
        self.model.habilitar_sala(selected_sala[1]['text'])
        self.view._frame.update_sala(selected_sala[0], selected_sala[1]['text'], selected_sala[1]['values'])

    def deshabilitar_sala(self):
        selected_sala = self.view._frame.selected_sala
        if selected_sala is None:
            self.view.throw_error("Error", "Por favor selecciona alguna de las salas antes de presionar el botón.")
            return

        self.model.deshabilitar_sala(selected_sala[1]['text'])
        self.view._frame.update_sala(selected_sala[0], selected_sala[1]['text'], selected_sala[1]['values'])

    """ FUNCIONES ADMINISTRADOR GLOBAL """
    def generar_cupones(self, cantidad, porcentaje):
        if len(cantidad) == 0 or len(porcentaje) == 0:
            self.view.throw_error("Error", "Por favor especifica un valor para ambos campos.")
        elif not cantidad.isdigit() or not porcentaje.isdigit():
            self.view.throw_error("Error", "Por favor asegurate que los valores ingresados sean números enteros positivos.")
        elif int(porcentaje) < 1 or int(porcentaje) > 100:
            self.view.throw_error("Error", "Por favor asegurate que el porcentaje sea mayor o igual a 1 y menor o igual a 100.")

        result = self.model.generar_cupones(int(cantidad), int(porcentaje))

        if result:
            self.view.throw_messagebox("Exito", "Los cupones han sido generados con éxito.")
        else:
            self.view.throw_error("Error", "Ha occurido un error al generar los cupones.")

    def boton_modificar_precios(self):
        self.view.switch_frame(PageModificarPrecio)

        peliculas = self.model.get_precios_peliculas()
        if len(peliculas) > 0:
            self.view._frame.set_peliculas(peliculas)

    def modificar_precio(self, precio):
        selected_pelicula = self.view._frame.selected_pelicula
        if selected_pelicula is None:
            self.view.throw_error("Error", "Por favor selecciona alguna de las películas antes de presionar el botón.")
            return
        if len(precio) == 0:
            self.view.throw_error("Error", "El campo del precio se encuentra vacio.")
            return
        if not precio.isdigit():
            self.view.throw_error("Error", "Por favor asegura que el precio corresponde a un número entero")
            return

        self.model.modificar_precio(selected_pelicula[1]['text'], selected_pelicula[1]['values'][1], int(precio))
        selected_pelicula[1]['values'][3] = int(precio)
        self.view._frame.update_pelicula(selected_pelicula[0], selected_pelicula[1]['text'], selected_pelicula[1]['values'])

    def boton_agregar_local_adm(self):
        self.view.switch_frame(PageAgregarAdmin)

    def boton_eliminar_local_adm(self):
        local_admins = self.model.get_local_admins()
        self.view.switch_frame(PageEliminarAdmin)
        self.view._frame.set_admins(local_admins)

    def eliminar_admin(self, rut):
        cine = self.view._frame.search_and_del_admin(rut)
        if cine is None:
            self.view.throw_error("Error", "El RUT ingresado no corresponde a ningún admin local.")
        else:
            self.model.eliminar_admin(rut, cine)

    def agregar_admin(self, nombre, rut, contraseña, cine, sueldo):
        result = self.model.agregar_admin(nombre, rut, contraseña, cine, sueldo)

        if not result:
            self.view.throw_error("Error", "Ha ocurrido un error al agregar al administrador, asegurate que el nombre de cine es correcto y que el usuario no exista en el sistema.")
        else:
            self.view.throw_messagebox("Exito", "El administrador local ha sido agregado con éxito al sistema.")