from tkinter import Frame, Label, Button


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
        
        boton2 = Button(self, text="Marcar asistencia", font='Helvetica 10 bold', command=lambda:self.marcar_asistencia)
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        
        boton3 = Button(self, text="Informe de ventas", font='Helvetica 10 bold', command=lambda:self.informe_ventas)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        
        boton4 = Button(self, text="Ver horario", font='Helvetica 10 bold', command=lambda:self.mostrar_horario)
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10)
        
    def marcar_asistencia(self):
        pass
    
    def informe_ventas(self):
        pass
    
    def mostrar_horario(self):
        pass

class SubPageEmpleado(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="SUBMENÚ REALIZAR VENTA:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=80)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Vender entrada", font='Helvetica 10 bold', command=lambda:self.venta_entrada)
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10)
        boton2 = Button(self, text=" Aplicar descuento", font='Helvetica 10 bold', command=lambda:self.aplicar_descuento)
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        boton3 = Button(self, text="Concretar venta", font='Helvetica 10 bold', command=lambda:self.concretar_venta)
        boton3.configure(bg="#ECEBE4")
        boton3.pack( pady=10)
        boton4 = Button(self, text="Cancelar venta", font='Helvetica 10 bold', command=lambda:self.cancelar_venta)
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10) 
        
    def venta_entrada(self):
        pass
    
    def aplicar_descuento(self):
        pass
    
    def concretar_venta(self):
        pass
    
    def cancelar_venta(self):
        pass