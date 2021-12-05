from tkinter import Frame, Label, StringVar, Entry, Button

class PageLogin(Frame):
    def __init__(self, master):
        self.controller = master.controller

        #Crea el frame del mismo color de fondo
        Frame.__init__(self, master)
        self.configure(bg="#33353d")
        
        #Añade el título del programa en el frame, con colores y posición (configure y pack)
        texto_titulo = Label(self, text="CINE4U", font='Helvetica 30 bold')
        texto_titulo.configure(bg="#33353d", fg="#cccccccff")
        texto_titulo.pack(pady=70)
        
        #Añade el texto para ingresar rut en el frame
        texto_usuario = Label(self, text="Ingrese su RUT:", font='Helvetica 12 bold')
        texto_usuario.configure(bg="#33353d", fg="#cccccccff")
        texto_usuario.pack()
        
        #Añade la entrada para el rut del usuario
        usuario = StringVar()
        entry_usuario = Entry(self, width=20, textvariable=usuario)
        entry_usuario.configure(bg="#e6e1da")
        entry_usuario.pack(pady=10) 
        
        #Añade el texto para ingresar la contraseña en el frame
        texto_contra = Label(self, text="Ingrese su contraseña:", font='Helvetica 12 bold')
        texto_contra.configure(bg="#33353d", fg="#cccccccff")
        texto_contra.pack()
        
        #Añade la entrada para la contraseña del usuario
        contra = StringVar()
        entry_contra = Entry(self, width=20, show="*", textvariable=contra)
        entry_contra.configure(bg="#e6e1da")
        entry_contra.pack(pady=10)
        
        #Añade el botón entrar en el frame
        boton_principal = Button(self, text="Entrar", 
                                command=lambda:self.controller.ingresar(usuario.get(), contra.get()), 
                                font='Helvetica 9 bold')
        boton_principal.configure(bg="#ec646c", fg="#1c1c1c")
        boton_principal.pack(pady=10)
        
        #Añade el texto de recordatorio
        reminder = Label(self, text="Recordar: RUT sin puntos ni dígito verificador.", font='Helvetica 9')
        reminder.configure(bg="#33353d", fg="#cccccccff")
        reminder.pack(pady=80)
