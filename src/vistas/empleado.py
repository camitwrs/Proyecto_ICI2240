from tkinter import Frame, Label, Button, StringVar, Entry
from tkinter.ttk import Combobox
class PageEmpleado(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ EMPLEADO:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=80)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Realizar venta", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageEmpleado))
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10) 
        
        boton2 = Button(self, text="Marcar asistencia", font='Helvetica 10 bold', command=lambda:self.controller.marcar_asistencia())
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        
        boton3 = Button(self, text="Informe de ventas", font='Helvetica 10 bold', command=lambda:self.informe_ventas)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        
        boton4 = Button(self, text="Ver horario", font='Helvetica 10 bold', command=lambda:self.controller.mostrar_horario())
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10)
        
    def marcar_asistencia(self):
        pass
    
    def informe_ventas(self):
        pass
    
    """def mostrar_horario(self):
        pass"""
        

class SubPageEmpleado(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Espacio en blanco, estética
        title = Label(self)
        title.configure(bg="#1C1C1C", fg="#ffffff")
        title.pack(pady=30)
        
        label1 = Label(self, text="SUBMENÚ REALIZAR VENTA:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=10)
        
        text1 = Label(self, text="Para vender la entrada, debe empezar desde la\n opción 1 hasta la opción 3.", font='Helvetica 9')
        text1.configure(bg="#1C1C1C", fg="#ffffff")
        text1.pack()
        text2 = Label(self, text="Usar la última opción SOLO si lo necesita.", font='Helvetica 9 bold')
        text2.configure(bg="#1C1C1C", fg="#ffffff")
        text2.pack(pady=10)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="1. Vender entrada", font='Helvetica 10 bold', command=lambda:self.controller.boton_vender_entrada())
        #lambda:master.switch_frame(PageVentaEntrada))
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10)
        
        boton2 = Button(self, text="2. Aplicar descuento", font='Helvetica 10 bold', command=lambda:self.controller.boton_aplicar_descuento())
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)

        boton3 = Button(self, text="3. Concretar venta", font='Helvetica 10 bold', command=lambda:self.controller.boton_concretar_venta())
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)

        boton4 = Button(self, text="Cancelar venta", font='Helvetica 10 bold', command=lambda:self.controller.boton_cancelar_venta())
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10) 
        
    """
    def venta_entrada(self):
        pass
    """    
    """
    def concretar_venta(self):
        pass
    
    def cancelar_venta(self):
        pass
    """
    
class PageVentaEntrada(Frame):
    def __init__(self, master):
        self.controller = master.controller
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")

        self.texto = StringVar()
        
        self.lista_pelis = []
        self.lista_funciones = []
        
        #Espacio en blanco, estética
        title = Label(self)
        title.configure(bg="#1C1C1C", fg="#ffffff")
        title.pack(pady=50)
        
        label1 = Label(self, text="Seleccione película", font='Helvetica 10 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=10)  
        self.combo1 = Combobox(self, state="readonly", width=50, values=self.lista_pelis)  
        self.combo1.bind("<<ComboboxSelected>>", self._callback_peliculas)                           
        self.combo1.pack()
    
        label3 = Label(self, text="Seleccione horario", font='Helvetica 10 bold')
        label3.configure(bg="#1C1C1C", fg="#ffffff")
        label3.pack(pady=10)  
        self.combo2 = Combobox(self, state="readonly", width=50, values=self.lista_funciones)  
        self.combo2.bind("<<ComboboxSelected>>", self._callback_funciones)                             
        self.combo2.pack()
        
        retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageEmpleado))
        retroceder.configure(bg="#9FA0FF")
        retroceder.pack(pady=30)
        
    def set_peliculas(self, peliculas: dict):
        self.opciones_peliculas = peliculas

        for pelicula in peliculas.keys():
            self.combo1['values'] = (*self.combo1['values'], pelicula)

    def set_funciones(self, funciones: dict):
        self.opciones_funciones = funciones
        self.combo2['values'] = ""

        for funcion in funciones.keys():
            self.combo2['values'] = (*self.combo2['values'], funcion)
        
    def _callback_peliculas(self, event_object):
        self.combo2.set("")
        self.controller.get_funciones(self.opciones_peliculas[event_object.widget.get()])

    def _callback_funciones(self, event_object):
        id_pelicula, inicio = self.opciones_funciones[event_object.widget.get()]
        self.controller.guardar_venta(id_pelicula, inicio)
                
class PageDescuento(Frame):        
    def __init__(self, master):
        self.controller = master.controller
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Espacio en blanco, estética
        title = Label(self)
        title.configure(bg="#1C1C1C", fg="#ffffff")
        title.pack(pady=50)
        
        label1 = Label(self, text="Ingrese el código de descuento", font='Helvetica 10 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=10) 
         
        cupon = StringVar()
        entry_cup = Entry(self, width=20, textvariable=cupon)
        entry_cup.configure(bg="#DADDD8")
        entry_cup.pack(pady=10) 
        
        boton_verificar = Button(self, text="Verificar código", 
                                command=lambda:self.controller.verificar_cupon(cupon.get()), 
                                font='Helvetica 10 bold')
        boton_verificar.pack(pady=10)
        
        retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=master.switch_frame(SubPageEmpleado))
        retroceder.configure(bg="#9FA0FF")
        retroceder.pack(pady=10)
