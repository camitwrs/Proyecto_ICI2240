from tkinter import Frame, Label, Button, END, StringVar, Entry
from tkinter import ttk


class PageAdminLocal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Espacio en blanco, estética
        title = Label(self)
        title.configure(bg="#33353d")
        title.pack(pady=30)
        
        #Añade el texto del menú
        label1 = Label(self, text="MENÚ ADMINISTRADOR LOCAL:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=50)
        
        #Añade los botones de las distintas opciones
        boton2 = Button(self, text="Modificar cartelera", font='Helvetica 10 bold', command=lambda:master.switch_frame(SubPageAdminLocal))
        boton2.configure(bg="#cccccccff", fg="#1c1c1c")
        boton2.pack(pady=10)
        boton4 = Button(self, text="Modificar empleados", font='Helvetica 10 bold', command=lambda:self.controller.boton_modificar_empleados())
        boton4.configure(bg="#cccccccff", fg="#1c1c1c")
        boton4.pack(pady=10)
        boton6 = Button(self, text="Modificar salas", font='Helvetica 10 bold', command=lambda:self.controller.boton_modificar_salas())
        boton6.configure(bg="#cccccccff", fg="#1c1c1c")
        boton6.pack(pady=10)
        
class PageAñadirPelicula(Frame):
     def __init__(self, master):
        self.controller = master.controller

        Frame.__init__(self, master)
        self.configure(bg="#33353d")

        formato_opciones = ['Doblada', 'Subtitulada']
        
        self.label_nombre = Label(self, text="Nombre", font='Helvetica 12 bold')
        self.label_nombre.configure(bg="#33353d", fg="#cccccccff")
        self.label_nombre.grid(row=0, column=0, pady=5)

        self.nombre = StringVar()
        self.entry_nombre = Entry(self, width=20, textvariable=self.nombre)
        self.entry_nombre.configure(bg="#e6e1da")
        self.entry_nombre.grid(row=0, column=1, pady=5)

        self.label_año = Label(self, text="Año", font='Helvetica 12 bold')
        self.label_año.configure(bg="#33353d", fg="#cccccccff")
        self.label_año.grid(row=1, column=0, pady=5)
        
        self.año = StringVar()
        self.entry_año = Entry(self, width=20, textvariable=self.año)
        self.entry_año.configure(bg="#e6e1da")
        self.entry_año.grid(row=1, column=1, pady=5)

        self.label_duracion = Label(self, text="Duracion (minutos)", font='Helvetica 12 bold')
        self.label_duracion.configure(bg="#33353d", fg="#cccccccff")
        self.label_duracion.grid(row=2, column=0, pady=5)
        
        self.duracion = StringVar()
        self.entry_duracion = Entry(self, width=20, textvariable=self.duracion)
        self.entry_duracion.configure(bg="#e6e1da")
        self.entry_duracion.grid(row=2, column=1, pady=5)

        self.label_precio = Label(self, text="Precio", font='Helvetica 12 bold')
        self.label_precio.configure(bg="#33353d", fg="#cccccccff")
        self.label_precio.grid(row=3, column=0, pady=5)
        
        self.precio = StringVar()
        self.entry_precio = Entry(self, width=20, textvariable=self.precio)
        self.entry_precio.configure(bg="#e6e1da")
        self.entry_precio.grid(row=3, column=1, pady=5)

        self.label_generos = Label(self, text="Géneros (separados por coma)", font='Helvetica 12 bold')
        self.label_generos.configure(bg="#33353d", fg="#cccccccff")
        self.label_generos.grid(row=4, column=0, pady=5)
        
        self.generos = StringVar()
        self.entry_generos = Entry(self, width=20, textvariable=self.generos)
        self.entry_generos.configure(bg="#e6e1da")
        self.entry_generos.grid(row=4, column=1, pady=5)

        self.combo1 = ttk.Combobox(self, state="readonly", width=50, values=formato_opciones)                        
        self.combo1.grid(row=5, column=0, columnspan=6)

        self.boton_retroceder = Button(self, 
                                       text="Guardar", 
                                       font='Helvetica 10 bold', 
                                       command=lambda:self.controller.añadir_pelicula(
                                           self.nombre.get(),
                                           self.año.get(),
                                           self.duracion.get(),
                                           self.precio.get(),
                                           self.generos.get(),
                                           self.combo1.get()
                                       ))
        self.boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        self.boton_retroceder.grid(row=6, column=0, pady=10, columnspan=6)

        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminLocal))
        self.boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        self.boton_retroceder.grid(row=7, column=0, pady=10, columnspan=6)

class PageModificarEmpleados(ttk.Frame): 
    """
        FALTA AGREGAR LA OPCION PARA AÑADIR EMPLEADOS, OSEA TODOS LOS INPUT DE DATOS Y UN BOTÓN PARA AGREGAR
    """
    def __init__(self, master):
        self.controller = master.controller
        self.selected_empleado = None

        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Añade el texto para ingresar rut en el frame
        self.texto_rut = Label(self, text="RUT:", font='Helvetica 12 bold')
        self.texto_rut.configure(bg="#33353d", fg="#cccccccff")
        self.texto_rut.grid(row=0, column=0, pady=(50, 0))
        
        # #Añade la entrada para el rut del usuario
        self.rut = StringVar()
        self.entry_rut = Entry(self, width=20, textvariable=self.rut)
        self.entry_rut.configure(bg="#e6e1da")
        self.entry_rut.grid(row=0, column=1, pady=(50, 0))

        # #Añade el texto para ingresar rut en el frame
        self.texto_nombre = Label(self, text="Nombre completo:", font='Helvetica 12 bold')
        self.texto_nombre.configure(bg="#33353d", fg="#cccccccff")
        self.texto_nombre.grid(row=1, column=0)
        
        # #Añade la entrada para el rut del usuario
        self.nombre = StringVar()
        self.entry_usuario = Entry(self, width=20, textvariable=self.nombre)
        self.entry_usuario.configure(bg="#e6e1da")
        self.entry_usuario.grid(row=1, column=1)
        #entry_usuario.pack(pady=10) 

        # #Añade el texto para ingresar rut en el frame
        self.texto_contraseña = Label(self, text="Contraseña:", font='Helvetica 12 bold')
        self.texto_contraseña.configure(bg="#33353d", fg="#cccccccff")
        self.texto_contraseña.grid(row=2, column=0)
        # texto_contraseña.pack()
        
        # #Añade la entrada para el rut del usuario
        self.contraseña = StringVar()
        self.entry_contraseña = Entry(self, width=20, textvariable=self.contraseña)
        self.entry_contraseña.configure(bg="#e6e1da")
        self.entry_contraseña.grid(row=2, column=1)
        #entry_contraseña.pack(pady=10) 

        # #Añade el texto para ingresar rut en el frame
        self.texto_sueldo = Label(self, text="Sueldo:", font='Helvetica 12 bold')
        self.texto_sueldo.configure(bg="#33353d", fg="#cccccccff")
        self.texto_sueldo.grid(row=3, column=0)
        # texto_sueldo.pack()
        
        # #Añade la entrada para el rut del usuario
        self.sueldo = StringVar()
        self.entry_sueldo = Entry(self, width=20, textvariable=self.sueldo)
        self.entry_sueldo.configure(bg="#e6e1da")
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
        self.boton_añadir_empleado.configure(bg="#cccccccff", fg="#1c1c1c")
        self.boton_añadir_empleado.grid(row=2, column=2, padx=20)

        self.boton_eliminar_empleado = Button(self, text="Eliminar empleado", font='Helvetica 10 bold', command=lambda:self.controller.eliminar_empleado())
        self.boton_eliminar_empleado.configure(bg="#cccccccff", fg="#1c1c1c")
        self.boton_eliminar_empleado.grid(row=3, column=2, padx=20)
        #self.boton_eliminar_empleado.pack(pady=10)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#33353d",
                fieldbackground="#33353d", foreground="#cccccccff")
        
        self.treeview = ttk.Treeview(self, columns=("id", "nombre", "sueldo"))
        self.treeview.tag_bind(
            "selected", "<<TreeviewSelect>>", self.item_selected)

        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="NOMBRE")
        self.treeview.heading("#2", text="SUELDO")

        self.treeview.grid(row=4, column=0, rowspan=10, columnspan=10)
        #self.treeview.pack()

        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminLocal))
        self.boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
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


class PageModificarSalas(Frame):
    def __init__(self, master):
        self.controller = master.controller
        self.selected_sala = None

        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#33353d")

        self.boton_habilitar_sala = Button(self, 
                                    text="Habilitar sala", 
                                    font='Helvetica 10 bold', 
                                    command=lambda:self.controller.habilitar_sala())
        self.boton_habilitar_sala.configure(bg="#cccccccff", fg="#1c1c1c")
        self.boton_habilitar_sala.grid(row=0, column=0, pady=(80, 0))

        self.boton_deshabilitar_sala = Button(self, 
                            text="Deshabilitar sala", 
                            font='Helvetica 10 bold', 
                            command=lambda:self.controller.deshabilitar_sala())
        self.boton_deshabilitar_sala.configure(bg="#cccccccff", fg="#1c1c1c")
        self.boton_deshabilitar_sala.grid(row=0, column=1, padx=50, pady=(80, 0))

        self.espacio = Label(self)
        self.espacio.configure(bg="#33353d")
        self.espacio.grid(pady=10)
        
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#33353d",
                fieldbackground="#33353d", foreground="#cccccccff")

        self.treeview = ttk.Treeview(self, columns=("id", "nombre", "sueldo"))
        self.treeview.tag_bind(
            "selected", "<<TreeviewSelect>>", self.item_selected)

        self.treeview.heading("#0", text="NÚMERO")
        self.treeview.heading("#1", text="CAPACIDAD")
        self.treeview.heading("#2", text="ESTADO")

        self.treeview.grid(row=2, column=0, rowspan=10, columnspan=10)


        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminLocal))
        self.boton_retroceder.configure(bg="#ec646c", fg="#1c1c1c")
        self.boton_retroceder.grid(row=13, column=1, pady=40)

    def item_selected(self, event):
        curl_item = self.treeview.focus()

        self.selected_sala = (curl_item, self.treeview.item(curl_item))

    def set_salas(self, salas: list):
        for sala in salas.values():
            item = self.treeview.insert("", 
                                        END, 
                                        text=sala[0],
                                        values=(sala[1], sala[2]),
                               tags=("selected"))

    def update_sala(self, sala, text, values):
        if values[1] == 'Habilitada':
            values[1] = 'Deshabilitada'
        else:
            values[1] = 'Habilitada'
            
        self.treeview.item(sala, text=text, values=values)

class SubPageAdminLocal(Frame):
    def __init__(self, master):
        self.controller = master.controller
        
        #Añade los botones de las distintas opciones
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        title = Label(self)
        title.configure(bg="#33353d")
        title.pack(pady=30)
        
        #Añade el texto del menú
        label1 = Label(self, text="SUBMENÚ MODIFICAR CARTELERA:", font='Helvetica 12 bold')
        label1.configure(bg="#33353d", fg="#cccccccff")
        label1.pack(pady=50)
        
        #Añade los botones de las distintas opciones
        boton1 = Button(self, text="Añadir película", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAñadirPelicula))
        boton1.configure(bg="#cccccccff", fg="#1c1c1c")
        boton1.pack( pady=10)