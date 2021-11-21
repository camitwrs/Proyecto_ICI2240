from tkinter import *
from tkinter import messagebox

def ingresar():
    # Asume que el que entra es un EMPLEADO. Funciona con user: 20603557 y pass: 2310
    if usuario.get() == "20603557" and contra.get() == "2310": 
        abrir_ventana2()
    # Asume que el que entra es un ADMIN LOCAL. Funciona con user: 11111111 y pass: 2310
    elif usuario.get() == "11111111" and contra.get() == "2310":
        abrir_ventana4()
    # Asume que el que entra es un ADMIN GLOBAL. Funciona con user: 22222222 y pass: 2310
    elif usuario.get() == "22222222" and contra.get() == "2310":
        abrir_ventana6()
    else:   
        messagebox.showinfo("LOGIN", "Error. Inténtelo nuevamente")

def abrir_ventana2(): # MENÚ EMPLEADO
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("EMPLEADO")
    ventana2.geometry("960x540")
    ventana2.configure(bg="#1C1C1C")
    label1 = Label(ventana2, text="MENÚ EMPLEADO:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=80)
    boton1 = Button(ventana2, text="Realizar venta", font='Helvetica 9 bold', command=lambda:abrir_ventana3(ventana2))
    boton1.configure(bg="#ECEBE4")
    boton1.pack(pady=10)
    boton2 = Button(ventana2, text="Marcar asistencia", font='Helvetica 9 bold', command=marcar_asistencia)
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10)
    boton3 = Button(ventana2, text="Informe de ventas", font='Helvetica 9 bold', command=informe_ventas)
    boton3.configure(bg="#ECEBE4")
    boton3.pack(pady=10)
    boton4 = Button(ventana2, text="Ver horario", font='Helvetica 9 bold', command=mostrar_horario)
    boton4.configure(bg="#ECEBE4")
    boton4.pack(pady=10)

def abrir_ventana3(ventana): # SUBMENÚ EMPLEADO - REALIZAR VENTA
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("EMPLEADO")
    ventana3.geometry("960x540")
    ventana3.configure(bg="#1C1C1C")
    label1 = Label(ventana3, text="SUBMENÚ REALIZAR VENTA:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=80)
    boton1 = Button(ventana3, text="Vender entrada", font='Helvetica 9 bold', command=venta_entrada)
    boton1.configure(bg="#ECEBE4")
    boton1.pack(pady=10)
    boton2 = Button(ventana3, text=" Aplicar descuento", font='Helvetica 9 bold', command=aplicar_descuento)
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10)
    boton3 = Button(ventana3, text="Concretar venta", font='Helvetica 9 bold', command=concretar_venta)
    boton3.configure(bg="#ECEBE4")
    boton3.pack( pady=10)
    boton4 = Button(ventana3, text="Cancelar venta", font='Helvetica 9 bold', command=cancelar_venta)
    boton4.configure(bg="#ECEBE4")
    boton4.pack(pady=10)      

def marcar_asistencia():
    pass

def informe_ventas():
    pass

def mostrar_horario():
    pass
    
def venta_entrada(): # Hay que agrandar la ventana
    pass

def aplicar_descuento():
    pass

def concretar_venta():
    pass

def cancelar_venta():
    pass

def abrir_ventana4(): # MENÚ ADMIN LOCAL
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("ADMIN LOCAL")
    ventana2.geometry("960x540")
    ventana2.configure(bg="#1C1C1C")
    label1 = Label(ventana2, text="MENÚ ADMINISTRADOR LOCAL:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=80)
    boton1 = Button(ventana2, text="Resumen general", font='Helvetica 9 bold', command=resumen_general)
    boton1.configure(bg="#ECEBE4")
    boton1.pack(pady=10)
    boton2 = Button(ventana2, text="Modificar cartelera", font='Helvetica 9 bold', command=lambda:abrir_ventana5(ventana2))
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10)
    boton3 = Button(ventana2, text="Informe de ventas", font='Helvetica 9 bold', command=informe_ventas)
    boton3.configure(bg="#ECEBE4")
    boton3.pack(pady=10)
    boton4 = Button(ventana2, text="Ver horario", font='Helvetica 9 bold', command=mostrar_horario)
    boton4.configure(bg="#ECEBE4")
    boton4.pack(pady=10)
    
def resumen_general():
    pass

def abrir_ventana5(ventana): # SUBMENÚ ADMIN LOCAL - MODIFICAR CARTELERA
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("ADMIN LOCAL")
    ventana3.geometry("960x540")
    ventana3.configure(bg="#1C1C1C")
    label1 = Label(ventana3, text="SUBMENÚ MODIFICAR CARTELERA:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=80)
    boton1 = Button(ventana3, text="Añadir película", font='Helvetica 9 bold', command=anadir_pelicula)
    boton1.configure(bg="#ECEBE4")
    boton1.pack( pady=10)
    boton2 = Button(ventana3, text="Añadir funciones", font='Helvetica 9 bold', command=anadir_funciones)
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10)
    boton3 = Button(ventana3, text="Cancelar funciones", font='Helvetica 9 bold', command=cancelar_funciones)
    boton3.configure(bg="#ECEBE4")
    boton3.pack(pady=10)
    boton4 = Button(ventana3, text="Modificar precio funciones", font='Helvetica 9 bold', command=modificar_precios)
    boton4.configure(bg="#ECEBE4")
    boton4.pack( pady=10)   

def anadir_pelicula():
    pass

def anadir_funciones():
    pass

def cancelar_funciones():
    pass

def modificar_precios():
    pass

def abrir_ventana6(): # MENÚ ADMINISTRADOR GLOBAL
    root.withdraw()
    ventana2 = Toplevel()
    ventana2.title("ADMIN GLOBAL")
    ventana2.geometry("960x540")
    ventana2.configure(bg="#1C1C1C")
    label1 = Label(ventana2, text="MENÚ ADMINISTRADOR GLOBAL:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=70)
    boton1 = Button(ventana2, text="Modificar administradores", font='Helvetica 9 bold', command=lambda:abrir_ventana7(ventana2))
    boton1.configure(bg="#ECEBE4")
    boton1.pack(pady=10)
    boton2 = Button(ventana2, text="Modificar cine", font='Helvetica 9 bold', command=modificar_cine)
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10)
    boton3 = Button(ventana2, text="Ver información cine", font='Helvetica 9 bold', command=mostrar_info_cine)
    boton3.configure(bg="#ECEBE4")
    boton3.pack(pady=10)
    boton4 = Button(ventana2, text="Modificar precios películas", font='Helvetica 9 bold', command=modificar_precios_totales)
    boton4.configure(bg="#ECEBE4")
    boton4.pack(pady=10)
    boton5 = Button(ventana2, text="Generar cupones de descuento", font='Helvetica 9 bold', command=generar_cupones)
    boton5.configure(bg="#ECEBE4")
    boton5.pack(pady=10)
    boton6 = Button(ventana2, text="Realizar reporte", font='Helvetica 9 bold', command=realizar_reporte)
    boton6.configure(bg="#ECEBE4")
    boton6.pack(pady=10)
    
def abrir_ventana7(ventana): # SUBMENÚ ADMIN GLOBAL - MODIFICAR ADMINS
    root.withdraw()
    ventana.withdraw()
    ventana3 = Toplevel()
    ventana3.title("ADMIN GLOBAL")
    ventana3.geometry("960x540")
    ventana3.configure(bg="#1C1C1C")
    label1 = Label(ventana3, text="SUBMENÚ MODIFICAR ADMINISTRADORES:", font='Helvetica 12 bold')
    label1.configure(bg="#1C1C1C", fg="#ffffff")
    label1.pack(pady=80)
    boton1 = Button(ventana3, text="Agregar administrador local", font='Helvetica 9 bold', command=agregar_adminlocal)
    boton1.configure(bg="#ECEBE4")
    boton1.pack(pady=10)
    boton2 = Button(ventana3, text="Eliminar administrador local", font='Helvetica 9 bold', command=eliminar_adminlocal)
    boton2.configure(bg="#ECEBE4")
    boton2.pack(pady=10) 

def agregar_adminlocal():
    pass

def eliminar_adminlocal():
    pass

def modificar_cine():
    pass

def mostrar_info_cine():
    pass

def modificar_precios_totales():
    pass

def generar_cupones():
    pass

def realizar_reporte():
    pass

################################ MENÚ PRINCIPAL - LOGIN #############################################

root = Tk()
root.title("CINE4U")
root.iconbitmap(r'Programa Python\icon.ico')
root.geometry("960x540")
root.configure(bg="#1C1C1C")
root.resizable(width=False, height=False)

label_titulo = Label(root, text="CINE4U", font='Helvetica 30 bold')
label_titulo.configure(bg="#1C1C1C", fg="#ffffff")
label_titulo.pack(pady=70)

label_usuario = Label(root, text="Ingrese su RUT:", font='Helvetica 12 bold')
label_usuario.configure(bg="#1C1C1C", fg="#ffffff")
label_usuario.pack()
usuario = StringVar()
entry_usuario = Entry(root, width=30, textvariable=usuario)
entry_usuario.configure(bg="#DADDD8")
entry_usuario.pack(pady=10)

label_pass = Label(root, text="Ingrese su contraseña:", font='Helvetica 12 bold')
label_pass.configure(bg="#1C1C1C", fg="#ffffff")
label_pass.pack()
contra = StringVar()
entry_pass = Entry(root, width=30, show="*", textvariable=contra)
entry_pass.configure(bg="#DADDD8")
entry_pass.pack(pady=10)

boton_principal = Button(root, text="Entrar", command=ingresar, font='Helvetica 9 bold')
boton_principal.configure(bg="#ECEBE4")
boton_principal.pack(pady=10)

reminder = Label(root, text="Recordar: RUT sin puntos ni dígito verificador.", font='Helvetica 8 ')
reminder.configure(bg="#1C1C1C", fg="#ffffff")
reminder.pack(pady=80)

root.mainloop()