from tkinter import Frame, Label, Button, StringVar, Entry
from tkinter.ttk import Combobox


class PageEmpleado(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ EMPLEADO:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=80)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Realizar venta", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageEmpleado))
        boton1.configure(bg="#cccccccff", fg="#1c1c1c")
        boton1.pack(pady=10) 
        
        boton2 = Button(self, text="Marcar asistencia", font='Helvetica 10 bold', command=lambda:self.controller.marcar_asistencia())
        boton2.configure(bg="#cccccccff", fg="#1c1c1c")
        boton2.pack(pady=10)
        
        boton3 = Button(self, text="Informe de ventas", font='Helvetica 10 bold', command=lambda:self.controller.informe_ventas())
        boton3.configure(bg="#cccccccff", fg="#1c1c1c")
        boton3.pack(pady=10)
        
        boton4 = Button(self, text="Ver horario", font='Helvetica 10 bold', command=lambda:self.controller.mostrar_horario())
        boton4.configure(bg="#cccccccff", fg="#1c1c1c")
        boton4.pack(pady=10)
        

class SubPageEmpleado(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        # INFORMACION ADICIONAL PARA EL USUARIO
        title = Label(self)
        title.configure(bg="#33353d")
        title.pack(pady=30)
        
        label1 = Label(self, text="SUBMENÚ REALIZAR VENTA:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=10)
        
        text1 = Label(self, text="Para vender la entrada, debe empezar desde la\n opción 1 hasta la opción 3.", font='Helvetica 9')
        text1.configure(bg="#33353d", fg="#cccccccff")
        text1.pack()
        text2 = Label(self, text="Usar la última opción SOLO si lo necesita.", font='Helvetica 9 bold')
        text2.configure(bg="#33353d", fg="#cccccccff")
        text2.pack(pady=10)
        
        # BOTONES 
        boton1 = Button(self, text="1. Vender entrada", font='Helvetica 10 bold', command=lambda:self.controller.boton_vender_entrada())
        boton1.configure(bg="#cccccccff", fg="#1c1c1c")
        boton1.pack(pady=10)
        
        boton2 = Button(self, text="2. Aplicar descuento", font='Helvetica 10 bold', command=lambda:self.controller.boton_aplicar_descuento())
        boton2.configure(bg="#cccccccff", fg="#1c1c1c")
        boton2.pack(pady=10)

        boton3 = Button(self, text="3. Concretar venta", font='Helvetica 10 bold', command=lambda:self.controller.boton_concretar_venta())
        boton3.configure(bg="#cccccccff", fg="#1c1c1c")
        boton3.pack(pady=10)

        boton4 = Button(self, text="Cancelar venta", font='Helvetica 10 bold', command=lambda:self.controller.boton_cancelar_venta())
        boton4.configure(bg="#cccccccff", fg="#1c1c1c")
        boton4.pack(pady=10) 

    
class PageVentaEntrada(Frame):
    def __init__(self, master):
        self.controller = master.controller
        Frame.__init__(self, master)
        self.configure(bg="#33353d")

        self.texto = StringVar()
        
        self.lista_pelis = []
        self.lista_funciones = []
        
        title = Label(self)
        title.configure(bg="#33353d")
        title.pack(pady=50)
        
        label1 = Label(self, text="Seleccione película", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=10)  
        self.combo1 = Combobox(self, state="readonly", width=50, values=self.lista_pelis)  
        self.combo1.bind("<<ComboboxSelected>>", self._callback_peliculas)                           
        self.combo1.pack()
    
        label3 = Label(self, text="Seleccione horario", font='Helvetica 10 bold')
        label3.configure(bg="#33353d", fg="#cccccccff")
        label3.pack(pady=10)  
        self.combo2 = Combobox(self, state="readonly", width=50, values=self.lista_funciones)  
        self.combo2.bind("<<ComboboxSelected>>", self._callback_funciones)                             
        self.combo2.pack()
        
        retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageEmpleado))
        retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        retroceder.pack(pady=30)
        
    def set_peliculas(self, peliculas: dict):
        """ Añade las películas que ingresan por parámetro a un combobox. """
        self.opciones_peliculas = peliculas

        for pelicula in peliculas.keys():
            self.combo1['values'] = (*self.combo1['values'], pelicula)

    def set_funciones(self, funciones: dict):
        """ Añade las funciones que ingresan por parámetro a un combobox. """
        self.opciones_funciones = funciones
        self.combo2['values'] = ""

        for funcion in funciones.keys():
            self.combo2['values'] = (*self.combo2['values'], funcion)
        
    def _callback_peliculas(self, event_object):
        """ Función que se llamada cuando es seleccionada una película. """
        self.combo2.set("")
        self.controller.get_funciones(self.opciones_peliculas[event_object.widget.get()])

    def _callback_funciones(self, event_object):
        """ Función que es llamada cuando es seleccionada una función. """
        id_pelicula, inicio = self.opciones_funciones[event_object.widget.get()]
        self.controller.guardar_venta(id_pelicula, inicio)
                
class PageDescuento(Frame):        
    def __init__(self, master):
        self.controller = master.controller
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Espacio en blanco, estética
        title = Label(self)
        title.configure(bg="#33353d")
        title.pack(pady=50)
        
        label1 = Label(self, text="Ingrese el código de descuento", font='Helvetica 10 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=10) 
         
        cupon = StringVar()
        entry_cup = Entry(self, width=20, textvariable=cupon)
        entry_cup.configure(bg="#e6e1da")
        entry_cup.pack(pady=10) 
        
        boton_verificar = Button(self, text="Verificar código", 
                                command=lambda:self.controller.verificar_cupon(cupon.get()), 
                                font='Helvetica 10 bold')
        boton_verificar.configure(bg="#cccccccff", fg="#1c1c1c")
        boton_verificar.pack(pady=10)
        
        retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageEmpleado))
        retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        retroceder.pack(pady=10)
