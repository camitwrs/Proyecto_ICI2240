from tkinter import Frame, Label, Button


class PageAdminLocal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ ADMINISTRADOR LOCAL:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=80)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Resumen general", font='Helvetica 10 bold', command=lambda:self.resumen_general)
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10)
        boton2 = Button(self, text="Modificar cartelera", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageAdminLocal))
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        boton3 = Button(self, text="Informe de ventas", font='Helvetica 10 bold', command=lambda:self.informe_ventas)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        boton4 = Button(self, text="Ver horario", font='Helvetica 10 bold', command=lambda:self.mostrar_horario)
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10)
    
    def resumen_general(self):
        pass
    
    def informe_ventas(self):
        pass
    
    def mostrar_horario(self):
        pass
    
class SubPageAdminLocal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="SUBMENÚ MODIFICAR CARTELERA:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=80)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Añadir película", font='Helvetica 10 bold', command=lambda:self.anadir_pelicula)
        boton1.configure(bg="#ECEBE4")
        boton1.pack( pady=10)
        boton2 = Button(self, text="Añadir funciones", font='Helvetica 10 bold', command=lambda:self.anadir_funciones)
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        boton3 = Button(self, text="Cancelar funciones", font='Helvetica 10 bold', command=lambda:self.cancelar_funciones)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        boton4 = Button(self, text="Modificar precio funciones", font='Helvetica 10 bold', command=lambda:self.modificar_precios)
        boton4.configure(bg="#ECEBE4")
        boton4.pack( pady=10)   
        
    def anadir_pelicula(self):
        pass
    
    def anadir_funciones(self):
        pass
    
    def cancelar_funciones(self):
        pass
    
    def modificar_precios(self):
        pass