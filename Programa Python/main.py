from tkinter import *
from tkinter import messagebox

class Aplicacion(Tk):
    #Crea la ventana 
    def __init__(self):
        Tk.__init__(self)
        self.title("C4U")
        self.geometry("960x540")
        self.configure(bg="#1C1C1C")
        self.resizable(0,0)
        self._frame = None
        
        #Llama a la página de LOGIN
        self.switch_frame(PageLogin)

    #Cambia entre páginas (frames)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class PageLogin(Frame):
    def __init__(self, master):
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")
        
        #Añade el título del programa en el frame, con colores y posición (configure y pack)
        texto_titulo = Label(self, text="CINE4U", font='Helvetica 30 bold')
        texto_titulo.configure(bg="#1C1C1C", fg="#ffffff")
        texto_titulo.pack(pady=70)
        
        #Añade el texto para ingresar rut en el frame
        texto_usuario = Label(self, text="Ingrese su RUT:", font='Helvetica 12 bold')
        texto_usuario.configure(bg="#1C1C1C", fg="#ffffff")
        texto_usuario.pack()
        
        #Añade la entrada para el rut del usuario
        usuario = StringVar()
        entry_usuario = Entry(self, width=20, textvariable=usuario)
        entry_usuario.configure(bg="#DADDD8")
        entry_usuario.pack(pady=10) 
        
        #Añade el texto para ingresar la contraseña en el frame
        texto_contra = Label(self, text="Ingrese su contraseña:", font='Helvetica 12 bold')
        texto_contra.configure(bg="#1C1C1C", fg="#ffffff")
        texto_contra.pack()
        
        #Añade la entrada para la contraseña del usuario
        contra = StringVar()
        entry_contra = Entry(self, width=20, show="*", textvariable=contra)
        entry_contra.configure(bg="#DADDD8")
        entry_contra.pack(pady=10)
        
        #Añade el botón entrar en el frame
        boton_principal = Button(self, text="Entrar", command=lambda:self.ingresar(usuario, contra, master), font='Helvetica 9 bold')
        boton_principal.configure(bg="#9FA0FF")
        boton_principal.pack(pady=10)
        
        #Añade el texto de recordatorio
        reminder = Label(self, text="Recordar: RUT sin puntos ni dígito verificador.", font='Helvetica 8 ')
        reminder.configure(bg="#1C1C1C", fg="#ffffff")
        reminder.pack(pady=80)  
    
    def ingresar(self, usuario, contra, master):
        # Asume que el que entra es un EMPLEADO. Funciona con user: 20603557 y pass: 2310
        if usuario.get() == "20603557" and contra.get() == "2310": 
            master.switch_frame(PageEmpleado)
            
        # Asume que el que entra es un ADMIN LOCAL. Funciona con user: 11111111 y pass: 2310
        elif usuario.get() == "11111111" and contra.get() == "2310":
            master.switch_frame(PageAdminLocal)
            
        # Asume que el que entra es un ADMIN GLOBAL. Funciona con user: 22222222 y pass: 2310
        elif usuario.get() == "22222222" and contra.get() == "2310":
            master.switch_frame(PageAdminGlobal)
        else:
            # Si el user no se encuentra, o está mal escrito, muestra un mensaje
            messagebox.showinfo("LOGIN", "Error. Inténtelo nuevamente")

class PageEmpleado(Frame):
    def __init__(self, master):
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

class PageAdminLocal(Frame):
    def __init__(self, master):
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

class PageAdminGlobal(Frame):
    def __init__(self, master):
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
    
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()