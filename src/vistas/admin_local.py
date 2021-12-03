from tkinter import Frame, Label, Button, END, StringVar, Entry
from tkinter import ttk


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
        boton3 = Button(self, text="Informe de personal", font='Helvetica 10 bold', command=lambda:self.informe_ventas)
        boton3.configure(bg="#ECEBE4")
        boton3.pack(pady=10)
        boton4 = Button(self, text="Modificar empleados", font='Helvetica 10 bold', command=lambda:self.controller.boton_modificar_empleados())
        boton4.configure(bg="#ECEBE4")
        boton4.pack(pady=10)
        boton5 = Button(self, text="Administar horario", font='Helvetica 10 bold', command=lambda:self.mostrar_horario)
        boton5.configure(bg="#ECEBE4")
        boton5.pack(pady=10)
        boton6 = Button(self, text="Modificar salas", font='Helvetica 10 bold', command=lambda:self.mostrar_horario)
        boton6.configure(bg="#ECEBE4")
        boton6.pack(pady=10)
        

class PageModificarEmpleados(ttk.Frame): 
    """
        FALTA AGREGAR LA OPCION PARA AÑADIR EMPLEADOS, OSEA TODOS LOS INPUT DE DATOS Y UN BOTÓN PARA AGREGAR
    """
    def __init__(self, master):
        self.controller = master.controller
        self.selected_empleado = None

        Frame.__init__(self, master)
        self.configure(bg="#1C1C1C")

        #Añade el texto para ingresar rut en el frame
        self.texto_rut = Label(self, text="RUT:", font='Helvetica 12 bold')
        self.texto_rut.configure(bg="#1C1C1C", fg="#ffffff")
        self.texto_rut.grid(row=0, column=0)
        #texto_rut.pack()
        
        # #Añade la entrada para el rut del usuario
        self.rut = StringVar()
        self.entry_rut = Entry(self, width=20, textvariable=self.rut)
        self.entry_rut.configure(bg="#DADDD8")
        self.entry_rut.grid(row=0, column=1)
        #entry_rut.pack(pady=10) 

        # #Añade el texto para ingresar rut en el frame
        self.texto_nombre = Label(self, text="Nombre completo:", font='Helvetica 12 bold')
        self.texto_nombre.configure(bg="#1C1C1C", fg="#ffffff")
        self.texto_nombre.grid(row=1, column=0)
        # texto_nombre.pack()
        
        # #Añade la entrada para el rut del usuario
        self.nombre = StringVar()
        self.entry_usuario = Entry(self, width=20, textvariable=self.nombre)
        self.entry_usuario.configure(bg="#DADDD8")
        self.entry_usuario.grid(row=1, column=1)
        #entry_usuario.pack(pady=10) 

        # #Añade el texto para ingresar rut en el frame
        self.texto_contraseña = Label(self, text="Contraseña:", font='Helvetica 12 bold')
        self.texto_contraseña.configure(bg="#1C1C1C", fg="#ffffff")
        self.texto_contraseña.grid(row=2, column=0)
        # texto_contraseña.pack()
        
        # #Añade la entrada para el rut del usuario
        self.contraseña = StringVar()
        self.entry_contraseña = Entry(self, width=20, textvariable=self.contraseña)
        self.entry_contraseña.configure(bg="#DADDD8")
        self.entry_contraseña.grid(row=2, column=1)
        #entry_contraseña.pack(pady=10) 

        # #Añade el texto para ingresar rut en el frame
        self.texto_sueldo = Label(self, text="Sueldo:", font='Helvetica 12 bold')
        self.texto_sueldo.configure(bg="#1C1C1C", fg="#ffffff")
        self.texto_sueldo.grid(row=3, column=0)
        # texto_sueldo.pack()
        
        # #Añade la entrada para el rut del usuario
        self.sueldo = StringVar()
        self.entry_sueldo = Entry(self, width=20, textvariable=self.sueldo)
        self.entry_sueldo.configure(bg="#DADDD8")
        self.entry_sueldo.grid(row=3, column=1)
        # entry_sueldo.pack(pady=10) 

        self.boton_añadir_empleado = Button(self, 
                                            text="Añadir empleado", 
                                            font='Helvetica 10 bold', 
                                            command=lambda:self.controller.añadir_empleado(
                                                self.rut.get(),
                                                self.contraseña.get(),
                                                self.nombre.get(),
                                                self.sueldo.get()
                                            ))
        self.boton_añadir_empleado.configure(bg="#9FA0FF")
        self.boton_añadir_empleado.grid(row=2, column=2, padx=20)

        self.boton_eliminar_empleado = Button(self, text="Eliminar empleado", font='Helvetica 10 bold', command=lambda:self.controller.eliminar_empleado())
        self.boton_eliminar_empleado.configure(bg="#9FA0FF")
        self.boton_eliminar_empleado.grid(row=3, column=2, padx=20)
        #self.boton_eliminar_empleado.pack(pady=10)

        self.treeview = ttk.Treeview(self, columns=("id", "nombre", "sueldo"))
        self.treeview.tag_bind(
            "selected", "<<TreeviewSelect>>", self.item_selected)

        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="NOMBRE")
        self.treeview.heading("#2", text="SUELDO")

        self.treeview.grid(row=4, column=0, rowspan=10, columnspan=10)
        #self.treeview.pack()

        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminLocal))
        self.boton_retroceder.configure(bg="#9FA0FF")
        self.boton_retroceder.grid(row=15, column=1, pady=40)
        #self.boton_retroceder.pack(pady=10)

        self.pack()

    def set_empleados(self, empleados: list):
        for empleado in empleados:
            item= self.treeview.insert("", 
                                END, 
                                text=empleado[0],
                                values=(empleado[1], empleado[2]),
                                tags=("selected"))

            print(item)

    def añadir_empleado(self, empleado):
        item = self.treeview.insert("",
                             END,
                             text=empleado.rut,
                            values=(empleado.nombre, empleado.sueldo),
                            tags=("selected"))
        print(item)

    def item_selected(self, event):
        curl_item = self.treeview.focus()

        self.selected_empleado = (curl_item, self.treeview.item(curl_item)['text'])

    def eliminar_empleado(self, curl_item):
        try:
            self.treeview.delete(curl_item)
            self.selected_empleado = None
        except:
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