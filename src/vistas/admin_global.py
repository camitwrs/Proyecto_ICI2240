from tkinter import Frame, Label, Button


class PageAdminGlobal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ ADMINISTRADOR GLOBAL:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=70)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Modificar administradores", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageAdminGlobal))
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10)
        boton2 = Button(self, text="Modificar cine", font='Helvetica 10 bold', command=lambda:self.modificar_cine)
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)
        boton3 = Button(self, text="Ver información cine", font='Helvetica 10 bold', command=lambda:self.mostrar_info_cine)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        boton4 = Button(self, text="Modificar precios películas", font='Helvetica 10 bold', command=lambda:self.modificar_precios_totales)
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10)
        boton5 = Button(self, text="Generar cupones de descuento", font='Helvetica 10 bold', command=lambda:self.generar_cupones)
        boton5.configure(bg="#ECEBE4")
        boton5.pack(pady=10)
        boton6 = Button(self, text="Realizar reporte", font='Helvetica 10 bold', command=lambda:self.realizar_reporte)
        boton6.configure(bg="#ECEBE4")
        boton6.pack(pady=10)

    def modificar_cine(self):
        pass
    
    def mostrar_info_cine(self):
        pass
    
    def modificar_precios_totales(self):
        pass
    
    def generar_cupones(self):
        pass
    
    def realizar_reporte(self):
        pass
    
class SubPageAdminGlobal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el texto del menú
        label1 = Label(self, text="SUBMENÚ MODIFICAR ADMINISTRADORES:", font='Helvetica 12 bold')
        label1.configure(bg="#1C1C1C", fg="#ffffff")
        label1.pack(pady=100)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Agregar administrador local", font='Helvetica 10 bold', command=lambda:self.agregar_adminlocal)
        boton1.configure(bg="#ECEBE4")
        boton1.pack(pady=10)
        boton2 = Button(self, text="Eliminar administrador local", font='Helvetica 10 bold', command=lambda:self.eliminar_adminlocal)
        boton2.configure(bg="#ECEBE4")
        boton2.pack(pady=10)

    def agregar_adminlocal(self):
        pass
    
    def eliminar_adminlocal(self):
        pass