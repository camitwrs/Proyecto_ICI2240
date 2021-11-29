from tkinter import Frame, Label, Button, END
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

        self.boton_eliminar_empleado = Button(self, text="Eliminar empleado", font='Helvetica 10 bold', command=lambda:self.controller.eliminar_empleado())
        self.boton_eliminar_empleado.configure(bg="#9FA0FF")
        self.boton_eliminar_empleado.pack(pady=10)


        self.treeview = ttk.Treeview(self, columns=("id", "nombre", "sueldo"))
        self.treeview.tag_bind(
            "selected", "<<TreeviewSelect>>", self.item_selected)

        self.treeview.heading("#0", text="ID")
        self.treeview.heading("#1", text="NOMBRE")
        self.treeview.heading("#2", text="SUELDO")

        self.treeview.pack()

        self.boton_retroceder = Button(self, text="Confirmar", font='Helvetica 10 bold', command=lambda:master.switch_frame(PageAdminLocal))
        self.boton_retroceder.configure(bg="#9FA0FF")
        self.boton_retroceder.pack(pady=10)

        self.pack()

    def set_empleados(self, empleados: list):
        for empleado in empleados:
            item= self.treeview.insert("", 
                                END, 
                                text=empleado[0],
                                values=(empleado[1], empleado[2]),
                                tags=("selected"))

            print(item)

    def item_selected(self, event):
        curl_item = self.treeview.focus()

        self.selected_empleado = (curl_item, self.treeview.item(curl_item)['text'])

    def eliminar_empleado(self, curl_item):
        self.treeview.delete(curl_item)



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